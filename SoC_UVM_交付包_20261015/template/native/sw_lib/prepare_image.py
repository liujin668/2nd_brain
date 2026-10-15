#!/usr/bin/env python3
"""Validate static ELF64 AArch64 images and export PT_LOAD segments.

No third party dependencies. Does not execute or relocate firmware. The result
must be adapted to the actual VIP memory loader; it is not an ELF boot loader.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys

UINT64_LIMIT = 1 << 64


def number(value):
    return int(value, 0)


def checked_end(start, size):
    if start < 0 or size < 0 or start >= UINT64_LIMIT or start + size > UINT64_LIMIT:
        raise ValueError("address range overflows 64 bits")
    return start + size


def region(value):
    try:
        base, size = (number(x) for x in value.split(":"))
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError("region must be BASE:SIZE, decimal or 0x hex")
    if size <= 0:
        raise argparse.ArgumentTypeError("region size must be positive")
    try:
        checked_end(base, size)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc))
    return base, size


def inspect_elf(data, address_kind, regions):
    if address_kind not in ("paddr", "vaddr"):
        raise ValueError("address_kind must be explicitly paddr or vaddr")
    if not regions:
        raise ValueError("at least one permitted memory region is required")
    for base, size in regions:
        if size <= 0:
            raise ValueError("empty permitted memory region")
        checked_end(base, size)
    if len(data) < 64 or data[:4] != b"\x7fELF":
        raise ValueError("not a complete ELF header")
    if data[4:7] != bytes((2, 1, 1)):
        raise ValueError("only ELF64 little-endian version 1 is supported")
    header = struct.unpack_from("<16sHHIQQQIHHHHHH", data)
    _, elf_type, machine, version, entry, phoff, _, _, ehsize, phentsize, phnum, _, _, _ = header
    if elf_type != 2 or machine != 183 or version != 1:
        raise ValueError("requires static ET_EXEC AArch64 image, no PIE/relocation")
    if ehsize != 64 or phentsize != 56 or phnum in (0, 0xffff):
        raise ValueError("unsupported ELF header/program-header layout")
    if phoff < ehsize or phoff + phentsize * phnum > len(data):
        raise ValueError("program-header table outside file")
    segments = []
    entries = []
    for index in range(phnum):
        p_type, flags, offset, vaddr, paddr, filesz, memsz, align = struct.unpack_from(
            "<IIQQQQQQ", data, phoff + index * phentsize)
        if p_type in (2, 3):
            raise ValueError("dynamic/interpreter segments are unsupported")
        if p_type != 1:
            continue
        if filesz > memsz or offset + filesz > len(data):
            raise ValueError("invalid PT_LOAD file/memory size")
        if memsz == 0:
            continue
        if align > 1 and ((align & (align - 1)) or (vaddr - offset) % align):
            raise ValueError("invalid PT_LOAD alignment")
        load_addr = paddr if address_kind == "paddr" else vaddr
        end = checked_end(load_addr, memsz)
        vend = checked_end(vaddr, memsz)
        if not any(base <= load_addr and end <= base + size for base, size in regions):
            raise ValueError("PT_LOAD lies outside permitted memory regions")
        for previous in segments:
            if load_addr < previous["load_address"] + previous["memory_size"] and previous["load_address"] < end:
                raise ValueError("overlapping PT_LOAD memory ranges require an explicit loader policy")
        payload = data[offset:offset + filesz]
        segment = {
            "index": index, "load_address": load_addr, "virtual_address": vaddr,
            "physical_address": paddr, "file_size": filesz, "memory_size": memsz,
            "zero_fill": memsz - filesz, "flags": flags,
            "file": "segment_{:02d}.bin".format(index),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "source_offset": offset
        }
        segments.append(segment)
        if flags & 1 and vaddr <= entry < vaddr + filesz:
            entries.append(load_addr + entry - vaddr)
    if not segments or len(entries) != 1:
        raise ValueError("entry must uniquely map to file-backed executable PT_LOAD bytes")
    return {
        "schema_version": 1, "format": "ELF64_LE_AARCH64_ET_EXEC",
        "address_kind": address_kind, "entry_virtual": entry,
        "entry_load_address": entries[0], "boot_entry_validated": False,
        "requires_address_translation": any(s["load_address"] != s["virtual_address"] for s in segments),
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "allowed_regions": [{"base": b, "size": s} for b, s in regions],
        "segments": segments,
        "loader_contract": "write file bytes at load_address then zero_fill bytes; verify through actual backing store"
    }


def export_image(source, destination, address_kind, regions):
    data = Path(source).read_bytes()
    manifest = inspect_elf(data, address_kind, regions)
    output = Path(destination)
    # Exclusive directory creation prevents a stale manifest/segment mixture.
    output.mkdir(parents=True, exist_ok=False)
    for segment in manifest["segments"]:
        start = segment["source_offset"]
        (output / segment["file"]).write_bytes(data[start:start + segment["file_size"]])
    (output / "image_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("elf", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--address-kind", required=True, choices=("paddr", "vaddr"))
    parser.add_argument("--region", required=True, action="append", type=region)
    args = parser.parse_args()
    try:
        result = export_image(args.elf, args.out, args.address_kind, args.region)
    except (ValueError, OSError, struct.error) as exc:
        print("IMAGE_PREPARE_ERROR: {}".format(exc), file=sys.stderr)
        return 2
    print("{} PT_LOAD segments; mapped entry=0x{:x}; {}".format(
        len(result["segments"]), result["entry_load_address"], args.out / "image_manifest.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())


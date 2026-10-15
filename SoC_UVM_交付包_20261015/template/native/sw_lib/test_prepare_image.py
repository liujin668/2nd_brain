import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("prepare_image", Path(__file__).with_name("prepare_image.py"))
IMAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMAGE)


def make_elf(load=0x100000000, vaddr=0x80000000, filesz=4, memsz=16):
    ident = b"\x7fELF" + bytes((2, 1, 1)) + bytes(9)
    header = struct.pack("<16sHHIQQQIHHHHHH", ident, 2, 183, 1, vaddr,
                         64, 0, 0, 64, 56, 1, 0, 0, 0)
    ph = struct.pack("<IIQQQQQQ", 1, 5, 120, vaddr, load, filesz, memsz, 1)
    return header + ph + b"ABCD"


class ImageTests(unittest.TestCase):
    def test_64bit_address_and_bss(self):
        out = IMAGE.inspect_elf(make_elf(), "paddr", [(0x100000000, 0x1000)])
        self.assertEqual(out["entry_load_address"], 0x100000000)
        self.assertEqual(out["segments"][0]["zero_fill"], 12)

    def test_virtual_mapping_is_explicit(self):
        out = IMAGE.inspect_elf(make_elf(), "vaddr", [(0x80000000, 0x1000)])
        self.assertEqual(out["entry_load_address"], 0x80000000)

    def test_wrong_region(self):
        with self.assertRaises(ValueError):
            IMAGE.inspect_elf(make_elf(), "paddr", [(0, 0x1000)])

    def test_wrong_isa(self):
        data = bytearray(make_elf())
        struct.pack_into("<H", data, 18, 243)
        with self.assertRaises(ValueError):
            IMAGE.inspect_elf(data, "paddr", [(0x100000000, 0x1000)])

    def test_truncated_file(self):
        with self.assertRaises(ValueError):
            IMAGE.inspect_elf(make_elf()[:-1], "paddr", [(0x100000000, 0x1000)])

    def test_bad_memory_size(self):
        with self.assertRaises(ValueError):
            IMAGE.inspect_elf(make_elf(memsz=2), "paddr", [(0x100000000, 0x1000)])

    def test_pie_rejected(self):
        data = bytearray(make_elf())
        struct.pack_into("<H", data, 16, 3)
        with self.assertRaises(ValueError):
            IMAGE.inspect_elf(data, "paddr", [(0x100000000, 0x1000)])

    def test_export_and_stale_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "demo.elf"
            source.write_bytes(make_elf())
            output = root / "image"
            IMAGE.export_image(source, output, "paddr", [(0x100000000, 0x1000)])
            self.assertEqual((output / "segment_00.bin").read_bytes(), b"ABCD")
            self.assertTrue((output / "image_manifest.json").is_file())
            with self.assertRaises(FileExistsError):
                IMAGE.export_image(source, output, "paddr", [(0x100000000, 0x1000)])


if __name__ == "__main__":
    unittest.main()

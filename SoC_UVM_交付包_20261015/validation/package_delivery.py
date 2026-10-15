#!/usr/bin/env python3
"""Validate and archive this delivery; excludes generated runs and local site config."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def include(path):
    rel = path.relative_to(ROOT)
    return (not any(part in ("__pycache__", ".git") for part in rel.parts)
            and not rel.as_posix().startswith("template/regress/out/")
            and rel.as_posix() != "template/config/site.json"
            and path.suffix not in (".pyc", ".pyo")
            and path.name != "SHA256SUMS")


def main():
    archive = ROOT.with_name(ROOT.name + ".zip")
    if archive.exists():
        raise SystemExit("Archive already exists; choose a new delivery version before packaging")
    check = subprocess.run([sys.executable, str(ROOT / "validation" / "check_bundle.py")],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           encoding="utf-8", errors="replace", timeout=60)
    if check.returncode:
        print(check.stdout, check.stderr)
        return 1
    integrity = json.loads(check.stdout)
    (ROOT / "validation" / "evidence" / "final_integrity.json").write_text(
        json.dumps(integrity, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and include(p))
    hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in files}
    manifest = ROOT / "SHA256SUMS"
    manifest.write_text("".join(digest + "  " + name + "\n" for name, digest in hashes.items()),
                        encoding="utf-8")
    files.append(manifest)
    with zipfile.ZipFile(archive, "x", zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for path in files:
            output.write(path, ROOT.name + "/" + path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(archive, "r") as completed:
        if completed.testzip() is not None:
            raise RuntimeError("Archive CRC validation failed")
        for name, digest in hashes.items():
            if hashlib.sha256(completed.read(ROOT.name + "/" + name)).hexdigest() != digest:
                raise RuntimeError("Archived file hash mismatch: " + name)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_name(archive.name + ".sha256").write_text(
        digest + "  " + archive.name + "\n", encoding="utf-8")
    print(json.dumps(dict(status="PASS", archive=str(archive), file_count=len(files),
                          size_bytes=archive.stat().st_size, sha256=digest), ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

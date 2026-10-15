#!/usr/bin/env python3
"""Delivery integrity checks; this is not an HDL compiler or simulator."""
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {"__pycache__", ".git"}


def included(path):
    rel = path.relative_to(ROOT)
    return not any(part in EXCLUDE for part in rel.parts) and "regress/out" not in rel.as_posix()


def main():
    files = [p for p in ROOT.rglob("*") if p.is_file() and included(p)]
    errors = []
    counts = {"python": 0, "json": 0, "markdown": 0, "sv": 0, "svh": 0}
    by_name = {}
    for p in files:
        by_name.setdefault(p.name, []).append(p)
    for path in files:
        suffix = path.suffix.lower()
        try:
            if suffix == ".py":
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
                counts["python"] += 1
            elif suffix == ".json":
                json.loads(path.read_text(encoding="utf-8-sig"))
                counts["json"] += 1
            elif suffix == ".md":
                text = path.read_text(encoding="utf-8-sig")
                counts["markdown"] += 1
                fences = re.findall(r"^\s*```", text, re.M)
                if len(fences) % 2:
                    errors.append(str(path.relative_to(ROOT)) + ": unbalanced code fence")
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                    if "://" in target or target.startswith(("#", "mailto:")):
                        continue
                    target = unquote(target.strip("<>").split("#")[0])
                    if target and not (path.parent / target).exists():
                        errors.append(str(path.relative_to(ROOT)) + ": missing local link " + target)
            elif suffix in (".sv", ".svh"):
                counts[suffix[1:]] += 1
                text = path.read_text(encoding="utf-8-sig")
                for name in re.findall(r'`include\s+"([^"]+)"', text):
                    if name != "uvm_macros.svh" and not (path.parent / name).is_file() and Path(name).name not in by_name:
                        errors.append(str(path.relative_to(ROOT)) + ": unresolved include " + name)
        except (SyntaxError, ValueError, UnicodeError) as exc:
            errors.append(str(path.relative_to(ROOT)) + ": " + str(exc))
    result = {"status": "PASS" if not errors else "FAIL", "scope": "syntax and document integrity only",
              "file_counts": counts, "errors": errors,
              "not_checked": ["SystemVerilog compilation", "UVM simulation", "commercial VIP", "LSF", "DUT behavior"]}
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

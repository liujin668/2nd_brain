"""One source for illustrative SV/C address constants; not actual SoC addresses."""
from pathlib import Path
import re
from flow_common import FlowError, read, write, integer


def generate(design, output):
    data = read(design)
    if data.get("schema_version") != 1 or data.get("die_count") != 1:
        raise FlowError("Generator supports schema 1 and one die")
    width = integer(data.get("address_width"), "address_width", 1, 64)
    regions = data.get("regions")
    if not isinstance(regions, list) or not regions:
        raise FlowError("regions must be nonempty")
    checked, names = [], set()
    for item in regions:
        name = item.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Z][A-Z0-9_]*", name) or name in names:
            raise FlowError("Region names must be unique uppercase identifiers")
        names.add(name)
        def parse(x):
            if type(x) is int:
                return x
            if isinstance(x, str):
                return int(x, 0)
            raise FlowError("Address/size must be integer or numeric string")
        base, size = parse(item["base"]), parse(item["size"])
        if base < 0 or size <= 0 or size >= 2**64 or base + size > 2**width:
            raise FlowError("Invalid region extent " + name)
        if any(base < x["base"] + x["size"] and x["base"] < base + size for x in checked):
            raise FlowError("Overlapping region " + name)
        checked.append(dict(name=name, base=base, size=size))
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    paths = [out / x for x in ("soc_generated_cfg_pkg.sv", "soc_generated_cfg.h", "resolved_design.json")]
    if any(x.exists() for x in paths):
        raise FlowError("Output exists; choose a new generated directory")
    sv = ["// Generated constants; not automatically connected to the DUT.",
          "package soc_generated_cfg_pkg;", "  localparam int SOC_ADDR_W = %d;" % width]
    c = ["/* Verify these constants against the real SoC map before use. */",
         "#ifndef SOC_GENERATED_CFG_H", "#define SOC_GENERATED_CFG_H", "#include <stdint.h>"]
    for r in checked:
        for field in ("base", "size"):
            name = r["name"] + "_" + field.upper()
            sv.append("  localparam logic [63:0] %s = 64'h%016x;" % (name, r[field]))
            c.append("#define %s UINT64_C(0x%x)" % (name, r[field]))
    paths[0].write_text("\n".join(sv + ["endpackage"]) + "\n", encoding="utf-8")
    paths[1].write_text("\n".join(c + ["#endif"]) + "\n", encoding="utf-8")
    write(paths[2], dict(data, regions=checked))
    return dict(status="GENERATED", output=str(out), scope=data.get("validation_scope"))

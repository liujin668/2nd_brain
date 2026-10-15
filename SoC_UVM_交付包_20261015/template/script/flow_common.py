"""Shared helpers. Python 3.8+, no third-party dependencies."""
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import threading
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
CANCEL = threading.Event()
RESERVED = ("+SOC_RUN_ID", "+SOC_RESULT_FILE", "+SOC_SEED", "+UVM_TESTNAME", "+SOC_PROFILE")


class FlowError(Exception):
    def __init__(self, message, status="CONFIG_ERROR"):
        super().__init__(message)
        self.status = status


def read(path):
    with Path(path).open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temp.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(str(temp), str(path))


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def unique(parent, prefix):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S")
    path = Path(parent) / (prefix + "-" + stamp + "-" + uuid.uuid4().hex[:12])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.mkdir(exist_ok=False)
    return path.resolve()


def integer(x, name, low=0, high=None):
    if type(x) is not int or x < low or (high is not None and x > high):
        raise FlowError("Invalid integer " + name)
    return x


def timeout(x):
    if type(x) not in (int, float) or not math.isfinite(x) or x <= 0:
        raise FlowError("timeout must be a positive finite number")
    return float(x)


def profile(name):
    data = read(ROOT / "config" / "profiles.json")
    if data.get("schema_version") != 1 or name not in data.get("profiles", {}):
        raise FlowError("Unknown profile " + name)
    p = data["profiles"][name]
    for field in ("min_checks_count", "min_stimulus_count"):
        integer(p[field], field, 1)
    if type(p.get("software_required")) is not bool:
        raise FlowError("Invalid software_required profile field")
    return p


def ready(p, scheduler="local"):
    if scheduler != "local":
        raise FlowError("LSF is TEMPLATE_ONLY; see lsf_adapter_template.py", "BLOCKED")
    if p["integration_status"] == "BLOCKED":
        raise FlowError(p.get("blocked_reason", "Profile not integrated"), "BLOCKED")



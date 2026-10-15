#!/usr/bin/env python3
"""Node-side worker. Does NOT submit jobs or claim LSF integration is complete."""
import argparse
import json
import sys
from flow_common import FlowError
from flow_engine import worker

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()
    try:
        result = worker(args.manifest)
        print(json.dumps(result, indent=2))
        # Preserve the raw test verdict; a negative selftest is still a failed
        # simulation. Only the controller may accept its exact expected IDs.
        sys.exit(0 if result["status"] == "PASS" else 1)
    except (FlowError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": getattr(exc, "status", "INFRA_ERROR"), "error": str(exc)}))
        sys.exit(2)

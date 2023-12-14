#!/usr/bin/python3

import sys
import json

from pathlib import Path

if (len(sys.argv) >= 2):
    file_obj = Path(sys.argv[1])
    if (file_obj.exists() and file_obj.suffix == ".json"):
        fatal_error = False
    else:
        fatal_error = True
else:
    fatal_error = True

if fatal_error:
    print("USAGE: {} SOME_FILE.json".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

data = json.loads(file_obj.read_text())

file_obj.write_text(
    json.dumps(data, indent=4)
)
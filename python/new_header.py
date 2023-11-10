#!/usr/bin/python3
"""NAIVE APPROACH FOR SCRIPT TO CREATE AN EMPTY BUT INCLUDE GUARDED C HEADER FILE"""

import sys

from pathlib import Path

error_message = ""

if (len(sys.argv) < 2):
    error_message = "USAGE: {} NEW_HEADER_NAME.h".format(sys.argv[0])
else:
    file_obj = Path(sys.argv[1])
    error_message = (
        "FILE '{}' ALREADY EXISTS".format(
            file_obj.name
        ) if file_obj.exists() else ""
    )

if (error_message):
    print(error_message, file=sys.stderr)
    exit(1)

boilerplace = "#ifndef NAME\n#define NAME\n\n#endif"

code = boilerplace.replace(
    "NAME",
    (file_obj.name).replace(
        ".", "_"
    ).upper()
)
file_obj.write_text(code)

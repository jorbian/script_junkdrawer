#!/usr/bin/python3

import re

from pathlib import Path

def get_function_names(file):
    """ATTEMPTS TO PULL THE NAMES OF FUNCTIONS FROM A '.c' OR '.h' FILE"""
    file_obj = Path(file)
    if ((not file_obj.exists) or (file_obj.suffix not in (".c", ".h"))):
        raise ValueError()

    function_pattern = re.compile(
        "^\s*[a-zA-Z_]\w*\s+([a-zA-Z_*]\w*\s*)\([^;]*\)",
        flags=re.M
    )
    function_names = [
        x.replace("*", "") for x in (re.findall(function_pattern, file_obj.read_text()))
    ]
    return (function_names)


if __name__ == "__main__":
    pass

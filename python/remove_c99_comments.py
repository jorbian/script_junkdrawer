#!/usr/bin/python3

from pathlib import Path

def remove_c99_comments(file):
    """REMOVES C99 STYLE COMMENTS FROM A '.c' OR '.h' FILE"""
    file_obj = Path(file)
    if ((not file_obj.exists) or (file_obj.suffix not in (".c", ".h"))):
        raise ValueError()

    code = file_obj.read_text()

    code = "\n".join(
        x for x in (
            x.split("//")[0] for x in code.split("\n")
        ) if x
    )
    file_obj.write_text(code)

remove_c99_comments(Path("test.c"))

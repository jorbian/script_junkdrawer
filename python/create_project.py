#!/usr/bin/python3

import sys

from pathlib import Path

DEFAULT_SUB_FOLDERS = ("css", "js")

def throw_error(message):
    """PRINT MESSAGE TO stderr AND GTFO="""
    print(message, file=sys.stderr)
    sys.exit(1)

if (len(sys.argv) < 2):
    throw_error(f'USAGE: {sys.argv[0]} $NEW_PROJECT_NAME')

project_folder_obj = Path(sys.argv[1])
if (project_folder_obj.exists()):
    throw_error(f'PROJECT FOLDER "{sys.argv[1]}" ALREADY EXISTS')
[
    Path(x).mkdir(parents=True, exist_ok=True)
        for x in (
            f'./{project_folder_obj}/{x}' for x in DEFAULT_SUB_FOLDERS
        )
]
[
    Path(f'./{x}/default.{x.name}').touch()
        for x in project_folder_obj.glob("*") if x.is_dir()
]
Path(f'./{project_folder_obj}/{sys.argv[1]}.html').touch()

print(f"NEW PROJECT '{sys.argv[1]}' SUCESSFULLY CREATED")

#!/usr/bin/python3

import json

from pathlib import Path

def create_new_file(file_obj):
    """CREATE NEW FILE AT THE SPECIFIED PATH"""
    if (not file_obj.exists()):
        file_obj.parent.mkdir(parents=True, exist_ok=True)
        file_obj.touch()

source_file = "structure.json"
source_file_obj = Path(source_file)
source_file_data = source_file_obj.read_text()

parsed_data = json.loads(source_file_data)

file_objs = (
    file for folder in {
        k: [Path(f'{k}/{p}') for p in v]
            for (k, v) in parsed_data.items()
    }.values() for file in folder
)

[create_new_file(file) for file in file_objs]
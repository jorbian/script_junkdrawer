#!/usr/bin/python3

import json

from pathlib import Path

def csv_row_to_json(*args, **kwargs):
    """CONVERT FIRST ENTRY MATCHING CERTIN PARAMETERS IN '.csv' TO JSON"""
    csv_file = Path(
        kwargs.get("input_file") or
        (args[0] if len(args) >= 1 else None) or
        "."
    )
    if ((not csv_file.exists()) or (csv_file.suffix != ".csv")):
        raise Exception()

    csv_data = (
        Path(csv_file).read_text()
    ).split("\n")

    csv_headers = csv_data[0].split(",")
    csv_data = [x.split(",") for x in csv_data[1:]]

    search_terms = kwargs.get("search_terms") or (lambda x: x == x)

    matches = [x for x in csv_data if search_terms(x)]
    if (not matches[0]):
        raise Exception()

    target_entry = dict(zip(csv_headers, matches[0]))

    output_file = (
        kwargs.get("output_file_gen") or
        (lambda x: "output.json")
    )(target_entry)

    Path(output_file).write_text(
        json.dumps(target_entry, indent=4)
    )

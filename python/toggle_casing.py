#!/usr/bin/python3

import re

from pathlib import Path


def to_snake_case(string):
    """CHANGE FROM PASCAL CASING TO SNAKE"""
    search_pattern = "[A-Z][^A-Z]*"

    words = [x for x in (re.findall(search_pattern, string)) if x]
    if (not words):
        raise Exception()
    
    return ("_".join(x.lower() for x in words))


def toggle_header_casing(file, transform=(lambda x: x)):
    file = Path(file)
    if (not file.exists()):
        raise Exception()

    table_data = (Path(file).read_text()).split("\n")

    table_headers = ",".join(transform(h) for h in
        (x for x in 
            table_data.pop(0).split(",")
        if x)
    )
    table_data.insert(0, table_headers)

    file.write_text(
        "\n".join(x for x in table_data if x)
    )

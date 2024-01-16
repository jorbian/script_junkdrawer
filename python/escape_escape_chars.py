#!/usr/bin/python3

import re
import sys

TARGET_CHARS = ("(",")","[","]",".","*","?","+","|","^", "$")

def escape_escape_chars(string):
    """ADD SLASHES NEXT TO CHARACTERS THAT NEED TO BE ESCAPED"""
    search_pattern = re.compile(
        "({})".format(
            "|".join(f"\\{x}" for x in TARGET_CHARS)
        )
    )
    return (
        re.sub(
            search_pattern,
            (lambda x: f'\\\\{x.group()}'),
            string
        )
    )

if __name__ == "__main__":

    if (len(sys.argv) < 2):
        print(
            "USAGE: {} STRING_TO_ESCAPE".format(sys.argv[0]),
            file=sys.stderr
        )
        exit(1)

    print(escape_escape_chars(sys.argv[1]))

#!/usr/bin/python3

from itertools import repeat

SUPPORTED_CHAR_PAIRS = {
    "parentheses": ('(', ')'),
    "brackets": ('[', ']'),
    "curly_braces": ('{', '}')
}

def create_nesting_pattern(chars=('(',')'), up_level=0):
    """GENERATES A REGEX PATTERN FOR NESTING PAIRS OF CHARS"""
    placeholders = ('A', 'B')
    basic_template = "\A(?:[^AB])*\B"
    add_level = "\A(?:(?:{})|(?:[^AB]))*\B"

    expression = basic_template

    for x in repeat(add_level, up_level):
        expression = x.format(expression)

    for char in zip(placeholders, chars):
        expression = expression.replace(*char)

    return (expression)

if __name__ == "__main__":

    import argparse

    class GetChars(argparse.Action):
        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            if nargs is not None:
                raise ValueError("nargs not allowed")
            super().__init__(option_strings, dest, **kwargs)
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, SUPPORTED_CHAR_PAIRS.get(values))

    parser = argparse.ArgumentParser()

    parser.add_argument('type', type=str,
        choices=tuple(SUPPORTED_CHAR_PAIRS.keys()),
        action=GetChars
    )
    parser.add_argument("--depth", type=int, default=1)

    x = parser.parse_args()

    print(create_nesting_pattern(x.type, x.depth))
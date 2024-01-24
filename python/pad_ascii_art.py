#!/usr/bin/python3

from pathlib import Path

def pad_ascii_art(infile, padding_char="+", margins=3):
    """ADD SPECIFIED PADDING TO A PIECE OF ASCII ART SAVED IN TEXT FILE"""
    infile = Path(infile)
    if (not infile.exists()):
        raise Exception

    file_content = (infile.read_text()).split("\n")

    target_line_len = (
        max(len(line) for line in file_content) + ((margins + 1) * 2)
    )
    format_string = (padding_char + " " * 3)
    format_string = "{}{}{}".format(
        format_string,
        "{}",
        format_string[::-1]
    )
    file_content = [format_string.format(x) for x in file_content]
    [
        file_content.insert(
            x(), (target_line_len * padding_char))
                for x in [
                    (lambda: 0), (lambda: len(file_content))
            ]
    ]
    file_content = "\n".join(file_content)

    outfile = Path(
        "{}{}{}".format(
            infile.stem,
            "PADDED",
            infile.suffix
        )
    )
    if (outfile.exists()):
        raise Exception

    outfile.write_text(file_content)

if __name__ == "__main__":
    """DEFAULTS TO INTERPRETING FILE AS SINGLE SCRIPT"""
    import argparse

    ARG_DEFS = {
        ("-f", "--file"): {
            "type": str,
            "required": True,
            "action": 'store'
        },
        ("-c", "--padding", "--char"): {
            "type": str,
            "required": False,
            "default": "*"
        },
        ("-m", "--margins"): {
            "type": int,
            "required": False,
            "default": 3
        },
    }

    parser = argparse.ArgumentParser()
    [
        parser.add_argument(*k, **v) for (k, v) in
            ARG_DEFS.items()
    ]
    [
        globals().update({k: v}) for (k, v) in
            vars(parser.parse_args()).items()
    ]
    pad_ascii_art(file, padding_char=padding, margins=margins)
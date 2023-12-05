#!/usr/bin/python3
#
# A quine is a type of program based on Willard Van Orman Quine's famous 
# paradox: "yields falsehood when preceded by its quotation" yields falsehood
# when preceded by its quotation. --
#
# The idea is for the program to produce its own source code as output. The 
# way that I do it here is technically cheating because it uses outside tools
# to loop up itself and copy what it finds into a new file but it was a great
# way to demonstrate use of a couple of my favourte tools in Python --

import random
import string

# Not even as a dev but as a user this object is something that makes Python
# something that can come in handy EVERY SINGLE DAY --
from pathlib import Path

# Again, as a user, nevermind as a dev, the Path object is my greatest
# workhorse. It allows you to creae and modify files pretty much at will --
# even at the binary level!! --
code = Path(__file__).read_text()

outfile_name = "z{}.py".format(
    ''.join(
        random.choices(
            (string.ascii_lowercase + string.digits),
            k=7
        )
    )
)
outfile_obj = Path(outfile_name)

outfile_obj.write_text(code)
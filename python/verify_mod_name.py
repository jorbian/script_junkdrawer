#!/usr/bin/python3

import sys

from pathlib import Path 

def verify_mod_name(mod_file):
    """ENSURES THAT A '.py' FILE NAME MATCHES CONVENTION"""
    mod_file = Path(mod_file)
    if (not mod_file.exists()):
        raise FileExistsError
    
    mod_name = (mod_file.stem)
    mod_obj = __import__(mod_name)

    func_name = {
        k: v for (k,v) in vars(mod_obj).items()
            if "__" not in k
    }.popitem()[0]

    if (func_name != mod_name):
       Path(mod_file).rename(f'{func_name}.py')

if (__name__ == "__main__"):
    """WHEN INVOKED DIRECTLY USES FILE NAME PROVIDED FROM TERMINAL"""
    if ((len(sys.argv) < 2) or Path(sys.argv[1]).suffix != ".py"):
        print(
            "USAGE: {} SOME_MOD.py".format(sys.argv[0]),
            file=sys.stderr
        )
        sys.exit(1)

    verify_mod_name(sys.argv[1])
#!/usr/bin/python3

from pathlib import Path

exe_file_sig = b'\x7fELF'

def do_thing_to_files(dir, macthes_criteria, do_thing):
    """PERFORM SOME ACTION ON ALL THE FILES IN A DIRECTORY MATCHING CRITERIA"""
    folder_obj = Path(dir)

    file_objs = (
        x for x in folder_obj.glob("*") if not x.is_dir()
    )
    for file in file_objs:
       if (macthes_criteria(file)):
           do_thing(file)

def delete_all_executables(dir):
    """DELETE ALL FILES MATCHING THE FILE SIGNATURE OF AN EXECUTABLE IN 'dir'"""
    def is_exectable(file):
        """DETERMINE IF FILE'S FILE SIGNATURE MATCHES ONE EXPECTED FOR EXEC"""
        return (
            file.read_bytes()[0:(len(exe_file_sig))] == exe_file_sig
        )
    def delete_file(file):
        """DOES EXACTLY WHAT IT SAYS ON THE TIN"""
        file.unlink()

    do_thing_to_files(dir, is_exectable, delete_file)

if __name__ == "__main__":
    """DEFAULTS TO CURRENT DIRETORY"""
    delete_all_executables(".")

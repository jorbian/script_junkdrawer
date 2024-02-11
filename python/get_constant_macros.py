#!/usr/bin/python3

import re

from pathlib import Path

class MacroConstant:

    CODE_TEMPLATE = "#define {} {}"
    SEARCH_PATTERN = re.compile(
        "^#\s?define\s(?P<name>[^0-9_][^\(\)\s]+)\s(?P<value>[^\(\)A-Z\s]+)$",
        re.MULTILINE
    )
    file = None
    all = []

    def __init__(self, **kwargs):

        for field, value in kwargs.items():
            setattr(self, field, value)

        self.adjust_value_type()

    def __str__(self):
        """USES THE ORIGINAL C CODE AS STRING REPRESENTATION OF OBJECT"""
        return (
            self.CODE_TEMPLATE.format(
                self.name, self.value
            )
        )
    
    def __repr__(self):
        """GENERATES STRING WHICH COULD BE USED TO RECREATE OBJECT"""
        return (
            "MacroConstant({})".format(
                ", ".join([f"'{x}'" for x in vars(self).values()])
            )
        )
    
    def define_as_variable(self):
        """DEFINES THE CONSTANT AS GLOBAL VARIABLE IN CURRENT PYTHON CONTEXT"""
        globals()[self.name] = self.value

    def adjust_value_type(self):
        """ADJUSTS TYPING OF self.value FOR CORRECT INTERPRETATION AS PYTHON CODE"""
        self.value = (int(self.value) if (self.value).isdigit() else self.value)

    @classmethod
    def find_all(cls, header, action):
        """FINDS ALL OF THE MACRO CONSTANTS DEFINED IN HEADER AND PERFORMS THE ACTION"""
        header = Path(header)
        if ((not header.exists()) or (header.suffix != ".h")):
            raise Exception

        header_code = header.read_text()

        macros = (
            MacroConstant(**x.groupdict())
                for x in re.finditer(
                    cls.SEARCH_PATTERN, header_code
                )
        )
        action(header, macros)

    @classmethod
    def define_all(cls, macro_list=None):
        """DEFINES AN LIST OF MacroConstant OBJECTS IN CURRENT PYTHON ENV"""
        if (macro_list is None):
            macro_list = cls.all

        [x.define_as_variable() for x in macro_list]

    @classmethod
    def load_header_file(cls, header, action=(lambda: True)):
        """LOADS CONSTANTS DEFINED IN HEADER AND DOES OR DOESNT DO A THING"""
        header = Path(header)
        if ((not header.exists()) or (header.suffix != ".h")):
            raise Exception

        def load_into_memory(header, macros):
            cls.file = header;
            cls.all = tuple(macros)
            action()

        cls.find_all(header, load_into_memory)

MacroConstant.load_header_file("elf.h",MacroConstant.define_all)

print(globals())
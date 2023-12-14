#!/usr/bin/python3

import csv

from pathlib import Path

class Currency:

    def __init__(self, **kwargs):
        self.iso_4217 = kwargs.get("iso_4217") or "XXX"
        self.numeric_code = kwargs.get("numeric_code") or 999
        self.decimal_places = kwargs.get("decimal_places") or 4
        self.name = kwargs.get("name") or "No currency"
        self.active_currency = False

    @property
    def iso_4217(self):
        return (self._iso_4217)
    
    @iso_4217.setter
    def iso_4217(self, iso_code):
        """MAKE SURE THAT THE VALUE BEING SET IS EXACTLY THREE LETTERS"""
        if (len(iso_code) != 3):
            raise Exception()
        self._iso_4217 = iso_code.upper()

    @property
    def numeric_code(self):
        """MAKES SURE ITS ALWAYS A STRING WITH LEN OF THREE"""
        return f"{self._numeric_code:0>3}"
    
    @numeric_code.setter
    def numeric_code(self, code):
        """MAKE SURE THAT NUMERIC CODE IS VALID THREE DIGIT NUMBER"""
        code = int(code)
        if ((code >= 1000) or (code < 1)):
            raise Exception()   
        self._numeric_code = code

    @property
    def decimal_places(self):
        """NUMBER OF DECIMAL PLACES USED ACCOUNTING IN CURRENCY"""
        return (self._decimal_places)
    
    @decimal_places.setter
    def decimal_places(self, d):
        "MAKES SURE THE VALUE IS 0, 1, 2, 3, or 4"
        d = int(d)
        if ((d > 4) or (d < 0)):
            raise Exception()
        self._decimal_places = d

    @property
    def name(self):
        return (self._name)
    
    @name.setter
    def name(self, name):
        self._name = name

    def create_table_row(self):
        """CREATES A ROW OF AN HTML TABLE"""
        return "<tr>{}</tr>".format(
            "".join(
                f"<td>{x}</td>" for x in (
                    list(vars(self).values())[:-1]
                )
            )
        )

    @classmethod
    def create_table(cls, currency_list):
        return "<table><tbody>{}</tbody></table>".format(
            "".join(cls.create_table_row(x) for x in currency_list)
        )

    @staticmethod
    def load_from_csv(source_file):
        """LOAD A LIST OF CURRENCIES FROM A CSV FILE"""
        source_file = Path(source_file)
        if (not source_file.exists()):
            return ([])
        
        first_line = (source_file.read_text().split("\n")[0]).split(",")
        property_names = [
            x[0] for x in vars(Currency).items() if isinstance(x[1], property)
        ]
        if (not first_line == property_names):
            return ([])

        with open(source_file, newline='') as csvfile:
            return list(
                Currency(**row) for row in csv.DictReader(csvfile)
            )
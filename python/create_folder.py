#!/usr/bin/python3

import json

from pathlib import Path

class Item:

    POSSIBLE_DATA_TYPES = (None)

    @classmethod
    def matches_possible_type(cls, item):
        """DETERMINES IF ITEM BEING SORTED MATCHES POSSIBLE DATATYPES"""
        return isinstance(
            item,
            cls.POSSIBLE_DATA_TYPES
        )

class File(Item):

    POSSIBLE_DATA_TYPES = (str)

class Folder(Item):

    POSSIBLE_DATA_TYPES = (
        dict, Path
    )

    @classmethod
    def unpack_folder_children(cls, info, parentpath="./"):
        """GENERATES THE FOLDER ITEM PATHS AS A LIST OF STRINGS"""
        item_paths = []

        for (key, value) in info.items():
            for item in value:
                if isinstance(item, dict):
                    child_items = cls.unpack_folder_children(
                        item,
                        f'{parentpath}/{key}'
                    )
                    item_paths = [*item_paths, *child_items]
                    continue
                item_paths.append(f'{parentpath}/{key}/{item}')

        return (path for path in item_paths)
    
    @classmethod
    def create_folder_child(cls, child):
        """CREATE THE CHILD ITEM BASED ON PATH"""
        child = Path(child)
        if (child.exists()):
            return

        (child.parent).mkdir(parents=True, exist_ok=True)

        child.write_text("")


test_file_name = "blockchain.json"
test_file_obj = Path(test_file_name)
test_file_data = json.loads(test_file_obj.read_text())

x = Folder.unpack_folder_children(test_file_data[0], f"./{test_file_obj.stem}")

[Folder.create_folder_child(a) for a in x]
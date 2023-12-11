#!/usr/bin/python3
"""
create an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """deserialize the json file"""
    with open(filename, 'w', encoding="utf-8") as file:
        object_file = json.load(file)

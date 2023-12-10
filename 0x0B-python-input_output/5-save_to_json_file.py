#!/usr/bin/python3
"""
a function that writes an Object to a text
file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """open a text file and serialize it"""
    with open(filename, 'w', encoding="utf-8") as file:
        my_obj = file.write()
    json_string = json.dumps(my_obj)
    return json_string

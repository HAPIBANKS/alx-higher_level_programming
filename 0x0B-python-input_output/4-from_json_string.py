#!/usr/bin/python3
"""
convert JSON to python object
"""


import json


def from_json_string(my_str):
    """deserialize to python object"""
    python_obj = json.load(my_str)
    return python_obj

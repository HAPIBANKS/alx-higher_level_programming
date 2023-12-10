#!/usr/bin/python3
"""
a function that returns the JSON representation
"""


import json
def to_json_string(my_obj):
    """serialize the python file into JSON"""
    json_string = json.dumps(my_obj)
    return json_string

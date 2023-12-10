#!/usr/bin/python3
"""
a function that returns the JSON representation
"""


def to_json_string(my_obj):
    """serialize the python file into JSON"""
    import json
    json_string = json.dumps(my_obj)
    print(json_string)

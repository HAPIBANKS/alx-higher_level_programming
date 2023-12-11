#!/usr/bin/python3
"""
A script that adds all arguments to a python file
and then save them to a file
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import json


try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file("add_item.json", items)

#!/usr/bin/python3
"""
Script to add command-line argument
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file("add_item.json", items)

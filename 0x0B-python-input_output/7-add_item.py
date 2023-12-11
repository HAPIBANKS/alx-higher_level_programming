#!/usr/bin/python3
"""
Script to add command-line arguments to a Python list and save them to a file.

This script reads the existing content from 'add_item.json' (if it exists) using
the 'load_from_json_file' function. It then adds the command-line arguments (excluding
the script name) to the list. The updated list is saved as a JSON representation in
the 'add_item.json' file using the 'save_to_json_file' function.

Usage:
    python script_name.py arg1 arg2 ...

Dependencies:
    - save_to_json_file function from 5-save_to_json_file.py
    - load_from_json_file function from 6-load_from_json_file.py

Note:
    If 'add_item.json' doesn't exist, it will be created, and the command-line
    arguments will be added to an empty list.

"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    # Load existing data from 'add_item.json' or initialize an empty list
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    # Create the file if it doesn't exist
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to 'add_item.json'
save_to_json_file("add_item.json", items)

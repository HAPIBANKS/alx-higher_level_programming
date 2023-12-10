#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """open the file and append"""
    with open(filename, 'a', encoding=utf-8) as file:
        append_file = file.append(text)
        return len(append_file)

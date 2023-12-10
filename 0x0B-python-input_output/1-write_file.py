#!/usr/bin/python3
"""
a function that writes a string toa text
file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write to a file and print the number of charac"""
    with open(filename, 'w', encoding="utf8") as f:
        file_written = f.write(text)
        return file_written

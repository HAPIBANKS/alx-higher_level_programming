#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encodind="utf-8") as file:
        file_content = file.read()
        print(file_content)

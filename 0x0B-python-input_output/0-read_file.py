#!/usr/bin/python3
"""
File input and ouput
"""



def read_file(filename=""):
    """
    Read a text file and print it to standard output
    """

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            
            file_content = file.read()
            print(file_content)
    
    except Exception as e:
        print(f"An error occurred: {e}")
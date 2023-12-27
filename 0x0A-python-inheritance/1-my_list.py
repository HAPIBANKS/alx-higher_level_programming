#!/usr/bin/python3
"""
MyList class inherits from list and provides a custom print_sorted method.
"""


class MyList(list):
    """the list sorted"""
    def print-sorted(self):
        self.sort()
        for element in self:
            print(element)

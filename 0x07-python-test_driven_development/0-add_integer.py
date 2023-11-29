#!/usr/bin/python3
"""
Addition of int a and b
if a or b is a float
it should be cast into an int
"""


def add_integer(a, b=98):
    """
    raise a TypeError if not an int or float
    if it's a float, cast into int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    add_result = a + b
    return add_result

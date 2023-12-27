#!/usr/bin/python3
"""
returns True if the object is exactly an
instance of the specified class;
otherwise False
"""


def is_same_class(obj, a_class):
    """check if object is an instance of the a given class"""
    return isinstance(type(obj), a_class)

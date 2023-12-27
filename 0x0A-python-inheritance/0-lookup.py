#!/usr/bin/python3
"""
Retruns the list of attribute and methods of an object
"""


def lookup(obj):
    """get the attribute"""
    attributes = []

    for key in dir(obj):
        value = getattr(obj, key)
        if callable(value):
            attributes.append(f"{key}()")
        else:
            attributes.append(key)

    return attributes

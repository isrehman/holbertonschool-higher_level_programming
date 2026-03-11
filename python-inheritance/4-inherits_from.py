#!/usr/bin/python3
"""Module that checks if object is instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited from a_class but is not a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

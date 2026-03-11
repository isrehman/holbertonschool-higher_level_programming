#!/usr/bin/python3
"""Module that inserts a line after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in content:
            f.write(line)
            if search_string in line:
                f.write(new_string)

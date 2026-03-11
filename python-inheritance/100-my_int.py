#!/usr/bin/python3
"""Module that defines MyInt class"""


class MyInt(int):
    """Rebel class that inverts == and != operators"""

    def __eq__(self, other):
        """Inverted == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted != operator"""
        return super().__eq__(other)

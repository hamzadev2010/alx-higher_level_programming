#!/usr/bin/python3
"""Specifies a class MyInt that inherits from int."""


class MyInt(int):
    """Override the int operators == and !=."""

    def __eq__(self, value):
        """Reimplement the int operators == and !=."""
        return self.real != value

    def __ne__(self, value):
        """Reimplement the != operator to behave
        like the == operator."""
        return self.real == value

# coding=UTF8

"""
Classes for error handling.
"""

class IepgError(Exception):
    def __init__(self, value, description):
        self.value = value
        self.description = description

    def __str__(self):
        return repr(self.value+': '+self.description)

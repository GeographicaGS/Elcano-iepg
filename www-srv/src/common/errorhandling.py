# coding=UTF8

"""
Exceptions
"""
from flask import jsonify
import const

class ElcanoApiRestError(Exception):
    status = 400
    
    def __init__(self, error, status=None, payload=None):
        """Exception initializer."""
        Exception.__init__(self)
        self.error = error
        if status:
            self.status = status
        self.payload = payload

    def toDict(self):
        """Error to dictionary."""
        rv = dict()
        rv["payload"] = self.payload or ()
        rv["error"] = self.error
        rv["status code"] = self.status
        return rv


class DataValidator():
    """Data validator."""
    def checkLang(self, lang):
        """Checks language."""
        if lang not in const.lang:
            raise ElcanoApiRestError("Not a language.", status=200, payload={"lang": lang})
        return None

    def checkNumber(self, n):
        """Checks for number."""
        if not str(n).isdigit():
            raise ElcanoApiRestError("Not a number.", status=200, payload={"Number": n})
        return None

    def checkIntList(self, n):
        """Checks that a list is composed exclusively by integers."""
        for i in n:
            self.checkNumber(i)
        return None

    def checkBoolean(self, n):
        """Checks if n is boolean."""
        if n==True:
            return None
        if n==False:
            return None
        raise ElcanoApiRestError("Not a boolean.", status=200, payload={"Boolean": n})

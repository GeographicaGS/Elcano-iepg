# coding=UTF8

"""

Model helpers, most of them parameter integrity checks.

Error codes:

-1: bad language
-2: not a number

"""

import cons

class ElcanoError(Exception):
    """Base class for errors."""
    def __init__(self, code, expr, msg):
        self.code = code
        self.expr = expr
        self.msg = msg

    def dict(self):
        return({"code": self.code, "expr": self.expr, "msg": self.msg})


def checkLang(lang):
    """Checks language."""
    if lang not in cons.lang:
        raise ElcanoError("-1", lang, "Bad language.")

    return None

    
def checkNumber(n):
    """Checks for number."""
    if not str(n).isdigit():
        raise ElcanoError("-2", str(n), "Not a number.")

    return None


def checkIntList(n):
    """Checks that a list is composed exclusively by integers."""
    for i in n:
        checkNumber(i)

    return None

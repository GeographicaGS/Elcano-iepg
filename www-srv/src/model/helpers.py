# coding=UTF8

"""

Model helpers, most of them parameter integrity checks.


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


class ElcanoErrorBadNewsSection(ElcanoError):
    """Bad news section error."""
    def __init__(self, expr):
        ElcanoError.__init__(self, -3, expr, "Bad news section.")


class ElcanoErrorBadLanguage(ElcanoError):
    """Bad language error."""
    def __init__(self, expr):
        ElcanoError.__init__(self, -1, expr, "Bad language.")


class ElcanoErrorNotANumber(ElcanoError):
    """Not a number error."""
    def __init__(self, expr):
        ElcanoError.__init__(self, -2, str(expr), "Not a number.")


class DataValidator():
    """Data validator."""
    def checkLang(self, lang):
        """Checks language."""
        if lang not in cons.lang:
            raise ElcanoErrorBadLanguage(lang)

        return None

    def checkNewsSection(self, section):
        """Checks if news section is valid."""
        if int(section) not in [1,2,3,4,5]:
            raise ElcanoErrorBadNewsSection(section)

        return None

    def checkNumber(self, n):
        """Checks for number."""
        if not str(n).isdigit():
            raise ElcanoErrorNotANumber(str(n))

        return None

    def checkIntList(self, n):
        """Checks that a list is composed exclusively by integers."""
        for i in n:
            checkNumber(i)

        return None
# coding=UTF8

"""

Block processing functions.

"""

def blockFunctionLumpSum(values):
    """Gets a list with values of a variable and returns the lump
    sum of the values. Returns an integer which is the lump sum."""
    s = 0
    for i in values.values():
        s+=i
    return(s)

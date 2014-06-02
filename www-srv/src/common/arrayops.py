# coding=UTF8

"""

Array operations.

"""

def arrayIntersection(array1, array2):
    """Returns the intersection of two arrays."""
    return([v for v in array1 if v in array2])


def arraySubstraction(array1, array2):
    """Returns array1 without members of array2."""
    return([v for v in array1 if v not in array2])

# coding=UTF8

"""

Array operations.

"""

def arrayIntersection(array1, array2):
    """Returns the intersection of two arrays. Objects must be hasheable. TODO: introduce hashes."""
    if array1 and array2:
        return([v for v in array1 if hash(v) in hash(array2)])
    if not array1 or not array2:
        return(None)

def arraySubstraction(array1, array2):
    """Returns array1 without members of array2. Objects must be hasheable."""
    if array1 and array2:
        return [v for v in array1 if hash(v) not in [hash(e) for e in array2]]
    if array1==[]:
        return([])
    if not array1:
        return(None)
    if not array2:
        return(array1)


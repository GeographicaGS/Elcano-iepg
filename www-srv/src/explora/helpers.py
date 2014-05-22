# coding=UTF8

"""

Explora helpers.

"""

def processFilter(request_args, filterName):
    """Gets request_args from a call and analyzes the filter, returns a list."""
    filter = None
    if filterName in request_args:
        filter=(None if request_args[filterName].split(",")[0]=="" else request_args[filterName].split(","))
    return filter

# coding=UTF8

"""

Explora helpers.

"""

def processFilter(requestArgs, filterName):
    """Gets request_args from a call and analyzes the filter, returns a list."""
    filter = None
    if filterName in requestArgs:
        filter = (None if requestArgs[filterName].split(",")[0]=="" else requestArgs[filterName].split(","))
    return filter


def processArgs(requestArgs, argName):
    """Process an argument from request.args."""
    arg = None
    if argName in requestArgs:
        arg = (None if requestArgs[argName]=="" else requestArgs[argName])
    return arg

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


def adjustBigUnits(value, format=0):
    """Formats a number in US or ES billions and millions without reaching
    a <0 number.

    format = 0 : US format
    format = 1 : ES format

    """
    units = ["US Billion", "Million", None] if format==0 else \
            ["ES Billion", "Million", None]
    trans = [value/1000000000.0, value/1000000.0, value] if format==0 else \
            [value/1000000000000.0, value/1000000.0, value]

    for i in range(0, 3):
        if trans[i]>=1.0:
            return (trans[i],units[i])


    

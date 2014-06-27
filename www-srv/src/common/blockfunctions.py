# coding=UTF8

"""

Block processing functions.

"""
# import common.helpers as helpers
# import common.datacache as datacache
import maplex.maplex as maplex

def blockFunctionLumpSum(data, context=None):
    """Gets a list with values of a variable and returns the lump
    sum of the values. Returns an integer which is the lump sum."""
    s = 0
    values = False
    for i in maplex.getBlockMembers(data["code"], year=data["year"], idNameFamily=1):
        v = context.getData(code=i["id_geoentity_child"], year=data["year"]).values()[0]["value"]
        if v is not None:
            values = True
            s += v
    if values:
        return(s)
    else:
        return(None)

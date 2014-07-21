# coding=UTF8

"""

Block processing functions.

"""
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


def blockFunctionRelativeContributions(data, context=None):
    """Calculates relative contributions for a block."""
    dataSetContext = context.dataSet.context
    family = context.dataSet.id.partition("_")[0]
    var = dataSetContext["dataSets"][family].variables[context.id]
    globalVar = dataSetContext["dataSets"][family].variables["global"]

    members = [i["id_geoentity_child"] for i in 
               maplex.getBlockMembers(data["code"], year=data["year"], idNameFamily=1)]
    members = [data["code"]] if members==[] else members
    
    varTotal = 0
    globalTotal = 0

    for i in members:
        varData = var.getData(code=i, year=data["year"]).values()[0]["value"]
        globalData = globalVar.getData(code=i, year=data["year"]).values()[0]["value"]
        varTotal = varTotal+varData if varData else varTotal
        globalTotal = globalTotal+globalData if globalData else globalTotal

    coeficient = dataSetContext["const"][family][var.id]["coeficient"]
    return(varTotal*coeficient/globalTotal*100)

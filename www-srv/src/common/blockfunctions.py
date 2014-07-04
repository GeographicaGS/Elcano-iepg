# coding=UTF8

"""

Block processing functions.

"""
import maplex.maplex as maplex
import const
import datacache

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
    print context
    family = context.dataSet.id.partition("_")[0]
    print family
    print 

    var = datacache.dataSets[family].variables[context.id]
    globalVar = datacache.dataSets[family].variables["global"]

    members = [i["id_geoentity_child"] for i in 
               maplex.getBlockMembers(data["code"], year=data["year"], idNameFamily=1)]

    print members
    
    varTotal = 0
    globalTotal = 0

    for i in members:
        varTotal += var.getData(code=i, year=data["year"]).values()[0]["value"]
        globalTotal += globalVar.getData(code=i, year=data["year"]).values()[0]["value"]

    print varTotal, globalTotal



    # print "IN: "+str(data)
    # print "Context: "+str(context.dataSet.id+" "+context.id)
    # print context.dataSet.variables
    # print


    # print "dataSets : "+str(datacache.dataSets)

    # # vGlobal = context.variables["

    # iepgIndividualContribution = datacache.dataSets["iepg_individual_contribution"].variables[context.id]

    # print
    # print "Individual : " + str(iepgIndividualContribution.getData(code="DE", year=2013))
    # print


    # print "Members: "+str(members)
    # print

    # varData = 0
    # for i in members:
    #     print i
    #     print context.getData(code=i, year=data["year"]).values()[0]["value"]
   #     varData += context.getData(code=i, year=data["year"]).values()[0]["value"]

    # print "varData: "+str(varData)

    return(-1)

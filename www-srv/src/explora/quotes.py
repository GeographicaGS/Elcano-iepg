# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,make_response
import common.helpers as chelpers
import common.datacache as datacache
import flux_lib.data.core as flux
from collections import OrderedDict
import numpy as np

@app.route('/quotesT/<string:family>/<string:variable>/<string:countries>/<string:lang>', methods=['GET'])
def quotesT(family,variable,countries,lang):
    """Quotes service. Call example:

    /quotes/iepg/global_global/US,DK,ES,NZ/es
    """
    family = family+"_quota"
    variable = variable+"_global" if variable=="global" else variable
    countriesArray = countries.split(",")

    # print "family: ", family
    # print "variable: ", variable
    # print "countriesArray: ", countriesArray

    out = []
    minData = None
    maxData = None



    try:
        years = datacache.dataSets[family].variables[variable].getVariableYears()
    except:
        return jsonify({"results": out})

    # print "years : ", years
    # print
    # print

    gva = flux.GeoVariableArray(geoentity=sorted(countriesArray), time=sorted([str(y) for y in years]))

    # print gva

    gvaInitData = []

    for i in range(len(years)):
        year = years[i]
        varData = chelpers.getData(datacache.dataSets[family].variables[variable], 
                                   year=year, countryList=countriesArray)

        # print "Data for ", year
        # print varData
        # print

        # Find min and max data
        data = OrderedDict(sorted(varData.items(), 
                                  key=lambda t: t[1]["code"]))
        data = [v["value"] for k,v in data.iteritems()]

        # print "Data "
        # print data
        # print

        gvaInitData.extend(data)


        # countryData = []
        # for data in varData.values():
        #     dataValue = {
        #         "country": data["code"],
        #         "value": data["value"]
        #     }
        #     countryData.append(dataValue)
        # yearData = {
        #     "year": year,
        #     "values": countryData
        # }
        # out.append(yearData)

    # print npA




    a = np.array(gvaInitData)
    # print "HHH : ", a.shape, gva.shape

    # print "kj : ", len(gvaInitData), a

    gva.addVariable("Data", data=a)


    # print "KJK : ", gva["XBSA","2013","Data"]

    # out = sorted(out, key=lambda t: t["year"])

    
    # print "Available data : "
    # print out
    # print
    # print

    print "Geoentity : ", gva.geoentity
    print "Time : ", [str(x) for x in gva.time]

    print gva[:,"2012","Data"]

    print np.nanmin(gva[:,"2012","Data"])
    print np.nanmax(gva[:,"2012","Data"])

    return jsonify({"results": out})




@app.route('/quotes/<string:family>/<string:variable>/<string:countries>/<string:lang>', methods=['GET'])
def quotes(family,variable,countries,lang):
    """Quotes service. Call example:

    /quotes/iepg/global_global/US,DK,ES,NZ/es
    """
    family = family+"_quota"
    variable = variable+"_global" if variable=="global" else variable
    countriesArray = countries.split(",")

    out = []    
    try:
        years = datacache.dataSets[family].variables[variable].getVariableYears()
    except:
        return(jsonify({"results": out}))

    for year in years:
        varData = chelpers.getData(datacache.dataSets[family].variables[variable], 
                                   year=year, countryList=countriesArray)
        countryData = []
        for data in varData.values():
            dataValue = {
                "country": data["code"],
                "value": data["value"]
            }
            countryData.append(dataValue)
        yearData = {
            "year": year,
            "values": countryData
        }
        out.append(yearData)

    out = sorted(out, key=lambda t: t["year"])
    return jsonify({"results": out})

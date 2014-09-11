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

    out = []
    minData = None
    maxData = None

    try:
        years = datacache.dataSets[family].variables[variable].getVariableYears()
    except:
        return jsonify({"results": out})

    gva = flux.GeoVariableArray(geoentity=sorted(countriesArray), time=sorted([str(y) for y in years]))
    gvaInitData = []

    for i in range(len(years)):
        year = years[i]
        varData = chelpers.getData(datacache.dataSets[family].variables[variable], 
                                   year=year, countryList=countriesArray)

        # Find min and max data
        data = OrderedDict(sorted(varData.items(), 
                                  key=lambda t: t[1]["code"]))
        data = [v["value"] for k,v in data.iteritems()]

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

    gvaInitData = [x if x is not None else np.nan for x in gvaInitData]
    a = np.swapaxes(np.array(gvaInitData).reshape((len(years), len(countriesArray))), 0, 1)
    gva.addVariable("Data", data=a)
    gva.addVariable("minYearValue")
    gva.addVariable("maxYearValue")
    
    for year in gva.time:
        print year
        print gva[:,year,"Data"]

        print np.nanmin(gva[:,year,"Data"])
        print np.nanmax(gva[:,year,"Data"])


        gva[:,year,"minYearValue"] = np.array([4,4,4,4,4,4,4,4,4,4])
        print gva[:,year,"minYearValue"]
        print

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

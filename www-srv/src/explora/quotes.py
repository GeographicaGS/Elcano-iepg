# coding=UTF8

"""

Explora country services.

"""
from explora import app
from flask import jsonify,request,make_response
import common.helpers as chelpers
import common.datacache as datacache

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
        print(years)
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

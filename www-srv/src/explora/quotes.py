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
from common.config import quotesClustersSeeds

@app.route('/quotes/<string:family>/<string:variable>/<string:countries>/<string:lang>', methods=['GET'])
def quotes(family,variable,countries,lang):
    """Quotes service. Call example:

    /quotes/iepg/global_global/US,DK,ES,NZ/es
    """
    family = family+"_quota"
    variable = variable+"_global" if variable=="global" else variable
    countriesArray = countries.split(",")

    try:
        years = datacache.dataSets[family].variables[variable].getVariableYears()
    except:
        return jsonify({"results": out})

    # Sorted lists of years and geoentities
    geoentities = sorted(countriesArray)
    times = sorted([str(y) for y in years])

    # Create a GeoVariableArray
    gva = flux.GeoVariableArray(geoentity=geoentities, time=times)
    gvaInitData = []

    # Prepare data for gva
    for i in range(len(years)):
        year = years[i]
        varData = chelpers.getData(datacache.dataSets[family].variables[variable], 
                                   year=year, countryList=countriesArray)
        data = OrderedDict(sorted(varData.items(), 
                                  key=lambda t: t[1]["code"]))
        data = [v["value"] for k,v in data.iteritems()]
        gvaInitData.extend(data)

    gvaInitData = [x if x is not None else np.nan for x in gvaInitData]
    a = np.swapaxes(np.array(gvaInitData).reshape((len(times), len(geoentities))), 0, 1)
    gva.addVariable("Data", data=a)
    clusters = gva.cluster("Data", quotesClustersSeeds)
    
    # Creating nodes dictionary
    points = []
    for y in range(len(clusters[0])):
        for c in range(len(clusters[0][y])):
            point = dict()
            point["codes"] = [geoentities[x] for x in clusters[0][y][c]]
            point["year"] = times[y]
            point["value"] = clusters[1][y][c]
            points.append(point)

    # Creating segments
    segments = []
    segmentCodes = []
    for c in geoentities:
        pointSequence = []
        for y in times:
            for p in range(len(points)):
                if c in points[p]["codes"] and points[p]["year"]==y:
                    pointSequence.append(p)

        for s in range(len(pointSequence)-1):
            segments.append([pointSequence[s], pointSequence[s+1]])
            segmentCodes.append([c])

    # Erase repeated segments
    i = 0
    while i<len(segments):
        t = i+1
        while t<len(segments):
            if segments[i]==segments[t]:
                segments.pop(t)
                code = segmentCodes.pop(t)
                segmentCodes[i].append(code[0])
            else:
                t+=1
        i+=1

    # Composing output
    out = dict()
    out["points"] = points
    out["segments"] = []

    for i in range(len(segments)):
        seg = dict()
        seg["points"] = segments[i]
        seg["codes"] = segmentCodes[i]
        out["segments"].append(seg)

    return jsonify({"results": out})

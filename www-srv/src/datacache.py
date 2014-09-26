# coding=UTF8

"""

Data cache.

"""

import varengine.varengine as varengine
import common.const as const
import redis
import pythonhelpers.database.datacache as datacache
import maplex.maplex as maplex
import copy
import common.arrayops as arrayops
import common.config as config
import sys

connclient = redis.StrictRedis(host="localhost", port=6379, db=0)
mc = datacache.RedisDataCache(connclient, prefix="iepg_", timeout=None)

if mc.get("IEPG data loaded")==1:
    print "Data already loaded in Redis."
    sys.exit()

def createCache():
    dataSets = dict()
    dataInterface = varengine.DataInterfacePostgreSql()
    tables = {
        "iepg": "iepg_data",
        "iepe": "iepe_data",
        "context": "pob_pib",
        "iepe_individual_contribution": "iepe_individual_contribution",
        "iepe_quota": "iepe_quota",
        "iepe_relative_contribution": "iepe_relative_contribution",
        "iepg_individual_contribution": "iepg_individual_contribution",
        "iepg_quota": "iepg_quota",
        "iepg_relative_contribution": "iepg_relative_contribution"
    }

    years = {
        "iepg": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013],
        "iepe": [2005, 2010, 2011, 2012, 2013],
        "context": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013],
        "iepe_individual_contribution": [2005, 2010, 2011, 2012, 2013],
        "iepe_quota": [2005, 2010, 2011, 2012, 2013],
        "iepe_relative_contribution": [2005, 2010, 2011, 2012, 2013],
        "iepg_individual_contribution": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013],
        "iepg_quota": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013],
        "iepg_relative_contribution": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]
    }

    blockFunctions = {
        "iepg": {
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
        },
        "context": {
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM", "XBEU"],
            "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
        },
        "iepg_quota": {
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
        },
        "iepg_relative_contribution": {
            "variables": ["energy", "primary_goods", "manufactures", "services", "investments",
                          "troops", "military_equipment", "migrations", "tourism", "sports", "culture",
                          "information", "technology", "science", "education", "cooperation"],
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionRelativeContributions"
        }
    }

    for fam in const.variableNames.keys():
        dataSets[fam] = varengine.DataSet(fam)
        dataSets[fam].context["dataSets"] = dataSets

        mapping = dict()
        dataInterface.readAll("iepg_data_redux."+tables[fam], 
                              "code", "date_in", "date_out")
        for k,var in const.variableNames[fam].iteritems():
            v = varengine.Variable(k, True, "float", dataSet=dataSets[fam])
            v.loadFromDataInterface(dataInterface, var["column"]) 
            if fam in blockFunctions:
                d = blockFunctions[fam]
                for y in years[fam]:
                    for b in d["blocks"]:
                        if "variables" in d:
                            if k in d["variables"]:
                                v.addValue(b, y, d["function"], None)
                        else:
                            v.addValue(b, y, d["function"], None)

    for dsKey, dataSet in dataSets.iteritems():
        dataSet.addToContext("const", const.variableNames)
        for varKey, variable in dataSet.variables.iteritems():
            variable.processData()
        dataSet.dropContext()

    for y in const.years:
        ds = dataSets["iepg_relative_contribution"]
        for b in ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"]:
            for c, dim in const.dimensions.iteritems():
                data = 0
                for var in dim:
                    v = ds.variables[var].getData(code=b, year=y)[str(b)+"@"+str(y)]["value"]
                    data = v+data if v else data
                ds.variables[c].addValue(b, y, "float", data)
    
    for dsKey in dataSets:
        mc.set(dsKey, dataSets[dsKey], 0)
    return(dataSets)

    
dataSets = createCache()

blocks = [maplex.getGeoentityNames(i["id_geoentity_block"], 1)[0]["names"][0] for i in maplex.getBlocks()]
blocksNoEu = copy.deepcopy(blocks)
blocksNoEu.remove("XBEU")
countriesAndEu = dataSets["iepg"].variables["energy"].getVariableCodes()
countriesAndEu = arrayops.arraySubstraction(countriesAndEu, blocks)
countriesAndEu.append("XBEU")
countries = copy.deepcopy(countriesAndEu)
countries.remove("XBEU")
blocksAndCountries = copy.deepcopy(countries)
blocksAndCountries.extend(blocks)

isoToSpanish, spanishToIso = maplex.getTranslationTable(1, idNameFamilyB=3)
isoToSpanish = {key: value for key,value in isoToSpanish.iteritems() if key in blocksAndCountries}
spanishToIso = {key: value for key,value in spanishToIso.iteritems() if value in blocksAndCountries}

isoToEnglish, englishToIso = maplex.getTranslationTable(1, idNameFamilyB=2)
isoToEnglish = {key: value for key,value in isoToEnglish.iteritems() if key in blocksAndCountries}
englishToIso = {key: value for key,value in englishToIso.iteritems() if value in blocksAndCountries}

isoToGeoentity, geoentityToIso = maplex.getTranslationTable(1)
isoToGeoentity = {key: value for key,value in isoToGeoentity.iteritems() if key in blocksAndCountries}
geoentityToIso = {key: value for key,value in geoentityToIso.iteritems() if value in blocksAndCountries}

mc.set("blocks", blocks, 0)
mc.set("blocksNoEu", blocksNoEu, 0)
mc.set("countriesAndEu", countriesAndEu, 0)
mc.set("countries", countries, 0)
mc.set("blocksAndCountries", blocksAndCountries, 0)
mc.set("isoToSpanish", isoToSpanish, 0)
mc.set("spanishToIso", spanishToIso, 0)
mc.set("isoToEnglish", isoToEnglish, 0)
mc.set("englishToIso", englishToIso, 0)
mc.set("isoToGeoentity", isoToGeoentity, 0)
mc.set("geoentityToIso", geoentityToIso, 0)

mc.set("IEPG data loaded", 1)
print "Cache done."

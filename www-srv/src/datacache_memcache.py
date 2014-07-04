# coding=UTF8

"""

Data cache.

"""

import varengine.varengine as varengine
import common.const as const
import memcache
import maplex.maplex as maplex
import copy
import common.arrayops as arrayops
import common.config as config

mc = memcache.Client([config.MemcachedConfig["host"]+":"+config.MemcachedConfig["port"]], debug=0)

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
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
        },
        "iepg_quota": {
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
        },
        "iepg_relative_contribution": {
            "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
            "function": "blockfunc::common.blockfunctions.blockFunctionRelativeContributions"
        }
    }

    for fam in const.variableNames.keys():
        dataSets[fam] = varengine.DataSet(fam)
        mapping = dict()
        dataInterface.readAll("iepg_data_redux."+tables[fam], 
                              "code", "date_in", "date_out")
        for k,var in const.variableNames[fam].iteritems():
            v = varengine.Variable(k, True, "float", dataSet=dataSets[fam])
            v.loadFromDataInterface(dataInterface, var["column"]) 
            if fam in blockFunctions:
                for y in years[fam]:
                    for b in blockFunctions[fam]["blocks"]:
                        v.addValue(b, y, blockFunctions[fam]["function"], None)
            v.processData()

        mc.set(fam, dataSets[fam], 0)

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

print "Cache done."

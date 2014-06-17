# coding=UTF8

"""

Data cache.

"""

import varengine.varengine as varengine
import const
import memcache
import maplex.maplex as maplex
import copy
import arrayops
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

    for fam in const.variableNames.keys():
        dataSets[fam] = varengine.DataSet(fam)
        mapping = dict()
        dataInterface.readAll("iepg_data_redux."+tables[fam], 
                              "code", "date_in", "date_out")
        for k,var in const.variableNames[fam].iteritems():
            v = varengine.Variable(k, True, "float", dataSet=dataSets[fam])
            mapping[k]=var["column"]
            dataSets[fam].loadVariableDataFromDataInterface(dataInterface, mapping=mapping)

        mc.set(fam, dataSets[fam], 0)

    return(dataSets)

dataSets = createCache()

for ds in dataSets.values():
    for v in ds.variables.values():
        for y in [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]:
            for b in ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"]:
                v.addValue(b, y, "blockfunc::common.blockfunctions.blockFunctionLumpSum", None)
        v.setupCache(varengine.DataCacheNumpy)
        v.cacheData()

blocks = [maplex.getGeoentityNames(i["id_geoentity_block"], 1)[0]["names"][0] for i in maplex.getBlocks()]
blocksNoEu = copy.deepcopy(blocks)
blocksNoEu.remove("XBEU")
countriesAndUe = dataSets["iepg"].variables["energy"].getVariableCodes()

for b in blocks:
    countriesAndUe.remove(b)
countriesAndUe.append("XBEU")
countries = copy.deepcopy(countriesAndUe)
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
mc.set("countriesAndUe", countriesAndUe, 0)
mc.set("countries", countries, 0)
mc.set("blocksAndCountries", blocksAndCountries, 0)
mc.set("isoToSpanish", isoToSpanish, 0)
mc.set("spanishToIso", spanishToIso, 0)
mc.set("isoToEnglish", isoToEnglish, 0)
mc.set("englishToIso", englishToIso, 0)
mc.set("isoToGeoentity", isoToGeoentity, 0)
mc.set("geoentityToIso", geoentityToIso, 0)

print "Cache done."

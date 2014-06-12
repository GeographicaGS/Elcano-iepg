# coding=UTF8

"""

Data cache.

"""

import varengine.varengine as varengine
reload(varengine)
import const
reload(const)
import common.cachewrapper as cachewrapper
import maplex.maplex as maplex
import copy
import arrayops


def createCache():
    dataSets = dict()
    dataInterface = varengine.DataInterfacePostgreSql()
    tables = {
        "iepg": "iepg_data" #,
        # "iepe": "iepe_data" #,
        # "context": "pob_pib",
        # "iepe_individual_contribution": "iepe_individual_contribution",
        # "iepe_quota": "iepe_quota",
        # "iepe_relative_contribution": "iepe_relative_contribution",
        # "iepg_individual_contribution": "iepg_individual_contribution" #,
        # "iepg_quota": "iepg_quota",
        # "iepg_relative_contribution": "iepg_relative_contribution"
    }

    for fam in ["iepg"]: # , "iepe"]: #, "iepe_individual_contribution", "context", 
                # "iepg_individual_contribution"]: # const.variableNames.keys():
        dataSets[fam] = varengine.DataSet(fam)
        mapping = dict()
        dataInterface.readAll("iepg_data_redux."+tables[fam], 
                              "code", "date_in", "date_out")
        for k,var in const.variableNames[fam].iteritems():
            v = varengine.Variable(k, True, "float", dataSet=dataSets[fam])
            mapping[k]=var["column"]
            dataSets[fam].loadVariableDataFromDataInterface(dataInterface, mapping=mapping)

    return(dataSets)

dataSets = cachewrapper.cacheWrapper(createCache)

for ds in dataSets.values():
    for v in ds.variables.values():
        for y in [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]:
            for b in ["XBAP", "XBSA"]:
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

isoToSpanish, spanishToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1, idNameFamilyB=3)
isoToSpanish = {key: value for key,value in isoToSpanish.iteritems() if key in blocksAndCountries}
spanishToIso = {key: value for key,value in spanishToIso.iteritems() if value in blocksAndCountries}

isoToEnglish, englishToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1, idNameFamilyB=2)
isoToEnglish = {key: value for key,value in isoToEnglish.iteritems() if key in blocksAndCountries}
englishToIso = {key: value for key,value in englishToIso.iteritems() if value in blocksAndCountries}

isoToGeoentity, geoentityToIso = cachewrapper.cacheWrapper(maplex.getTranslationTable, 1)
isoToGeoentity = {key: value for key,value in isoToGeoentity.iteritems() if key in blocksAndCountries}
geoentityToIso = {key: value for key,value in geoentityToIso.iteritems() if value in blocksAndCountries}

print "Cache done."

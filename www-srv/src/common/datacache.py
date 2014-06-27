# coding=UTF8

"""

Data cache.

"""

import common.cachewrapper as cachewrapper
import const

dataSets = dict()
for fam in const.variableNames.keys():
    dataSets[fam] = cachewrapper.getM(fam)

blocks = cachewrapper.getM("blocks")
blocksNoEu = cachewrapper.getM("blocksNoEu")
countriesAndEu = cachewrapper.getM("countriesAndEu")
countries = cachewrapper.getM("countries")
blocksAndCountries = cachewrapper.getM("blocksAndCountries")
isoToSpanish = cachewrapper.getM("isoToSpanish")
spanishToIso = cachewrapper.getM("spanishToIso")
isoToEnglish = cachewrapper.getM("isoToEnglish")
englishToIso = cachewrapper.getM("englishToIso")
isoToGeoentity = cachewrapper.getM("isoToGeoentity")
geoentityToIso = cachewrapper.getM("geoentityToIso")

print "Cache done."

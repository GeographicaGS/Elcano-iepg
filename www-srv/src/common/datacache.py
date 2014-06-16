# coding=UTF8

"""

Data cache.

"""

import common.cachewrapper as cachewrapper

dataSets = cachewrapper.getM("dataSets")
blocks = cachewrapper.getM("blocks")
blocksNoEu = cachewrapper.getM("blocksNoEu")
countriesAndUe = cachewrapper.getM("countriesAndUe")
countries = cachewrapper.getM("countries")
blocksAndCountries = cachewrapper.getM("blocksAndCountries")
isoToSpanish = cachewrapper.getM("isoToSpanish")
spanishToIso = cachewrapper.getM("spanishToIso")
isoToEnglish = cachewrapper.getM("isoToEnglish")
englishToIso = cachewrapper.getM("englishToIso")
isoToGeoentity = cachewrapper.getM("isoToGeoentity")
geoentityToIso = cachewrapper.getM("geoentityToIso")

print "Cache done."

# coding=UTF8

"""

Data cache.

"""

from pythonhelpers.database.datacache import RedisDataCache
import redis
import const
from common.config import RedisConfig

connclient = redis.StrictRedis(host=RedisConfig["host"], port=RedisConfig["port"], db=0)
mc = RedisDataCache(connclient, prefix="iepg_", timeout=None)

dataSets = dict()
for fam in const.variableNames.keys():
    # dataSets[fam] = cachewrapper.getM(fam)
    dataSets[fam] = mc.get(fam)

blocks = mc.get("blocks")
blocksNoEu = mc.get("blocksNoEu")
countriesAndEu = mc.get("countriesAndEu")
countries = mc.get("countries")
blocksAndCountries = mc.get("blocksAndCountries")
isoToSpanish = mc.get("isoToSpanish")
spanishToIso = mc.get("spanishToIso")
isoToEnglish = mc.get("isoToEnglish")
englishToIso = mc.get("englishToIso")
isoToGeoentity = mc.get("isoToGeoentity")
geoentityToIso = mc.get("geoentityToIso")


print "Cache done."

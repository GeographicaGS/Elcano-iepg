import common.helpers as h
reload(h)
import varengine.varengine as e
reload(e)
import maplex.maplex as m
reload(m)
import maplex.maplexmodel
reload(maplex.maplexmodel)
import varengine.varenginemodel
reload(varengine.varenginemodel)
import common.const
reload(common.const)
# import common.datacache as dc
# reload(dc)
import common.config as config
reload(config)

ds = e.Dataset('iepg')
ds.loadFromDatabase()
print ds.variables
v = ds.variables["information"]
v.cacheData()

print m.getTranslationTable(1, idNameFamilyB=3)


# print v.getData()
# print
# print v.getData(code="SK")
# print
# print v.getData(year=1990)
# print
# print v.getData(code="US", year=1990)

# print(v.getData())
# print(v.getData(code="US", year=2013))
# print(v.getVariableYears())
# print(v.getVariableCodes())

# years = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]
# for i in years:
#     print v.getData(code="SK", year=i)
#     print v.getYearData(i)

# print v.getData(year=2013)
# print
# print h.getRanking(v.getVariableCodes(), 1990, v)
# print
# print h.getRankingCode(v.getVariableCodes(), 2013, v, "GB")

# print h.getData(v)
# print
# print h.getData(v, code="US")
# print
# print h.getData(v, year=2013)
# print
# print h.getData(v, code="US", year=2013)
# print
# print h.getData(v, code="XBEU")
# print
# print h.getData(v, code="XBEU", year=2013)
# print
# print h.getData(v, code="XBAP")
# print
# print h.getData(v, code="XBAP", year=2013)
# print




# print h.getBlockMembers("XBAP")

# coding=UTF8

# This module reads 

import data.excel_utils as excel_utils, numpy as np, data.core as core
reload(core)
reload(excel_utils)

book = excel_utils.ExcelReader("Prototipo hoja de datos.xlsx")

print book.sheets
print 

print book.cellReader("Metadata",0,0)
print

print book.rowReader("Metadata", markColumn=0, startMark="Environmental Variables", 
                     endMark="Filiation")
print

a = book.readGeoVariableArray("IEPG.Economic.Energy", dataType=np.int32)
print 

b = core.GeoVariableArray(["US","ES","EN","NL"],["1990","2000"])



# Reading core.GeoVariableArray from a Geoentity/Time formated sheet
# aGeo = book.readGeoVariableArray("Test 0", dataType=np.uint64)
# bGeo = book.readGeoVariableArray("Test 1", dataType=np.uint64, geoentitiesOrientation=excel_utils.ORIENTATION_COLS)
# bGeo.addVariable("TEST", np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))

# aGeo.merge(bGeo)


# # book.rowReader
# print "Rows"
# print 0, book.rowReader("Test 2")
# print
# print 1, book.rowReader("Test 2", startCell=(1,1))
# print
# print 2, book.rowReader("Test 2", startCell=(1,1), dimensions=(2,2))
# print
# print 3, book.rowReader("Test 2", markColumn=4, startMark="Variable Type")
# print
# print 4, book.rowReader("Test 2", startMark="LANGUAGE_CODES", endMark="LANGUAGE_CODES")
# print 
# print 5, book.rowReader("Test 2", startMark="Environmental Variables", endMark="")
# print 











# TEST ZONE

# a = core.GeoVariableArray(["US", "ES"], ["2011","2010"])

# a.addVariable("V0", np.array([1,2,3,4]))
# a.addVariable("V1", np.array([5,6,7,8]))
# a.addVariable(["V2","V3"], [np.array([9,10,11,12]),np.array([[13,14],[15,16]])])

# a.addTime("2013")
# a.addGeoentity("DE")

# print a.shape



# print "Columns"
# a = book.columnReader("test")
# print a
# print
# print 1, book.columnReader("test", startColumn=19)
# print
# print 2, book.columnReader("test", startMark="7")
# print
# print 3, book.columnReader("test", startMark="3", endMark="6")
# print
# print 4, book.columnReader("test", startMark="3", endMark="3")
# print 
# print 5, book.columnReader("test", endMark="8")
# print
# print 6, book.columnReader("test", startColumn=8, startMark=1, endMark=6)
# print


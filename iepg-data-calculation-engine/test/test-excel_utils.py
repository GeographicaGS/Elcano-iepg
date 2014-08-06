# coding=UTF8

# This module reads 

import data.excel_utils as excel_utils, numpy as np, data.core as core
reload(core)
reload(excel_utils)

book = excel_utils.ExcelReader("test/test-excel_utils.xlsx")



a = book.readGeoVariableArray("Test 0", dataType=np.uint64)

b = book.readGeoVariableArray("Test 1", dataType=np.uint64, geoentitiesOrientation=excel_utils.ORIENTATION_COLS)

a.merge(b)












# print "Rows"
# print 0, book.rowReader("test")
# print
# print 1, book.rowReader("test", startRow=19)
# print
# print 2, book.rowReader("test", startMark="7")
# print
# print 3, book.rowReader("test", startMark="3", endMark="6")
# print
# print 4, book.rowReader("test", startMark="3", endMark="3")
# print 
# print 5, book.rowReader("test", endMark="8")
# print
# print 6, book.rowReader("test", startRow=8, startMark=1, endMark=6)
# print

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

# coding=UTF8

# This module reads 

import excel_utils
reload(excel_utils)

book = excel_utils.ExcelReader("test-excel_utils.xlsx")

print 0, book.rowReader("test")
print
print 1, book.rowReader("test", startRow=19)
print
print 2, book.rowReader("test", startMark="7")
print
print 3, book.rowReader("test", startMark="3", endMark="6")
print
print 4, book.rowReader("test", startMark="3", endMark="3")
print 
print 5, book.rowReader("test", endMark="8")
print
print 6, book.rowReader("test", startRow=8, startMark=1, endMark=6)
print


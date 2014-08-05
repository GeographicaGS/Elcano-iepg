# coding=UTF8

import xlrd, datetime, core, numpy as np

class ExcelReader(object):
    """Reads Excel files."""
    _book = None
    
    def __init__(self, filePath):
        """Opens the file."""
        self._book = xlrd.open_workbook(filePath)

    @property
    def sheets(self):
        """Sheets in workbook."""
        return(self._book.sheet_names())

    def cellReader(self, sheetName, row, col):
        """Reads a single cell."""
        sheet = self._book.sheet_by_name(sheetName)
        return(sheet.cell(row, col))

    def rowReader(self, sheetName, startRow=None, endRow=None, startCol=None, 
                  endCol=None, markColumn=None, startMark=None, endMark=None):
        """Reads all rows from start to end, given as strings. Keep in mind
        that rows starts internally at 0, while in the sheet
        representation the start at 1. Substract one from the desired
        row. Reading do not include the last row.

        """
        sheet = self._book.sheet_by_name(sheetName)
        startRow = startRow if startRow else 0
        endRow = endRow if endRow else sheet.nrows
        startCol = startCol if startCol else 0
        endCol = endCol if endCol else sheet.ncols
        markColumn = markColumn if markColumn else 0
        read = False if (startMark or startMark=="") else True
        out = []
        r = None

        for r in range(startRow, endRow):
            cell = sheet.cell(r, markColumn)
            if (startMark=="" or startMark) and cell.value==self.castType(cell, startMark):
                read = True
            if read:
                row = []
                for c in range(startCol, endCol):
                    row.append(sheet.cell(r, c))
                out.append(row)
            if (endMark=="" or endMark) and cell.value==self.castType(cell, endMark):
                out.pop(len(out)-1)
                break
    
        return((out, r if r else None))

    def columnReader(self, sheetName, startRow=None, endRow=None, startCol=None, 
                     endCol=None, markRow=None, startMark=None, endMark=None):
        """TODO: mimic behaviour between this and rowReader."""
        sheet = self._book.sheet_by_name(sheetName)
        startRow = startRow if startRow else 0
        endRow = endRow if endRow else sheet.nrows
        startCol = startCol if startCol else 0
        endCol = endCol if endCol else sheet.ncols
        markRow = markRow if markRow else 0
        read = False if (startMark or startMark=="") else True
        out = []
        r = None

        for c in range(startCol, endCol):
            cell = sheet.cell(markRow, c)
            if (startMark=="" or startMark) and cell.value==self.castType(cell, startMark):
                read = True
            if read:
                column = []
                for r in range(startRow, endRow):
                    column.append(sheet.cell(r, c))
                out.append(column)
            if (endMark=="" or endMark) and cell.value==self.castType(cell, endMark):
                out.pop(len(out)-1)
                break
    
        return((out, c if c else None))
            
    def castType(self, cell, value):
        """Casts a Python value to the cell type."""
        if cell.ctype==xlrd.XL_CELL_EMPTY:
            return(unicode(value))
        if cell.ctype==xlrd.XL_CELL_NUMBER:
            return(float(value))
        if cell.ctype==xlrd.XL_CELL_TEXT:
            return(str(value))
        if cell.ctype==xlrd.XL_CELL_DATE:
            dt = xlrd.xldate_as_tuple(cell.value, 0)
            return(datetime.datetime(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
        if cell.ctype==xlrd.XL_CELL_BOOLEAN:
            return(True if cell.value==1 else False)

    def unifyType(self, cell, pyType):
        """TODO: This has to be done taking into account Numpy arrays types.
        TODO: Mirror with the function above and clearly define
        functionality.

        """
        print cell, pyType

        if cell.ctype==xlrd.XL_CELL_EMPTY and pyType==core.DATA_TYPE_INT:
            return(np.nan)
        if cell.ctype==xlrd.XL_CELL_NUMBER and pyType==core.DATA_TYPE_INT:
            return(int(cell.value))


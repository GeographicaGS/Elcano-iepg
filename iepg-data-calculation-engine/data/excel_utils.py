# coding=UTF8

import xlrd, datetime, core, numpy as np
reload(core)


OUTPUT_NDARRAY = 0
OUTPUT_PYTYPES = 1
OUTPUT_CELLS = 2
OUTPUT_RECORDS = 3

ORIENTATION_ROWS = 0
ORIENTATION_COLS = 1

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

    def rowReader(self, sheetName, startRow=0, endRow=None, startCol=0, 
                  endCol=None, markColumn=None, startMark=None, endMark=None,
                  lineal=False, numpyArray=True, dataType=None):
        """TODO: review this method, make it stronger. Subdivide in several
        others. Make startMark and endMark more flexible, based on
        lambda functions that examine the row or column readed and
        decide if continue or stop the reading.

        

        Reads all rows from start to end, given as strings. Keep in
        mind that rows starts internally at 0, while in the sheet
        representation the start at 1. Substract one from the desired
        row. Reading do not include the last row.

        - **sheetName:** Excel sheet to read from;
        - **startRow:** row to start reading from. Defaults to 0;
        - **endRow:** row to end reading. By default, reads to the last row of the sheet;
        - **startCol:** column to start reading from. Defaults to 0;
        - **endCol:** column to end reading. By default, reads to the last column of the sheet;
        - **markColumn:** column to look for start and end marks. Defaults to startCol;
        - **startMark:** start mark to begin reading;
        - **endMark:** end mark to stop reading;
        - **lineal:** if True, returns a lineal array, if False, an array organized first in rows and then in columns;
        - **numpyArray:** if True, returns a bidimensional numpy.ndarray. If False, returns Excel cell objects. TODO: check relation between lineal and numpyArray, for it is possible to output an unidimensional Numpy array;
        - **dataType:** a Numpy or Python data type to cast data to. If Numpy

        TODO: aside from returning cell objects, implement an option
        to return fully casted Python types for each cell in an
        heterogeneous way. Also to return dictionary, record like
        structures given a field name header.

        """
        sheet = self._book.sheet_by_name(sheetName)
        endRow = endRow if endRow else sheet.nrows
        startCol = startCol if startCol else 0
        endCol = endCol if endCol else sheet.ncols
        markColumn = markColumn if markColumn else startCol
        if numpy:
            lineal=True
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
                    if lineal:
                        out.append(sheet.cell(r,c))
                    else:
                        row.append(sheet.cell(r, c))
                if not lineal:
                    out.append(row)
            if (endMark=="" or endMark) and cell.value==self.castType(cell, endMark):
                out.pop(len(out)-1)
                break
    
        if numpy:
            pass
        else:
            return((out, r if r else None))

    def columnReader(self, sheetName, startRow=0, endRow=None, startCol=0, 
                     endCol=None, markRow=None, startMark=None, endMark=None,
                     lineal=False, numpyArray=True, dataType=None):
        """TODO: mimic behaviour between this and rowReader."""
        sheet = self._book.sheet_by_name(sheetName)
        endRow = endRow if endRow else sheet.nrows
        endCol = endCol if endCol else sheet.ncols
        markRow = markRow if markRow else startRow
        if numpyArray:
            lineal=True
            dataType = dataType if dataType else np.float_
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
                    cell = sheet.cell(r,c)
                    data = self.cast(cell.value, cell.ctype, dataType) \
                           if numpyArray else cell
                    if lineal:
                        out.append(data)
                    else:
                        column.append(data)
                if not lineal:
                    out.append(column)
            if (endMark=="" or endMark) and cell.value==self.cast(cell, endMark):
                out.pop(len(out)-1)
                break

        if numpyArray:
            out = np.resize(np.array(out), (endRow-startRow, endCol-startCol))
            return out
        else:
            return((out, c if c else None))

    def readCube(self, sheets, startCell=(0,0), dimensions=None, output=OUTPUT_NDARRAY, dataType=None,
                 orientation=ORIENTATION_ROWS, startLambda=None, endLambda=None):
        """TODO: extract a multidimensional Numpy array from a series of
        identical sheets starting in a cell for a certain dimension."""
        for sheet in sheets:
            sheet = self._book.sheet_by_name(sheet)
            print sheet
            
        


    def readGeoVariableArray(self, sheetName, startCell=(0,0), dimensions=None, 
                             geoentitiesOrientation=ORIENTATION_ROWS, dataType=np.float_):
        """Returns a GeoVariableArray given the square of a sheet and taking
        the geoentities either from top of columns or first column,
        depending on the geoentities parameter. The other orientation
        is for time. Geoentities identifiers are treated as strings.

        - **sheetName:** sheet to read from;
        - **startCell:** start cell to read from. Defaults to (0,0);
        - **dimensions:** dimensions to read. Defaults to the full extent of the sheet;
        - **geoentitiesOrientation:** tells if geoentities are row or column oriented. By default, they are searched in rows;
        - **dataType:** data type to convert to. It is a Numpy data type. Defaults to np.float_
        
        """
        sheet = self._book.sheet_by_name(sheetName)
        dimensions = dimensions if dimensions else (sheet.nrows, sheet.ncols)

        rows = []
        for r in range(startCell[0], startCell[0]+dimensions[0]):
            col = []
            for c in range(startCell[1], startCell[1]+dimensions[1]):
                col.append(sheet.cell(r,c))
            rows.append(col)

        if geoentitiesOrientation==ORIENTATION_ROWS:
            geoentities = [self.__cast(x[0].value, x[0].ctype, str) for x in rows][1:]
            time = [core.Time(self.__cast(x.value, x.ctype, str)) for x in rows[0][1:]]
        else:
            geoentities = [self.__cast(x.value, x.ctype, str) for x in rows[0][1:]]
            time = [core.Time(self.__cast(x[0].value, x[0].ctype, str)) for x in rows][1:]

        data = []
        for a in rows[1:]:
            data.extend(a[1:])

        data = np.array([self.__cast(x.value, x.ctype, dataType) for x in data])
        geovar = core.GeoVariableArray(geoentities, time)
        geovar.addVariable(sheetName, data)
        
        return(geovar)
            
    def __cast(self, value, typeA, typeB):
        """Casts a type to a type. Types can be either Excel cell types,
        Python base types or Numpy types.

        """
        if typeA==0:
            if typeB==np.float64 or typeB==np.int32 or typeB==np.uint64:
                return(np.nan)
            if typeB==str:
                return(None)
        if typeA==1:
            if typeB==str:
                return(str(value))
        if typeA==2:
            if typeB==np.float64:
                return(np.float64(value))
            if typeB==np.int32:
                return(np.int32(value))
            if typeB==np.uint64:
                return(np.uint64(value))
            if typeB==str:
                return(str(value))
        if typeA==str:
            if typeB==np.int32:
                return(np.int32(value))
        if typeA==int:
            if typeB==np.float64:
                return(np.float64(value))

        raise EquidnaExcelException("Unhandled type conversion: value %s (%s) from %s to %s" \
                                    % (value, type(value), typeA, typeB))



class EquidnaExcelException(Exception):
    """Exception for Equidna Excel interface."""
    _message = ""

    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return("EquidnaExcelException: "+self._message)

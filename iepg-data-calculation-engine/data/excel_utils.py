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
    """This class reads Reads Excel XSLX files. The constructor gets the path to the XSLX file."""
    _book = None
    
    def __init__(self, filePath):
        """Opens the file."""
        self._book = xlrd.open_workbook(filePath)

    @property
    def sheets(self):
        """Sheets in the XLSX book."""
        return(self._book.sheet_names())

    def cellReader(self, sheetName, row, col):
        """Reads a single cell, given the sheet name, row, and col."""
        sheet = self._book.sheet_by_name(sheetName)
        return(sheet.cell(row, col))

    def rowReader(self, sheetName, startCell=(0,0), dimensions=None,
                  markColumn=None, startMark=None, endMark=None):
        """Returns a set of Excel rows and the last row readed:

        - *sheetName:* sheet name;
        - *startCell:* cell to start reading from. Defaults to (0,0);
        - *dimensions:* tuple (for example (2,2)), dimensions to read from the start cell. Defaults to the whole sheet extend;
        - *markColumn:* column to check for start and end marks;
        - *startMark:* start mark;
        - *endMark:* end mark.

        """
        sheet = self._book.sheet_by_name(sheetName)
        dimensions = dimensions if dimensions else (sheet.nrows-startCell[0],sheet.ncols-startCell[1])
        markColumn = markColumn if markColumn else startCell[1]
        read = False if (startMark or startMark=="") else True
        out = []

        for r in range(startCell[0], startCell[0]+dimensions[0]):
            cell = sheet.cell(r, markColumn)
            if (startMark or startMark=="") and cell.value==self.__cast(startMark, cell.ctype, str):
                read = True
            if read:
                out.append([sheet.cell(r,c) for c in range(startCell[1], startCell[1]+dimensions[1])])
            if (endMark or endMark=="") and cell.value==self.__cast(endMark, cell.ctype, str):
                break

        return out, r if r else None

    # def columnReader(self, sheetName, startRow=0, endRow=None, startCol=0, 
    #                  endCol=None, markRow=None, startMark=None, endMark=None,
    #                  lineal=False, numpyArray=True, dataType=None):
    #     """TODO: mimic behaviour between this and rowReader."""
    #     sheet = self._book.sheet_by_name(sheetName)
    #     endRow = endRow if endRow else sheet.nrows
    #     endCol = endCol if endCol else sheet.ncols
    #     markRow = markRow if markRow else startRow
    #     if numpyArray:
    #         lineal=True
    #         dataType = dataType if dataType else np.float_
    #     read = False if (startMark or startMark=="") else True
    #     out = []
    #     r = None

    #     for c in range(startCol, endCol):
    #         cell = sheet.cell(markRow, c)
    #         if (startMark=="" or startMark) and cell.value==self.castType(cell, startMark):
    #             read = True
    #         if read:
    #             column = []
    #             for r in range(startRow, endRow):
    #                 cell = sheet.cell(r,c)
    #                 data = self.cast(cell.value, cell.ctype, dataType) \
    #                        if numpyArray else cell
    #                 if lineal:
    #                     out.append(data)
    #                 else:
    #                     column.append(data)
    #             if not lineal:
    #                 out.append(column)
    #         if (endMark=="" or endMark) and cell.value==self.cast(cell, endMark):
    #             out.pop(len(out)-1)
    #             break

    #     if numpyArray:
    #         out = np.resize(np.array(out), (endRow-startRow, endCol-startCol))
    #         return out
    #     else:
    #         return((out, c if c else None))

    def readCube(self, sheets, startCell=(0,0), dimensions=None, output=OUTPUT_NDARRAY, dataType=None,
                 orientation=ORIENTATION_ROWS, startLambda=None, endLambda=None):
        """TODO: extract a multidimensional Numpy array from a series of
        identical sheets starting in a cell for a certain dimension."""
        for sheet in sheets:
            sheet = self._book.sheet_by_name(sheet)
            print sheet

    def readGeoVariableArray(self, sheetName, startCell=(0,0), dimensions=None, 
                             geoentitiesOrientation=ORIENTATION_ROWS, dataType=np.float):
        """Returns a GeoVariableArray given the square of a sheet and taking
        the geoentities either from top of columns or first column,
        depending on the geoentities parameter. The other orientation
        is for time. Geoentities identifiers are treated as strings.

        - **sheetName:** sheet to read from;
        - **startCell:** start cell to read from. Defaults to (0,0);
        - **dimensions:** dimensions to read. Defaults to the full extent of the sheet;
        - **geoentitiesOrientation:** tells if geoentities are row or column oriented. By default, they are searched in rows;
        - **dataType:** data type to convert to. It is a Numpy data type. Defaults to np.float.
        

        TODO: column-oriented sheets reading are inefficient. Check,
        read in columns instead of rows.

        """
        sheet = self._book.sheet_by_name(sheetName)
        dimensions = dimensions if dimensions else (sheet.nrows, sheet.ncols)

        rows = []
        for r in range(startCell[0], startCell[0]+dimensions[0]):
            col = []
            for c in range(startCell[1], startCell[1]+dimensions[1]):
                col.append(sheet.cell(r,c))
            rows.append(col)

        data = []
        if geoentitiesOrientation==ORIENTATION_ROWS:
            geoentities = [self.__cast(x[0].value, x[0].ctype, str) for x in rows][1:]
            time = [core.Time(self.__cast(x.value, x.ctype, str)) for x in rows[0][1:]]

            for a in rows[1:]:
                data.extend(a[1:])
        else:
            geoentities = [self.__cast(x.value, x.ctype, str) for x in rows[0][1:]]
            time = [core.Time(self.__cast(x[0].value, x[0].ctype, str)) for x in rows][1:]

            for a in range(0,len(rows[0])-1):
                for b in rows[1:]:
                    data.append(b[a+1])

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
                return("")
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

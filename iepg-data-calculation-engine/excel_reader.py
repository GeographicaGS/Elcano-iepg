# coding=UTF8

# This module reads IEPG data from Excel
# ASSUMPTIONS: Data are ordered by code and years are also ordered

import data.excel_utils as excel_utils, data.core as core, ast, numpy as np
reload(excel_utils)
reload(core)

book = excel_utils.ExcelReader("Prototipo hoja de datos.xlsx", decimalSeparator=",")

environment = dict()
variables = dict()
years = []
geoentities = []

# Read metadata
environmentEx,lastRowEnv = book.rowReader("Metadata", startCell=(1,0), endMark="")
variablesEx,lastRowVar = book.rowReader("Metadata", startCell=(lastRowEnv+1,0), startMark="Filiation")

environmentEx.pop(len(environmentEx)-1)
variablesEx.pop(0)


print environmentEx, lastRowEnv
print
print variablesEx, lastRowVar
print

# Read configuration variables
for i in environmentEx:
    environment[i[0].value] = ast.literal_eval(i[1].value)

data = core.GeoVariableArray()

# Read variables
# for i in variablesEx:
#     var = core.Variable(i[0].value, 
#                         getattr(core, i[4].value),
#                         getattr(np, i[5].value), 
#                         environment["LANGUAGE_CODES"], 
#                         ast.literal_eval(i[1].value) if i[1].value!="" else None,
#                         ast.literal_eval(i[2].value) if i[2].value!="" else None,
#                         ast.literal_eval(i[3].value) if i[3].value!="" else None,
#                         ast.literal_eval(i[6].value) if i[6].value!="" else None)

# print var
# print

a = book.readGeoVariableArray("IEPG.Economic.Energy", dataType=np.int32)
b = book.readGeoVariableArray("IEPG.Economic.EnergyEst", dataType=np.int32)

# data.merge(a)
# data.merge(b)

# print "Reads:"
# a = book.readGeoVariableArray(".".join(var.filiation), dataType=var.dataType)

# data.merge(a)

#     data,last = book.rowReader(str(i[0].value), startRow=0, endRow=1)
#     years.extend([int(x.value) for x in data[0][1:]])

#     data,last = book.columnReader(str(i[0].value), startRow=1, startCol=0, endCol=1)
#     geoentities.extend([x.value for x in data[0]])
#     variables[i[0].value] = var

# geoentities = sorted(list(set(geoentities)))
# years = [core.Time(x,7,1) for x in sorted(list(set(years)))]

# dataArray = core.GeoVariableArray(geoentities, years)




# TEST ZONE



# data,b = book.rowReader("IEPG.Economic.Energy", startRow=1, startCol=1, lineal=True)

# linealData = []
# for r in data:
#     for c in r:
#         linealData.append(book.unifyType(c, core.DATA_TYPE_INT))



# ndarray = np.array(linealData)
# ndarray.resize((70, 8))

# Usage examples for VarEngine

# Example 00

d = e.Dataset("iepg")
v0 = d.createVariable("manufactures", True, "float")
v1 = d.createVariable("energy", True, "float")

d.registerInDatabase()
for i in d.variables.values():
    i.registerInDatabase()
    i.createVariableTable()
    i.populateFromTable("iepg_data_redux.iepg_data", "date_in", "date_out", "code", i.idVariable)

# Example 01

d = e.Dataset("iepg")
d.loadFromDatabase()

print d.variables

print d.variables["energy"].getVariableYears()
print d.variables["energy"].getVariableCodes()

c = e.DataCache(d.variables["energy"])
c2 = e.DataCache(d.variables["manufactures"])
print c.getData("GB", 1990)
print c2.getData("GB", 1990)

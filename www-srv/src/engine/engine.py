# coding=UTF8

"""

Variable engine.

TODO: variables should be coded with a date_in/date_out time lapse and a code. 
This code is expressed in whatever code stored as a name family in Maplex, and this family
must be stored in variable metadata. Internally, only id_geoentity must be used. Create 
functions for translation between different codes. Treat codes as arrays, for there can be
in a family more than one name for the same geoentity.

Combine Maplex and Engine?

TODO: Create a class in Elcano to store long lasting dictionaries and translation tables coming from the 
database to retrieve them easily

"""
import common.timelapse as timelapse
import enginemodel


def getVariableCodes(idFamily, idVariable, year=None):
    """Returns available codes for variable idVariable."""
    m = enginemodel.EngineModel()
    variable = getVariable(idFamily, idVariable)
    return([i["code"] for i in m.getVariableCodes(variable["var_table"], year)] if variable else None)


def getVariable(idFamily, idVariable):
    """Returns variable with ID idVariable."""
    m = enginemodel.EngineModel()
    return(m.getVariable(idFamily, idVariable))


def getVariables(family=None):
    m = enginemodel.EngineModel()
    return(m.getVariables(family))


def getVariableYears(idFamily, idVariable):
    """Returns years present in a variable. TODO: make it generic."""
    m = enginemodel.EngineModel()
    return([int(i["year"]) for i in m.getVariableYears(getVariable(idFamily, idVariable)["var_table"])])


def getIdFamilyByName(name):
    """Returns the variable family ID by it's english name."""
    m = enginemodel.EngineModel()
    return(m.getIdFamilyByName(name)[0]["id_family"])


def getVariableValue(idFamily, idVariable, code, year):
    """Returns the value of a variable."""
    m = enginemodel.EngineModel()
    var = getVariable(idFamily, idVariable)
    d = m.getVariableValue(var["var_table"], var["var_column"], code, year)
    return(d["data"] if d else None)

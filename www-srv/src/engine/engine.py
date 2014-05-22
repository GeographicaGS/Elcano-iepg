# coding=UTF8

"""

Variable engine.

TODO: variables should be coded with a date_in/date_out time lapse and a code. 
This code is expressed in whatever code stored as a name family in Maplex, and this family
must be stored in variable metadata. Internally, only id_geoentity must be used. Create 
functions for translation between different codes. Treat codes as arrays, for there can be
in a family more than one name for the same geoentity.

Combine Maplex and Engine?

"""
import common.timelapse as timelapse
import enginemodel


def getVariableCodes(idVariable, year=None):
    """Returns available codes for variable idVariable."""
    m = enginemodel.EngineModel()
    variable = getVariable(idVariable)
    return(m.getVariableCodes(variable["var_table"], year))


def getVariable(idVariable):
    """Returns variable with ID idVariable."""
    m = enginemodel.EngineModel()
    return(m.getVariable(idVariable))


def getVariables():
    m = enginemodel.EngineModel()
    return(m.getVariables())


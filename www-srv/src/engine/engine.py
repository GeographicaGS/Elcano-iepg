# coding=UTF8

"""

Variable engine.

"""
import common.timelapse as timelapse
import enginemodel


def getVariableCodes(idVariable):
    """Returns available codes for variable idVariable."""
    m = enginemodel.EngineModel()
    variable = m.getVariable(idVariable)
    return(m.getVariableCodes(variable["var_table"]))


def getVariable(idVariable):
    """Returns variable with ID idVariable."""
    m = enginemodel.EngineModel()
    return(m.getVariable(idVariable))


def getVariables():
    m = enginemodel.EngineModel()
    return(m.getVariables())


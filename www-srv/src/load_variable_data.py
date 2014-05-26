# coding=UTF8

"""

Variable data loader.

"""

import common.const as const
reload(const)
import varengine.varengine as varengine
reload(varengine)


d = varengine.Dataset("iepg")
d.registerInDatabase()
for k,v in const.variablesIepg.iteritems():
    var = d.createVariable(k, True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepg_data", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepe")
d.registerInDatabase()
for k,v in const.variablesIepe.iteritems():
    var = d.createVariable(k, True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepe_data", "date_in", "date_out", "code", k)

d = varengine.Dataset("context")
d.registerInDatabase()
var = d.createVariable("population", True, "float")
var.registerInDatabase()
var.createVariableTable()
var.populateFromTable("iepg_data_redux.pob_pib", "date_in", "date_out", "code", "population")
var = d.createVariable("gdp", True, "float")
var.registerInDatabase()
var.createVariableTable()
var.populateFromTable("iepg_data_redux.pob_pib", "date_in", "date_out", "code", "pib")

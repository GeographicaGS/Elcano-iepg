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
for k,v in const.variableNames["iepg"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepg_data", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepe")
d.registerInDatabase()
for k,v in const.variableNames["iepe"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepe_data", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepe_individual_contribution")
d.registerInDatabase()
for k,v in const.variableNames["iepe_individual_contribution"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepe_individual_contribution", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepe_quota")
d.registerInDatabase()
for k,v in const.variableNames["iepe_quota"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepe_quota", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepe_relative_contribution")
d.registerInDatabase()
for k,v in const.variableNames["iepe_relative_contribution"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepe_relative_contribution", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepg_individual_contribution")
d.registerInDatabase()
for k,v in const.variableNames["iepg_individual_contribution"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepg_individual_contribution", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepg_quota")
d.registerInDatabase()
for k,v in const.variableNames["iepg_quota"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepg_quota", "date_in", "date_out", "code", k)

d = varengine.Dataset("iepg_relative_contribution")
d.registerInDatabase()
for k,v in const.variableNames["iepg_relative_contribution"].iteritems():
    var = d.createVariable(v["key"], True, "float")
    var.registerInDatabase()
    var.createVariableTable()
    var.populateFromTable("iepg_data_redux.iepg_relative_contribution", "date_in", "date_out", "code", k)


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

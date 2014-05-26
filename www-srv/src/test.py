import common.helpers as h
reload(h)
import varengine.varengine as e
reload(e)
import maplex.maplex as m
reload(m)
import varengine.varenginemodel
reload(varengine.varenginemodel)
import common.const
reload(common.const)
import common.datacache as dc
reload(dc)




#print h.getVariableValue('iepg', 'energy', 'XBEU', 2013)

# print h.getRanking(["AT", "US", "ES", "XBEU", "XBAP"], 2013, 'iepg', 'energy')

#print e.getVariableCodes('iepg', 'energy')

# print h.getVariableValuesSeries(['IE', 'ES'], 2013, 'iepg', 'energy')



# print d.createVariableFromTable("energy", True, "iepg_data_redux.iepg_data", "date_in", "date_out", 
#                                 "code", "energy", "float")


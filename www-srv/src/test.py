import common.helpers as h
reload(h)
import engine.engine as e
reload(e)
import maplex.maplex as m
reload(m)
import engine.enginemodel
reload(engine.enginemodel)
import common.const
reload(common.const)

#print h.getVariableValue('iepg', 'energy', 'XBEU', 2013)

print h.getRanking(["AT", "US", "ES", "XBEU", "XBAP"], 2013, 'iepg', 'energy')

#print e.getVariableCodes('iepg', 'energy')

# print h.getVariableValuesSeries(['IE', 'ES'], 2013, 'iepg', 'energy')

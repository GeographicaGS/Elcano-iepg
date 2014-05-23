import common.helpers as h
reload(h)
import engine.engine as e
reload(e)
import maplex.maplex as m
reload(m)
import engine.enginemodel
reload(engine.enginemodel)

print h.getVariableValue('iepg', 'energy', 'XBEU', 2013)

import common.helpers as helpers
import common.const
import engine.engine as engine
reload(common.const)
reload(helpers)
reload(engine)


print(helpers.getIepgCountries())
print
print(helpers.getIepeCountries())
print
print(engine.getVariable(1))
print
print(engine.getVariables())

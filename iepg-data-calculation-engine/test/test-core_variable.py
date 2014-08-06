# coding=UTF8

import data.core as core, numpy as np
reload(core)

# Arises exception
# v0 = core.Variable("")

v0 = core.Variable("a.b.c", dataType=np.int_)

print "Filiation: ", v0.filiation
print "Variable type: ", v0.varType
print "Data type: ", v0.dataType
print "Languages: ", v0.languages
print "Names: ", v0.names
print "Descriptions: ", v0.descriptions
print "Units: ", v0.units
print "Traits: ", v0.traits
print "Str: ", str(v0)
print "Hash: ", hash(v0)

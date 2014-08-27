# coding=UTF8

import data.core as c
import numpy as np
reload(c)

# First dimension: Countries
# Second: Time intervals
# Third: Variables                                


x = c.GeoVariableArray(["ES","DE"], [c.Time("2013"), 
                                     c.Time("2014")])


print x.shape
print
x.addGeoentity(["US","US","US","NL"])
x.addTime([c.Time("2012"),c.Time("2011")])


y = np.array([0,0,0,0,1,1,1,1,10,10,10,10,100,100,100,100]).reshape(4,4)
x.addVariable(["V0","V1","V2"], [y,y+1,y+2])


print x.data
print

print "00 : ", x[0,0,2]
print
print "01 : ", x[0:1, 0:2, 1:3]
print
print "02 : ", x[(0,1), 1, (0,2)]
print
print "03 : ", x["DE", 0, "V0"]
print
print "04 : ", x[("DE", "ES"), 1, ("V0", "V2")]
print
print "05 : ", x[("ES"), lambda x: x/c.Time("2011-7-1"), ("V2")]
print
print "06 : ", x[("US", "NL"), "2011-7-1", ("V0", "V2")]
print
print "07 : ", x["DE", c.Time("2011-7-1"), "V2"]
print

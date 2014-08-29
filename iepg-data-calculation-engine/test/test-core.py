# coding=UTF8

import data.core as c
import numpy as np
reload(c)

a = c.GeoVariableArray(geoentity=["ES","EN","US"], time=["2011","2012","2013"], variable=["V0","V1","V2"],
                       data=[0.000,0.100,0.200, \
                             0.010,0.110,0.210, \
                             0.020,0.120,0.220, \
                             0.001,0.101,0.201, \
                             0.011,0.111,0.211, \
                             0.021,0.121,0.221, \
                             0.002,0.102,0.202, \
                             0.012,0.112,0.212, \
                             0.022,0.122,0.222])
print a.shape

print a()
print 

print a[0,0,0]
print
print a[("US","ES"),("2013","2011"),("V2","V0")]
print

# # print '000 : x[:,:,:]'
# # print x[:,:,:]
# # print
# # print '010 : x[0,0,2]'
# # print x[0,0,2]
# # print
# # print '020 : x[0:1, 0:2, 1:3]'
# # print x[0:1, 0:2, 1:3]
# # print
# # print '030 : x[(0,1), 1, (0,2)]'
# # print x[(0,1), 1, (0,2)]
# # print
# # print '040 : x["DE", 0, "V0"]'
# # print x["DE", 0, "V0"]
# # print
# # print '050 : x[("DE", "ES"), 1, ("V0", "V2")]'
# # print x[("DE", "ES"), 1, ("V0", "V2")]
# # print
# # print '055 : x[:,"2012-7-1",:]'
# # print x[:,"2012-7-1",:]
# # print
# # print '060 : x[("ES"), lambda x: x/c.Time("2011-7-1"), ("V2")]'
# # print x[("ES"), lambda x: x/c.Time("2012-7-1"), ("V2")]
# # print
# # print '070 : x[("US", "ES"), "2011-7-1", ("V0", "V2")]'
# # print x[("US", "ES"), "2011-7-1", ("V0", "V2")]
# # print
# # print '080 : x["DE", c.Time("2011-7-1"), "V2"]'
# # print x["DE", c.Time("2011-7-1"), "V2"]
# # print

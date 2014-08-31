# coding=UTF8

import data.excel_utils as eu, data.core as c, numpy as np, datetime as dt
reload(eu)

w = eu.ExcelWriter("/home/malkab/Desktop/test"+str(dt.datetime.now())+".xlsx")
a = c.GeoVariableArray(geoentity=["US","ES"], time=["2011","2012"], variable=["V0","V1"], 
                       data=np.array([.000,.001,0.010,0.011,0.100,0.101,0.110,0.111]))

w.writeGeoVariableArray(a)


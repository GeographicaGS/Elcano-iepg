# coding=UTF8

# --------------------------------
# Equidna Data Engine Core Classes
# --------------------------------

import numpy as np
from datetime import datetime

x = np.empty((2,2), dtype=[('x', np.int32), ('y', np.int32)])
y = np.empty((2,2))

# , ('y', np.int32), ('t', np.int32)])

# x[:,:,0] = np.random.rand(2,2)


class GeoVariableArray(object):
    """Data array for Equidna."""
    data = None
    __geoentity = None
    __time = None
    __variable = None

    def __init__(self, geoentity, time):
        """Initializator. Gets a list of geoentities and times to initialize the data array."""
        self.__geoentity = geoentity
        self.__time = time
        self.__variable = []
        self.data = np.empty((len(self.__geoentity), len(self.__time), 1))
        # self.data = np.linspace(0, 100, num=len(self.__geoentity)*len(self.__time)*2). \
        #             reshape((len(self.__geoentity), len(self.__time), 2))

    def size(self):
        """Returns dimensions."""
        return(self.data.shapex)

    def __getitem__(self, key):
        print key
        return(self.data[key])

    def addGeoentities(self, geoentities):
        """Adds the geoentities dimension."""
        self.geoentities = geoentities
        self.data.reshape((self.geoentitiesSize(), self.timeSize()))

    def getData(self, geoentity=None, time=None):
        geo = [self.__geoentity.index(x) for x in geoentity] if geoentity else None
        t = time if time else 0
        print geo
        return(self.data[geo, t])

    def addVariable(self, array, name):
        self.__variable.append(name)
        array.resize(len(self.__geoentity), len(self.__time), 1)

        if len(self.__variable)==1:
            self.data = array

        else: 
            self.data = np.append(self.data, array, axis=2)

        print(self.__variable)


        self.data.resize((len(self.__geoentity), len(self.__time), len(self.__variable)))
        # self.data[:,:,len(self.__variable)-1] = array




        # else:
        #     self.data = np.append(self.data, array, axis=2)






x = GeoVariableArray(["ES","DE"],[datetime(2013,01,01), datetime(2014,1,1)]) # , datetime(2012,1,1)])
y = np.array([1,1,1,1]).reshape(2,2)
x.addVariable(y, "V0")
x.addVariable(y+1, "V1")
x.addVariable(y+2, "V2")

# print x.data()
# print
# print x.data(geoentity=0, time=0)
# print
# print x.data(geoentity=[1:,1:], time=None)

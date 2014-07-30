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




class TimeInterval(object):
    """Time interval for Equidna."""
    start = None
    end = None

    def __init__(self, startStr, endStr):
        """Initializator."""
        self.start = datetime.strptime(startStr, self.__getStrptime(startStr)) \
                     if startStr else None
        self.end = datetime.strptime(endStr, self.__getStrptime(endStr)) \
                   if endStr else None

        if self.start and self.end and self.start>=self.end:
            self.start = None
            self.end = None

    def timeIn(self, time):
        if isinstance(time, str):
            time = datetime.strptime(time, self.__getStrptime(time))

        if self.start and self.end and self.start<=time and time<=self.end:
            return(True)
        if self.start and self.end is None and self.start<=time:
            return(True)
        if self.start is None and self.end and time<=self.end:
            return(True)

        return(False)

    def __str__(self):
        """To str."""
        return("TimeInterval: "+str(self.start)+" | "+str(self.end))

    def __getStrptime(self, strptime):
        """Get the strptime."""
        if ":" in strptime:
            strp = "%Y-%m-%d %H:%M"
        else:
            strp = "%Y-%m-%d"

        return(strp)

        


    



e0 = TimeInterval("2013-01-01", "2014-01-01")
e1 = TimeInterval("2015-01-01", "2014-01-01")
e2 = TimeInterval("2013-01-01", None)
e3 = TimeInterval(None, "2015-01-01")
e4 = TimeInterval("2014-01-01", "2015-01-01")
t = datetime(2013,6,1)
print e0.timeIn(t), e1.timeIn(t), e2.timeIn(t), e3.timeIn(t), e4.timeIn(t)




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

    def size(self):
        """Returns dimensions."""
        return(self.data.shapex)

    def __getitem__(self, key):
        print key
        print type(key)
        print type(key[0])
        print type(key[1])
        print type(key[2])
        if isinstance(key[0], str):
            geo = [key[0]]
        if isinstance(key[1], str):
            time = [key[1]]
        if isinstance(key[2], str):
            var = [key[2]]

        print geo, time, var
        
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
        self.data.resize((len(self.__geoentity), len(self.__time), len(self.__variable)))

    





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

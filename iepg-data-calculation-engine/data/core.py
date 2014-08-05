# coding=UTF8

# --------------------------------
# Equidna Data Engine Core Classes
# --------------------------------

import numpy as np
from datetime import datetime



class Time(object):
    """Time interval for Equidna."""
    start = None
    end = None

    def __init__(self, *timeInit):
        """Initializator."""
        if isinstance(timeInit[0], str) and len(timeInit)==1:
            if "|" in timeInit[0]:
                self.start = self._getDatetime(timeInit[0].split("|")[0])
                self.end = self._getDatetime(timeInit[0].split("|")[1])
            else:
                self.start = self._getDatetime(timeInit[0])
                self.end = self._getDatetime(timeInit[0])
        if len(timeInit)==2:
            self.start = self._getDatetime(timeInit[0])
            self.end = self._getDatetime(timeInit[1])

        if isinstance(timeInit[0], int) and len(timeInit)==3:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2])
            self.end = datetime(timeInit[0], timeInit[1], timeInit[2])

        if isinstance(timeInit[0], int) and len(timeInit)==4 and timeInit[3] is None:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2])
            self.end = None

        if isinstance(timeInit[0], int) and len(timeInit)==5:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])
            self.end = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])

        if isinstance(timeInit[0], int) and len(timeInit)==5:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])
            self.end = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])

        if isinstance(timeInit[0], int) and len(timeInit)==6 and timeInit[5] is not None:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2])
            self.end = datetime(timeInit[3], timeInit[4], timeInit[5])

        if isinstance(timeInit[0], int) and len(timeInit)==6 and timeInit[5] is None:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])
            self.end = None

        if isinstance(timeInit[0], int) and len(timeInit)==10:
            self.start = datetime(timeInit[0], timeInit[1], timeInit[2], timeInit[3], timeInit[4])
            self.end = datetime(timeInit[5], timeInit[6], timeInit[7], timeInit[8], timeInit[9])

        if timeInit[0] is None and len(timeInit)==6:
            self.start = None
            self.end = datetime(timeInit[1], timeInit[2], timeInit[3], timeInit[4], timeInit[5])

        if timeInit[0] is None and len(timeInit)==4:
            self.start = None
            self.end = datetime(timeInit[1], timeInit[2], timeInit[3])

    def __div__(self, time):
        """Operator overload. Returns True if time is into the interval,
        extremes included. It gets either a datetime object or a
        string in ISO.

        """
        if not isinstance(time, Time):
            time = Time(time)

        if self.start and self.end and self.start<=time.start and time.end<=self.end:
            return(True)
        if self.start and self.end is None and self.start<=time.start:
            return(True)
        if self.start is None and self.end and time.end<=self.end:
            return(True)

        return(False)

    def __str__(self):
        """To str."""
        return("Time: "+str(self.start)+" | "+str(self.end))

    def _getDatetime(self, strptime):
        """Get the strptime."""
        if strptime=="" or strptime is None: return(None)

        if ":" in strptime:
            strp = "%Y-%m-%d %H:%M"
        else:
            strp = "%Y-%m-%d"

        return(datetime.strptime(strptime, strp))



class GeoVariableArray(object):
    """Data array for Equidna."""
    data = None
    __geoentity = None
    __time = None
    __variable = None

    def __init__(self, geoentity, time):
        """Initializator. Gets a list of geoentities and times to initialize the data array."""
        if not isinstance(geoentity, list) or not isinstance(time, list):
            raise EquidnaDataException("Both geoentity and time must be lists.")
        self.__geoentity = geoentity
        self.__time = time
        self.__variable = []
        self.data = np.empty((len(self.__geoentity), len(self.__time), 1))

    def shape(self):
        """Returns dimensions."""
        return(self.data.shape)

    def __getitem__(self, key):
        geo = self.__analyzeKey(key[0], self.__geoentity)
        time = self.__analyzeKey(key[1], self.__time)
        var = self.__analyzeKey(key[2], self.__variable)
        return(self.data[geo,time,var])

    def __analyzeKey(self, key, dimension):
        """Analyses key for a given dimension."""
        if isinstance(dimension[0], Time) and callable(key):
            out = ()
            for i in range(0, len(dimension)):
                if key(dimension[i]):
                    out+=(i,)
            return(out)
        if isinstance(key, str):
            return(dimension.index(key))
        if isinstance(key, tuple):
            out = ()
            for i in key:
                out+=(self.__analyzeKey(i, dimension),)
            return(out)
        if isinstance(key, (int, slice)):
            return(key)

    def addGeoentity(self, geoentity):
        """Adds the geoentities dimension. Geoentity can be a string or a list
        of strings. WARNING! Values added to the matrix are random!
        Initialize true values inmediatly!

        """
        if isinstance(geoentity, str):
            geoentity = [geoentity]
        geoentity = list(set(geoentity))
        self.geoentity.extend([x for x in geoentity if x not in self.geoentity])
        s = self.shape()
        self.data.resize((s[0]+len(geoentity),s[1],s[2]))

    @property
    def geoentity(self):
        """Geoentities."""
        return(self.__geoentity)

    @property
    def time(self):
        """Time intervals."""
        return(self.__time)

    @property
    def variable(self):
        """Variables."""
        return(self.__variable)

    def addVariable(self, array, name):
        self.__variable.append(name)
        array.resize(len(self.__geoentity), len(self.__time), 1)
        if len(self.__variable)==1:
            self.data = array
        else: 
            self.data = np.append(self.data, array, axis=2)
        self.data.resize((len(self.__geoentity), len(self.__time), len(self.__variable)))



class EquidnaDataException(Exception):
    """Exception for Equidna data."""
    _message = ""

    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return("EquidnaDataException: "+self._message)

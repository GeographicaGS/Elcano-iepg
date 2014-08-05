# coding=UTF8

# --------------------------------
# Equidna Data Engine Core Classes
# --------------------------------

import numpy as np, hashlib
from datetime import datetime

VAR_TYPE_CONTINUOUS = 0
VAR_TYPE_DISCRETE = 1

# TODO: TAKE INTO ACCOUNT Numpy TYPE SYSTEM
DATA_TYPE_NONE = 0
DATA_TYPE_NAN = 1
DATA_TYPE_FLOAT = 2
DATA_TYPE_INT = 3

class Geoentity(object):
    """TODO: Geoentity class."""
    pass



class Variable(object):
    """TODO: Variable class. Make stronger."""
    _filiation = None
    _languages = None
    _names = None
    _descriptions = None
    _units = None
    _varType = None
    _dataType = None
    _traits = None

    def __init__(self, filiation, languages, names, descriptions, units, varType, dataType, traits):
        """Constructor. TODO: accept names and descriptions and units as
        strings. Expand to the number of languages involved.

        """
        if filiation is None:
            raise EquidnaDataException("Filiation cannot be None.")
        self._filiation = filiation.split(".")
        self._languages = languages

        self._names = dict()
        self._descriptions = dict()
        self._units = dict()
        
        for i in range(0, len(self._languages)):
            if names:
                self._names[self._languages[i]] = names[i]
            if descriptions:
                self._descriptions[self._languages[i]] = descriptions[i]
            if units:
                self._units[self._languages[i]] = units[i]

        self._varType = varType
        self._dataType = dataType
        self._traits = traits

    @property
    def filiation(self):
        """Variable filiation."""
        return(self._filiation)

    @property
    def languages(self):
        """Variable languages."""
        return(self._languages)

    @property
    def names(self):
        """Names."""
        return(self._names)

    @property
    def descriptions(self):
        """Descriptions."""
        return(self._descriptions)

    @property
    def units(self):
        """Variable units."""
        return(self._units)
    
    @property
    def varType(self):
        """Variable type: continuous / discrete."""
        return(self._varType)

    @property
    def dataType(self):
        """Data type (integer, etc.)."""
        return(self._dataType)
    
    @property
    def traits(self):
        """Variable traits."""
        return(self._traits)

    def __hash__(self):
        """Returns the hash."""
        return(int(hashlib.sha256(str(self._filiation)).hexdigest(), base=16))

    def __str__(self):
        """To string."""
        return(str(self._filiation))

        
        
    



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
    """Data array for Equidna. TODO: test if Numpy supports discrete
    values.

    """
    __data = None
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
        self.__data = np.empty((len(self.__geoentity), len(self.__time), 1))

    @property
    def shape(self):
        """Returns dimensions."""
        return(self.__data.shape)

    def __getitem__(self, key):
        """TODO: implement slicing in the following ways:

        """
        geo = self.__analyzeKey(key[0], self.__geoentity)
        time = self.__analyzeKeyTime(key[1])
        var = self.__analyzeKey(key[2], self.__variable)
        return(self.__data[geo,time,var])

    def __analyzeKeyTime(self, key):
        """Analyses a time key."""
        if callable(key):
            out = ()
            for i in range(0, len(self.__time)):
                if key(self.__time[i]):
                    out+=(i,)
            return(out)
        if isinstance(key, (str, Time)):
            out = ()
            for i in range(0, len(self.__time)):
                if self.__time[i]/key:
                    out+=(i,)
            return(out)
        if isinstance(key, tuple):
            out = ()
            for i in key:
                out+=(self.__analyzeKeyTime(i),)
            return(out)
        if isinstance(key, (int, slice)):
            return(key)
        
    def __analyzeKey(self, key, dimension):
        """Analyses key for a given dimension."""
        if isinstance(key, str) and isinstance(dimension[0], Time):
            out = ()
            t = Time(key)
            for i in range(0, len(dimension)):
                if dimension[i]/key:
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
        """Adds new geoentities to the geoentity dimension. Geoentity can be a
        string or a list of strings. WARNING! Values added to the
        matrix are random! Initialize true values inmediatly!

        """
        geoentity = list(set([geoentity] if isinstance(geoentity, str) else geoentity))
        self.__geoentity.extend([x for x in geoentity if x not in self.__geoentity])
        s = self.shape
        self.__data.resize((s[0]+len(geoentity),s[1],s[2]))

    def addTime(self, time):
        """Adds new times to the time dimension. time can be a Time or a list
        of Time. WARNING! Values added to the matrix are random!
        Initialize true values inmediatly!

        """
        time = list(set([time] if isinstance(time, Time) else time))
        self.__time.extend([x for x in time if x not in self.__time])
        s = self.shape
        self.__data.resize((s[0],s[1]+len(time),s[2]))

    @property
    def data(self):
        """Data matrix. It's a Numpy ndarray object."""
        return(self.__data)

    @property
    def geoentity(self):
        """Geoentities in the data matrix."""
        return(self.__geoentity)

    @property
    def time(self):
        """Times in the data matrix."""
        return(self.__time)

    @property
    def variable(self):
        """Variables in the data matrix."""
        return(self.__variable)

    def addVariable(self, name, darray):
        """Adds a new variable to the variables dimension. Variables can be a
        string or a list of strings. darray is a numpy ndarray.

        """
        name = [name] if isinstance(name, str) else name
        darray = [darray] if isinstance(darray, np.ndarray) else darray
        if len(name)!=len(darray):
            raise EquidnaDataException("Variable names and matrices number mismatch.")

        for i in range(0, len(name)):
            if name[i] in self.variable:
                continue
            darr = np.copy(darray[i])
            s = self.shape
            darr.resize(s[0], s[1], 1) 
            self.__variable.append(name[i])
            if len(self.__variable)==1:
                self.__data = darr
            else: 
                self.__data = np.append(self.__data, darr, axis=2)
                self.__data.resize((len(self.__geoentity), len(self.__time), len(self.__variable)))



class EquidnaDataException(Exception):
    """Exception for Equidna data."""
    _message = ""

    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return("EquidnaDataException: "+self._message)

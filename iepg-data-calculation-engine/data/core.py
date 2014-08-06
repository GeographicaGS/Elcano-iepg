# coding=UTF8

# --------------------------------
# Equidna Data Engine Core Classes
# --------------------------------

import numpy as np, hashlib, arrayops



reload(arrayops)



from datetime import datetime

VAR_TYPE_CONTINUOUS = 0
VAR_TYPE_DISCRETE = 1



class Geoentity(object):
    """TODO: Geoentity class."""
    pass



class Variable(object):
    """TODO: Variable class. Make stronger.

    TODO: accept names and descriptions and units as strings. Expand
    to the number of languages involved.

    - **filiation:** a dot separated filiation trace (IEPG.Economic.Energy);
    - **varType:** either VAR_TYPE_CONTINUOUS or VAR_TYPE_DISCRETE. It defaults to VAR_TYPE_CONTINUOUS;
    - **dataType:** a Numpy data type. Defaults to numpy.float64;
    - **languages:** list of language codes for names, descriptions and units. Must be declared for names, descriptions, and units to be added (["ES", "EN"]);
    - **names:** list of names in languages (["Energía", "Energy"]);
    - **descriptions:** list of descriptions (["Desc ES", "Desc EN"]);
    - **units:** list of units in languages (["Kw/h", "Kw/h"]);
    - **traits:** a dictionary with custom traits.

    """
    _filiation = None
    _languages = None
    _names = None
    _descriptions = None
    _units = None
    _varType = None
    _dataType = None
    _traits = None

    def __init__(self, filiation, varType=VAR_TYPE_CONTINUOUS, dataType=np.float_, 
                 languages=None, names=None, descriptions=None, 
                 units=None, traits=None):
        """Constructor. See general class description."""
        if filiation is None or filiation=="":
            raise EquidnaDataException("Bad filiation.")
        self._filiation = filiation.split(".")
        self._languages = languages

        if languages:
            for i in range(0, len(self._languages)):
                if names:
                    self._names = dict()
                    self._names[self._languages[i]] = names[i]
                if descriptions:
                    self._descriptions = dict()
                    self._descriptions[self._languages[i]] = descriptions[i]
                if units:
                    self._units = dict()
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
        """Initializator. TODO: initialize months with str syntax '2013-01'."""
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

    def __lt__(self, other):
        """Less than. Compares lower limit."""
        return self.start<other.start

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
            if "-" not in strptime:
                strptime = strptime.split(".")[0] if "." in strptime else strptime
                strptime = strptime+"-07-01"

        return(datetime.strptime(strptime, strp))

    def __hash__(self):
        """Get the hash."""
        return(int(hashlib.sha256(str(self)).hexdigest(), base=16))



class GeoVariableArray(object):
    """Data array for Equidna. TODO: test if Numpy supports discrete
    values.

    """
    __data = None
    __geoentity = None
    __time = None
    __variable = None

    def __init__(self, geoentity, time):
        """Initializator. Gets a list of geoentities and times to initialize
        the data array. TODO: initialize time with a list of strings.

        """
        self.__geoentity = [geoentity] if not isinstance(geoentity, list) else geoentity
        time = [time] if not isinstance(time, list) else time
        self.__time = [Time(x) for x in time if not isinstance(x, Time)]
        self.__time.extend([x for x in time if isinstance(x, Time)])
        self.__variable = []
        self.__data = np.empty((len(self.__geoentity), len(self.__time), 1))
        self.__data[:] = np.nan

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

    def __setitem__(self, key, value):
        """Set item."""
        geo = self.__analyzeKey(key[0], self.__geoentity)
        time = self.__analyzeKeyTime(key[1])
        var = self.__analyzeKey(key[2], self.__variable)

        self.__data[geo,time,var]=value

    def sort(self):
        unsorted = True
        while unsorted:
            unsorted = False
            i = 0
            while i<len(self.geoentity)-1:
                if self.geoentity[i]>self.geoentity[i+1]:
                    x = self.geoentity[i]
                    y = self.geoentity[i+1]
                    a = np.array(self.__data[i,:,:])
                    b = np.array(self.__data[i+1,:,:])
                    self.geoentity[i] = y
                    self.geoentity[i+1] = x
                    self.__data[i,:,:] = b
                    self.__data[i+1,:,:] = a
                    unsorted = True
                else:
                    i+=1

        unsorted = True
        while unsorted:
            unsorted = False
            i = 0
            while i<len(self.time)-1:
                if self.time[i]>self.time[i+1]:
                    x = self.time[i]
                    y = self.time[i+1]
                    a = np.array(self.__data[:,i,:])
                    b = np.array(self.__data[:,i+1,:])
                    self.time[i] = y
                    self.time[i+1] = x
                    self.__data[:,i,:] = b
                    self.__data[:,i+1,:] = a
                    unsorted = True
                else:
                    i+=1

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

    def addGeoentity(self, geoentity, data=None):
        """Adds new geoentities to the geoentity dimension. Geoentity can be a
        string or a list of strings. WARNING! Values added to the
        matrix are random! Initialize true values inmediatly!

        TODO: provide data matrix.

        """
        geoentity = [geoentity] if not isinstance(geoentity, list) else geoentity
        data = [data] if data and not isinstance(data[0], list) else data
        
        for i in range(0, len(geoentity)):
            s = self.shape
            if not data:
                dataA = np.empty((1,s[1],1))
                dataA[:] = np.nan
            else:
                dataA = data[i]
            self.__data = np.append(self.__data, np.array(dataA).reshape(1, s[1], s[2]), 
                                    axis=0)
            self.__geoentity.append(geoentity[i])

    def addTime(self, time, data=None):
        """Adds new times to the time dimension. time can be a Time or a list
        of Time. WARNING! Values added to the matrix are random!
        Initialize true values inmediatly!

        """
        time = [time] if not isinstance(time, list) else time
        data = [data] if data and not isinstance(data[0], list) else data
        
        for i in range(0, len(time)):
            s = self.shape
            if not data:
                dataA = np.empty((s[0],1,1))
                dataA[:] = np.nan
            else:
                dataA = data[i]
            self.__data = np.append(self.__data, np.array(dataA).reshape(s[0], 1, s[2]), 
                                    axis=1)
            self.__time.append(Time(time[i]) if not isinstance(time[i], Time) else time[i])

    def addVariable(self, name, darray):
        """Adds a new variable to the variables dimension. Variables can be a
        string or a list of strings. darray is a unidimensional numpy ndarray.

        TODO: check other addXXX methods and reharse this. CRAP!

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

    def merge(self, geoVariableArray):
        """Merges two GeoVariableArrays."""

        HERE!!!


        print self.geoentity
        print geoVariableArray.geoentity

        diffGeoentity = arrayops.arraySubstraction(geoVariableArray.geoentity, self.geoentity)

        print diffGeoentity

        self.addGeoentity(diffGeoentity)

        print self.geoentity

        # print geoVariableArray[diffGeoentity

        print
        print
        print self.time
        print geoVariableArray.time

        diffTime = arrayops.arraySubstraction(geoVariableArray.time, self.time)

        print diffTime

        self.addTime(diffTime)

        print self.time

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



class EquidnaDataException(Exception):
    """Exception for Equidna data."""
    _message = ""

    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return("EquidnaDataException: "+self._message)

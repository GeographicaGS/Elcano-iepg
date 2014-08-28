# coding=UTF8

# --------------------------------
# Equidna Data Engine Core Classes
# --------------------------------

import numpy as np, hashlib, arrayops
from datetime import datetime, timedelta
import calendar

VAR_TYPE_CONTINUOUS = 0
VAR_TYPE_DISCRETE = 1

COPY_ALL = 0
COPY_GEOENTITIES = 1
COPY_TIMES = 2



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
        if len(timeInit)==1:
            if "|" in timeInit[0]:
                self.start = self._getDatetime(timeInit[0].split("|")[0])
                self.end = self._getDatetime(timeInit[0].split("|")[1], lowerLimit=False, initialTime=self.start)
            else:
                self.start = self._getDatetime(timeInit[0])
                self.end = self._getDatetime(timeInit[0], lowerLimit=False, initialTime=self.start)
        if len(timeInit)==2:
            self.start = self._getDatetime(timeInit[0])
            self.end = self._getDatetime(timeInit[1], lowerLimit=False, initialTime=self.start)

        if self.start and self.end and self.start>self.end:
            self.start = None
            self.end = None

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

    def _getDatetime(self, strptime, lowerLimit=True, initialTime=None):
        """Get the strptime."""
        if strptime=="" or strptime is None: return(None)


        # TODO: arreglar esto para que funcione con decrecimientos de año, contemplar las dos fechas a la vez, no hacer una análisis por separado.
        if any([x in strptime for x in ("Y","M","W","D","H","m","S")]) and initialTime:
            for x in ("Y","M","W","D","H","m","S"):
                parse = strptime.split(x)
                if len(parse)>1:
                    c = int(parse[0])
                    strptime = parse[1]
                    if x=="Y":
                        initialTime += datetime(initialTime.year+c, initialTime.month, initialTime.day, \
                                                initialTime.hour, initialTime.minute, initialTime.second) - \
                            initialTime
                    if x=="M":
                        if initialTime.month==12:
                            initialTime += datetime(initialTime.year+c, 1, initialTime.day, \
                                                    initialTime.hour, initialTime.minute, initialTime.second) - \
                                initialTime
                        else:
                            initialTime += datetime(initialTime.year, initialTime.month+c, initialTime.day, \
                                                    initialTime.hour, initialTime.minute, initialTime.second) - \
                                initialTime
                    if x=="W":
                        initialTime += timedelta(weeks=c)
                    if x=="D":
                        initialTime += timedelta(days=c)
                    if x=="H":
                        initialTime += timedelta(hours=c)
                    if x=="m":
                        initialTime += timedelta(minutes=c)
                    if x=="S":
                        initialTime += timedelta(seconds=c)

            return initialTime



        strp = "%Y-%m-%d %H:%M:%S"
        dt = strptime.split(" ")

        # Process date
        ymd = dt[0].split("-")
        if len(ymd)==2:
            if lowerLimit:
                ymd.append("01")
            else:
                days = calendar.monthrange(int(ymd[0]), int(ymd[1]))[1]
                ymd.append(str(days))
        if len(ymd)==1:
            if lowerLimit:
                ymd.extend(["01","01"])
            else:
                ymd.extend(["12","31"])

        # Process time
        if len(dt)==2:
            hms = dt[1].split(":")
            if len(hms)==2:
                if lowerLimit:
                    hms.append("00")
                else:
                    hms.append("59")
            if len(hms)==1:
                if lowerLimit:
                    hms.extend(["00","00"])
                else:
                    hms.extend(["59","59"])
        else:
            if lowerLimit:
                hms = ["00","00","00"]
            else:
                hms = ["23","59","59"]

        strptime = str(int(float(ymd[0])))+"-"+ymd[1]+"-"+ymd[2]+" "+hms[0]+":"+hms[1]+":"+hms[2]
        return(datetime.strptime(strptime, strp))

    def __hash__(self):
        """Get the hash."""
        return(int(hashlib.sha256(str(self)).hexdigest(), base=16))



class GeoVariableArray(object):
    """Data array for Equidna. Instantiate it with a list of geoentities and times.

    TODO: test if Numpy supports discrete values. 
    TODO: initialize time with a list of strings. 
    TODO: accessing the object like "x" should return the data array

    """
    __data = None
    __geoentity = None
    __time = None
    __variable = None

    def __init__(self, geoentity=None, time=None, variable=None, data=None):
        """Initializator. Gets a list of geoentities and times to initialize
        the data array. TODO: initialize time with a list of strings.

        """
        self.__geoentity = [geoentity] if geoentity and not isinstance(geoentity, list) else geoentity
        if time:
            time = [time] if not isinstance(time, list) else time
            self.__time = [Time(x) for x in time if not isinstance(x, Time)] if time else None
            self.__time.extend([x for x in time if isinstance(x, Time)])
        self.__variable = [variable] if variable and not isinstance(variable, list) else variable
        
        self.__addDataToMatrix(data=data)

    def __addDataToMatrix(self, data=None, dimension=None):
        """Adds data if the matrix is fully configured with geoentities,
        times, and variables. Set it to nan if there are no data,
        otherwise, adds the passed data, if any, to the given
        dimension (if any, otherwise sets the whole matrix).

        """
        # print "EW : ", data
        # print "EW : ", dimension
        # print "EW : ", self.__data is not None and dimension is not None

        # Creates the array if not there and all is in place
        arrayJustCreated = False
        if self.__data is None:
            if self.__variable and self.__geoentity and self.__time:
                self.__data = np.empty((len(self.__geoentity), len(self.__time), len(self.__variable)))
                arrayJustCreated = True

        if self.__data is not None and data is not None and dimension is None:
            # Initializes data to full array
            self.__data = np.array(data).reshape((len(self.__geoentity), 
                                                  len(self.__time), len(self.__variable)))
        elif self.__data is not None and dimension is not None:
            # Adds data to a dimension, either blank or real data
            s = self.shape
            if dimension==0 and not arrayJustCreated:
                if data:
                    dataA = data
                else:
                    dataA = np.empty((1,s[1],s[2]))
                    dataA[:] = np.nan
                self.__data = np.append(self.__data, np.array(dataA).reshape(1,s[1],s[2]), axis=dimension)
            elif dimension==0:
                if data:
                    self.__data = np.array(data).reshape(s[0],s[1],s[2])
                else:
                    self.__data[:] = np.nan
            if dimension==1 and not arrayJustCreated:
                if data:
                    dataA = data
                else:
                    dataA = np.empty((s[0],1,s[2]))
                    dataA[:] = np.nan
                self.__data = np.append(self.__data, np.array(dataA).reshape(s[0],1,s[2]), axis=dimension)
            elif dimension==1:
                if data:
                    self.__data = np.array(data).reshape(s[0],s[1],s[2])
                else:
                    self.__data[:] = np.nan
            if dimension==2 and not arrayJustCreated:
                if data:
                    dataA = data
                else:
                    dataA = np.empty((s[0],s[1],1))
                    dataA[:] = np.nan
                self.__data = np.append(self.__data, np.array(dataA).reshape(s[0],s[1],1), axis=dimension)
            elif dimension==2:
                if data:
                    self.__data = np.array(data).reshape(s[0],s[1],s[2])
                else:
                    self.__data[:] = np.nan
        elif self.__data is not None:
            self.__data[:] = np.nan

    def __call__(self):
        """Returns the data array."""
        return self.__data

    @property
    def geoentity(self):

        """Geoentity instances in the data matrix."""
        return(self.__geoentity)

    @property
    def time(self):
        """Times instances in the data matrix."""
        return(self.__time)

    @property
    def variable(self):
        """Variable instances in the data matrix."""
        return(self.__variable)

    @property
    def shape(self):
        """Returns dimensions of the data matrix. First item is Geoentity number, second Time, 
        and third Variable."""
        if self.__data is not None:
            return self.__data.shape
        else:
            return None

    @property
    def size(self):
        """Returns size of data: Geoentity x Time x Variable."""
        return self.__data.size

    @property
    def data(self):
        """Data matrix. It's a Numpy ndarray object."""
        return(self.__data)

    def __getitem__(self, key):
        """Gets data. NOTE: Always retrieve data with a [:,:,:] format. If not, it returns None."""
        if not isinstance(key, tuple) or len(key)<3:
            return None

        # print "Start geo: ", key[0], type(key[0])
        # print "Start time: ", key[1], type(key[1])
        # print "Start var: ", key[2], type(key[2])

        geo = self.__analyzeKeyGeoentity(key[0])
        time = self.__analyzeKeyTime(key[1])
        var = self.__analyzeKeyVariable(key[2])

        # Filter void tuples
        if geo==() or time==() or var==(): return None

        # Filter single element tuples like (2,) to int
        geo = int(geo[0]) if isinstance(geo, tuple) and len(geo)==1 else geo
        time = int(time[0]) if isinstance(time, tuple) and len(time)==1 else time
        var = int(var[0]) if isinstance(var, tuple) and len(var)==1 else var


        print "End geo: ", geo, type(geo)
        print "End time: ", time, type(time)
        print "End var: ", var, type(var)

        if isinstance(geo, slice):
            start = geo.start if geo.start else 0
            stop = geo.stop if geo.stop else len(self.__geoentity)
            step = geo.step if geo.step else 1
            itemsGeo = [self.__geoentity[i] for i in range(start, stop, step)]
        elif isinstance(geo, int):
            itemsGeo = [self.__geoentity[geo]]
        else:
            itemsGeo = [self.__geoentity[i] for i in geo]

        if isinstance(time, slice):
            start = time.start if time.start else 0
            stop = time.stop if time.stop else len(self.__time)
            step = time.step if time.step else 1
            itemsTime = [self.__time[i] for i in range(start, stop, step)]
        elif isinstance(time, int):
            itemsTime = [self.__time[time]]
        else:
            itemsTime = [self.__time[i] for i in time]

        if isinstance(var, slice):
            start = var.start if var.start else 0
            stop = var.stop if var.stop else len(self.__geoentity)
            step = var.step if var.step else 1
            itemsVar = [self.__variable[i] for i in range(start, stop, step)]
        elif isinstance(var, int):
            itemsVar = [self.__variable[var]]
        else:
            itemsVar = [self.__variable[i] for i in var]


        print "Items geo: ", itemsGeo
        print "Items time: ", itemsTime
        print "Items var: ", itemsVar


        # If any of the indices is a tuple, life becomes a little bit miserable
        if any([str(type(x))=="<type 'tuple'>" for x in (geo,time,var)]):
            ordered = True
            sequence = [geo,time,var]
            typ = ["geo","time","var"]
            while ordered:
                ordered = False
                # print "Ordered : ", sequence, typ
                i = 0
                while i<2:
                    if not isinstance(sequence[i], tuple) and isinstance(sequence[i+1], tuple):
                        sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                        typ[i], typ[i+1] = typ[i+1], typ[i]
                        ordered = True
                    else:
                        i+=1

            out = self.__data
            dims = 3
            for i in range(0,3):
                # print "i : ", i
                # print "Dims : ", dims
                # print "out"
                # print out
                # print
                if typ[i]=="geo":
                    if dims==3:
                        out = out[geo,:,:]
                    if dims==2:
                        out = out[geo,:]
                    if dims==1:
                        out = out[geo]
                if typ[i]=="time":
                    if dims==3:
                        out = out[:,time,:]
                    if dims==2:
                        out = out[:,time]
                    if dims==1:
                        out = out[time]
                if typ[i]=="var":
                    if dims==3:
                        out = out[:,:,var]
                    if dims==2:
                        out = out[:,var]
                    if dims==1:
                        out = out[var]
                if not isinstance(sequence[i], tuple):
                    # print "Not tuple? :", type(typ[i])
                    dims-=1
            return out
        else:
            return self.__data[geo,time,var]

            

        # # if isinstance(key, (slice, int)):
        # #     return(self.__data[key])




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
        """Analyses a time key. TODO: this has a problem when asking for a
        non-existent year, like in data["US","2323","V0"]. FIX!

        """
        # print "UUU : ",key, type(key)

        if callable(key):
            out = ()
            for i in range(0, len(self.__time)):
                # print "ll : ", key(self.__time[i])
                if key(self.__time[i]):
                    out+=(i,)
            return out
        if isinstance(key, (str, Time)):
            out = ()
            for i in range(0, len(self.__time)):
                if self.__time[i]/key:
                    out+=(i,)
            return out
        if isinstance(key, tuple):
            out = ()
            for i in key:
                out+=(self.__analyzeKeyTime(i),)
            return tuple(x for y in out for x in y)
        if isinstance(key, (int, slice)):
            return key
        
    def __analyzeKeyGeoentity(self, key):
        """Analyses key for a given dimension."""
        if isinstance(key, str):
            return(self.geoentity.index(key))
        if isinstance(key, tuple):
            out = ()
            for i in key:
                out+=(self.__analyzeKeyGeoentity(i),)
            return(out)
        if isinstance(key, (int, slice)):
            return(key)

    def __analyzeKeyVariable(self, key):
        """Analyses key for a given dimension."""
        if isinstance(key, str):
            return(self.variable.index(key))
        if isinstance(key, tuple):
            out = ()
            for i in key:
                out+=(self.__analyzeKeyVariable(i),)
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

        if self.__geoentity is None:
            self.__geoentity = []

        for i in range(0, len(geoentity)):
            if geoentity[i] not in self.__geoentity:
                self.__geoentity.append(geoentity[i])
                if data is not None:
                    self.__addDataToMatrix(data=data[i], dimension=0)
                else:
                    self.__addDataToMatrix(dimension=0)

    def addTime(self, time, data=None):
        """Adds new times to the time dimension. time can be a Time or a list
        of Time. WARNING! Values added to the matrix are random!
        Initialize true values inmediatly!

        """
        time = [time] if not isinstance(time, list) else time
        data = [data] if data and not isinstance(data[0], list) else data

        if self.__time is None:
            self.__time = []

        for i in range(0, len(time)):
            if time[i] not in self.__time:
                self.__time.append(Time(time[i]) if not isinstance(time[i], Time) else time[i])
                if data is not None:
                    self.__addDataToMatrix(data=data[i], dimension=1)
                else:
                    self.__addDataToMatrix(dimension=1)

    def addVariable(self, variable, data=None):
        """Adds a new variable to the variables dimension. Variables can be a
        string or a list of strings. darray is a unidimensional numpy
        ndarray or a bidimensional one. There must be enough data to
        fit the size of the array.

        TODO: Use Variable objects here.
        TODO: check other addXXX methods and reharse this. CRAP!

        """
        variable = [variable] if not isinstance(variable, list) else variable
        data = [data] if data and not isinstance(data[0], list) else data

        if self.__variable is None:
            self.__variable = []

        for i in range(0, len(variable)):
            if variable[i] not in self.__variable:
                self.__variable.append(variable[i])
                if data is not None:
                    self.__addDataToMatrix(data=data[i], dimension=2)
                else:
                    self.__addDataToMatrix(dimension=2)
            

        # for i in range(0, len(name)):
        #     if name[i] in self.variable:
        #         continue

        #     if darray[i].size!=self.__data[:,:,0].size:
        #         raise EquidnaDataException("Data and GeoVariableArray must have the same size.")

        #     s = self.shape
        #     self.__variable.append(name[i])
        #     if len(self.__variable)==1:
        #         self.__data = darray[i].reshape((s[0],s[1],1))
        #     else: 
        #         self.__data = np.append(self.__data, darray[i].reshape((s[0],s[1],1)), axis=2)

    def copyStructure(self, copy=COPY_ALL):
        """Returns a GeoVariableArray with the same geoentities and times."""
        geoentity = []
        time = []

        if copy==COPY_ALL or copy==COPY_GEOENTITIES:
            geoentity = self.geoentity
        if copy==COPY_ALL or copy==COPY_TIMES:
            time = self.time

        return GeoVariableArray(geoentity, time)

    def merge(self, geoVariableArray):
        """Merges two GeoVariableArrays. If a variable is present in the
        second GeoVariableArray that is present in the first one it's
        omitted.

        """
        diffGeoentityAB = arrayops.arraySubstraction(self.geoentity, geoVariableArray.geoentity)
        diffGeoentityBA = arrayops.arraySubstraction(geoVariableArray.geoentity, self.geoentity)
        self.addGeoentity(diffGeoentityBA)
        geoVariableArray.addGeoentity(diffGeoentityAB)

        diffTimeAB = arrayops.arraySubstraction(self.time, geoVariableArray.time)
        diffTimeBA = arrayops.arraySubstraction(geoVariableArray.time, self.time)
        self.addTime(diffTimeBA)
        geoVariableArray.addTime(diffTimeAB)

        self.sort()
        geoVariableArray.sort()

        diffVariable = arrayops.arraySubstraction(geoVariableArray.variable, self.variable)
        self.addVariable(diffVariable, [geoVariableArray[:,:,x] for x in diffVariable])



class EquidnaDataException(Exception):
    """Exception for Equidna data."""
    _message = ""

    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return("EquidnaDataException: "+self._message)

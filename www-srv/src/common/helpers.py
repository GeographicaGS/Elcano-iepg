# coding=UTF8

"""

Common helpers.

"""
import hashlib
from config import MemcachedConfig
from flask import jsonify
from const import families, variables, blocks
import model.iepgdatamodel
if MemcachedConfig["enabled"] == True:
    import memcache


def cacheWrapper(funcName, *args, **kwargs):
    """Cache wrapping helper."""
    if MemcachedConfig["enabled"]:
        h = hashlib.sha256(funcName.__name__+str(args)+str(kwargs)).hexdigest()
        mc = memcache.Client([MemcachedConfig["host"]+":"+MemcachedConfig["port"]], debug=0)
        v = mc.get(h)
        if v:
            return(v)
        else:
            out = funcName(*args, **kwargs)
            mc.set(h, out, MemcachedConfig["expiration"])
            return(out)
    else:
        return(funcName(*args, **kwargs))


def baseMapData():
    m = basemap.GeometryData()
    geomData = cacheWrapper(m.geometryData)
    out = dict()
    for r in geomData:
        data = dict()
        data["name_en"] = r["name_en"]
        data["name_es"] = r["name_es"]
        data["geojson"] = r["geojson"]
        out[r["iso_3166_1_2_code"]] = data

    return(jsonify(out))


def getVariableData(family, key):
    """Retrieves variable data."""
    for k,i in variables.items():
        if i["family"]==family and i["key"]==key:
            return i
    
    return None


def blocksGetData(code):
    """Retrieves block data."""
    return(blocks[code])


def blocksCalculateData(blockCode, year, family, variable):
    """Calculates block data for a variable."""
    m = IepgDataModel()
    block = blocks[blockCode]
    print("ii", block)
    data = cacheWrapper(m.getCountriesData, block["members"][str(year)], year, family, variable)
    print(data)

    return(None)


def searchParser(searchString, searchFields):
    """Returns a where clause based on the search string syntax. Examples:
    
    +eu +eeuu +economía: eu AND eeuu AND economía
   
    (+eu +eeuu) economía: economía OR (eu AND eeuu)

    (+eu -eeuu) economía: economía OR (eu AND NOT eeuu)"""
    searchString=searchString.strip(" ")
    if searchString.count("(")<>searchString.count(")"):
        return(None)

    parentAtom = parseAtom(searchString)
    parentAtom.parse([openQuote, openParen, default])

    print(parentAtom)




class parseAtom(object):
    __atomSyntax = None
    __childAtoms = None
    __atomType = None
    __parentAtom = None

    def __init__(self, syntax, type=None, parent=None):
         self.__atomSyntax = syntax
         self.__atomType = type
         self.__childAtoms = []
         self.__parentAtom = parent

    def getSyntax(self):
        return(self.__atomSyntax)

    def getType(self):
        return(self.__atomType)

    def setType(self, type):
        self.__atomType = type

    def addChildAtom(self, atom):
        self.__childAtoms.append(atom)

    def parse(self, precedence):
        for t in precedence:
            out = t(self)
            if isinstance(out, parseAtom):
                self.__atomType = "Literal"

        l = True
        while l:
            l = False
            for a in self.getChildAtoms():
                if a.getType() is None:
                    a.parse(precedence)
                    l = True

    def getChildAtoms(self):
          return(self.__childAtoms)

    def hasChildAtoms(self):
        return(True if len(self.__childAtoms)>0 else false)

    def __str__(self):
        a = """
        Type: {}, Syntax: {}, Parent type: {}
        """.format(self.__atomType, self.__atomSyntax, 
                   self.__parentAtom.getType() if self.__parentAtom is not None else None)

        for i in self.__childAtoms:
            a+=str(i)

        return(a)




def openParen(atom):
    """Return splitted string based on closing parenthesses."""
    open = 0
    begin = -1
    end = -1
    string = atom.getSyntax()
    for i in range(0, len(string)):
        if string[i]=="(":
            open+=1
        if string[i]==")":
            open-=1
        if open==1 and begin==-1:
            begin = i
        if open==0 and begin<>-1:
            end = i
            break

    if begin<>-1 and end<>-1:
        atom.setType("Root")
        atom.addChildAtom(parseAtom(string[0:begin], parent=atom))
        atom.addChildAtom(parseAtom("(", type="Token", parent=atom))
        atom.addChildAtom(parseAtom(string[begin+1:end], parent=atom))
        atom.addChildAtom(parseAtom(")", type="Token", parent=atom))
        atom.addChildAtom(parseAtom(string[end+1:], parent=atom))
    else:
        return(atom)
 

def openQuote(atom):
    """Return splitted string based on double quotes."""
    open = 0
    begin = -1
    end = -1
    string = atom.getSyntax()
    for i in range(0, len(string)):
        if string[i]=='"' and begin>-1:
            end = i 
            break
        if string[i]=='"':
            begin = i

    if begin<>-1 and end<>-1:
        atom.setType("Root")
        atom.addChildAtom(parseAtom(string[0:begin], parent=atom))
        atom.addChildAtom(parseAtom('"', type="Token", parent=atom))
        atom.addChildAtom(parseAtom(string[begin+1:end], type="Literal", parent=atom))
        atom.addChildAtom(parseAtom('"', type="Token", parent=atom))
        atom.addChildAtom(parseAtom(string[end+1:], parent=atom))
    else:
        return(atom)


def default(atom):
    """Default parsing."""
    atom.setType("Default")

# coding=UTF8

"""

Maplex core

"""
import maplexmodel
import datetime

def addName(name, description):
    """Adds a name. Returns reference ID to the new name."""
    m = maplexmodel.MaplexModel()
    id = m.newName(name, description)
    return(id)


def getNameFamilies():
    """Returns name families."""
    m = maplexmodel.MaplexModel()
    return(m.getNameFamilies())


def assignGeoentityName(idGeoentity, idName, idNameFamily, dateIn=None, dateOut=None):
    """Assign a name to a geoentity.
    TODO: get down to the hour
    """
    if dateIn:
        dateIn = datetime.datetime.strptime(dateIn, '%Y-%m-%d')
    if dateOut:
        dateOut = datetime.datetime.strptime(dateOut, '%Y-%m-%d')
        
    m = maplexmodel.MaplexModel()
    id = m.assignGeoentityName(idGeoentity, idName, idNameFamily, dateIn=dateIn, dateOut=dateOut)
    return(id)


def getGeoentities():
   """Returns geoentities."""
   m = maplexmodel.MaplexModel()
   return(m.getGeoentities())


def getNames():
   """Returns names."""
   m = maplexmodel.MaplexModel()
   return(m.getNames())


def getBlocks():
    """TODO: end this."""
    pass

# coding=UTF8

"""

Maplex core

"""
import maplexmodel
import common.timelapse

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
    """Assign a name to a geoentity."""
    dateIn = common.timelapse.Time(dateIn) if dateIn else None
    dateOut = common.timelapse.Time(dateOut) if dateOut else None
        
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


def getName(idName):
   """Returns name with ID idName."""
   m = maplexmodel.MaplexModel()
   return(m.getName(idName))


def getBlocks(timeLapseBlock=None, timeLapseMembers=None):
    """Retrieves basic information about blocks."""
    m = maplexmodel.MaplexModel()
    return(m.getBlocks(timeLapseBlock, timeLapseMembers))

    

# coding=UTF8

"""

Maplex core

TODO: Can a geoentity have geoms by itself and be a block at the same time? > yes, it should
In this case, has any sense that the block itself has a date_in/date_out?
Think in the incorporation/separation process between geoentities, more than in the "block" 
concept. Think always in a TIMELINE fashion.

Geoentity is TOO abstract. A geoentity must have one multipolygon or none, then use the 
incorporation/separation process to manage geoentities relationships. This is MUCH better. TIMELINES of
aggregations/separations nested together.

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


def getNames(idNameFamily=None):
   """Returns names."""
   m = maplexmodel.MaplexModel()
   return(m.getNames(idNameFamily))


def getName(idName):
   """Returns name with ID idName."""
   m = maplexmodel.MaplexModel()
   return(m.getName(idName))


def getGeoentityNames(idGeoentity, idNameFamily):
    """Returns a list with all geoentity names corresponding to the given family."""
    m = maplexmodel.MaplexModel()
    return(m.getGeoentityNames(idGeoentity, idNameFamily))


def getIdGeoentityByName(name, idNameFamily):
    """Returns the idGeoentity for a name and ID name family."""
    m = maplexmodel.MaplexModel()
    return(m.getIdGeoentityByName(name, idNameFamily))

def getTranslationTable(idNameFamilyA, idNameFamilyB=None):
    """Returns two dictionaries: one keyer by idNameFamilyA to idNameFamilyB conversion,
    and reverse. If idNameFamilyB is None, idGeoentity is used as idNameFamilyB."""
    m = maplexmodel.MaplexModel()
    ab = dict()
    ba = dict()
    for d in m.getTranslationTable(idNameFamilyA, idNameFamilyB):
        ab[d["name_a"]] = d["name_b"]
        ba[d["name_b"]] = d["name_a"]
    return(ab, ba)



# TODO: redefine this method so it returns blocks whose existence is completely 
# within the lapse and make a difference on if the lapse is calculated by its members
# or the block itself
# Create a time topology: adjacency of timelapses, intersection of timelapses, containment of, etc...
# add after, before, coincident
# def getBlocks(timeLapseBlock=None, timeLapseMembers=None):
#     """Retrieves basic information about blocks."""
#     m = maplexmodel.MaplexModel()
#     return(m.getBlocks(timeLapseBlock, timeLapseMembers))


def getBlocks(timeLapseBlock=None, timeLapseMembers=None, idNameFamily=None):
    """Retrieves basic information about blocks. If idNameFamily is None, idGeoentity is returned."""
    m = maplexmodel.MaplexModel()
    return(m.getBlocks(timeLapseBlock, timeLapseMembers, idNameFamily))


def getBlockMembers(idGeoentityBlock, year=None, idNameFamily=None):
    """Retrieves block members. If idNameFamily is None, idGeoentity is returned. TODO: erase the idNameFamily
    from all functions. Stick exclusively to the id_geoentity. Use translation tables."""
    m = maplexmodel.MaplexModel()
    return(m.getBlockMembers(idGeoentityBlock, year, idNameFamily))


def getGeoentityBlocks(idGeoentity, year=None):
    """Returns all blocks idGeoentity is in."""
    m = maplexmodel.MaplexModel()
    return(m.getGeoentityBlocks(idGeoentity, year))


def isBlock(idGeoentity):
    """Returns True if idGeoentity is a block."""
    m = maplexmodel.MaplexModel()
    return(idGeoentity in m.idGeoentitiesBlocks(idGeoentity))

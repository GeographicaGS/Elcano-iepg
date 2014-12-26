# coding=UTF8

"""

Parser for searches.

"""
import hashlib
import datetime


class Parser(object):
    """Returns a where clause based on the search string syntax. Examples:
    
    +eu +eeuu +economía: eu AND eeuu AND economía
   
    (+eu +eeuu) economía: economía OR (eu AND eeuu)

    (+eu -eeuu) economía: economía OR (eu AND NOT eeuu)"""
    __code = None
    __atoms = None

    def __init__(self, code):
        self.__code = code
        self.__atoms = [Atom(code)]

    def getAtom(self, i):
        return(self.__atoms[i])

    def popAtom(self, i):
        self.__atoms.pop(i)

    def insertAtom(self, atom, i):
        self.__atoms.insert(i, atom)

    def parse(self, tokens, syntax):
        i = 0
        for i in tokens:
            k = 0
            while k<len(self.getAtoms()):
                if not self.getAtom(k).hasTypes():
                    a = self.getAtom(k).getSyntax().split(i["token"])
                    if len(a)>1:
                        self.popAtom(k)
                        for l in range(len(a)-1,0,-1):
                            if a[l]<>'':
                                self.insertAtom(Atom(a[l]),k)
                            self.insertAtom(Atom(i["token"], types=i["types"]),k)
                        if a[0]<>'':
                            self.insertAtom(Atom(a[0]),k)
                    else:
                        k+=1
                else:
                    k+=1

        for i in self.getAtoms():
            if not i.hasTypes():
                i.addType("Literal")

        for i in syntax:
            print(i)

    def getAtoms(self):
        return(self.__atoms)

    def str(self):
        for i in self.__atoms:
            print(i)
        s = ""
        for i in self.__atoms:
            s+=i.getSyntax()
        print(s)


class Atom(object):
    __syntax = None
    __types = None
    __hash = None
    __openAtom = None
    __closeAtom = None

    def __init__(self, syntax, types=[], openAtom=None, closeAtom=None):
         self.__syntax = syntax
         self.__types = types
         self.__openAtom = openAtom
         self.__closeAtom = closeAtom
         self.__hash = hashlib.md5(syntax+str(types)+str(datetime.datetime.utcnow().isoformat())).hexdigest()

    def getOpenAtom(self):
        return(self.__openAtom)

    def getCloseAtom(self):
        return(self.__closeAtom)

    def setOpenAtom(self, hash):
        self.__openAtom = hash

    def setCloseAtom(self, hash):
        self.__closeAtom = hash

    def getHash(self):
        return(self.__hash)

    def getSyntax(self):
        return(self.__syntax)

    def getTypes(self):
        return(self.__type)

    def isType(self, type):
        return(type in self.__types)

    def hasTypes(self):
        return(True if self.__types<>[] else False)

    def addType(self, type):
        self.__types.append(type)

    def getTypes(self):
        return(self.__types)

    def __str__(self):
        return("Types: {}, Syntax: {}, Hash: {}".format(self.__types, self.__syntax, self.__hash))


# def synWhitespaces(atoms):
#      """Process whitespaces."""
#      i = 0
#      while i<len(atoms):
#          if atoms[i].isType("Whitespace") and i==0:
#              atoms.pop(i)
#              continue
#          if atoms[i].isType("Whitespace") and i==len(atoms)-1:
#              atoms.pop(i)
#              continue
#          if atoms[i].isType("Whitespace") and atoms[i+1].isType("Whitespace"):
#              atoms.pop(i+1)
#              continue

#          i+=1


def synQuotes(atoms):
     """Erases quotes."""
     i = 0
     start = -1
     end = -1
     for i in range(0, len(atoms)):
         if atoms[i].isType('Double quote'):
             if start==-1:
                 start = i
             else:
                 end = i

     if start<>-1 and end==-1:



class ParserError(Exception):
    def __init__(self, error):
        Exception.__init__(self)
        self.error = error
        
    def __str__(self):
        return(self.error)
         


# def synPlusMinus(atoms):
#      """Erases consecutives +,- tokens."""
#      i = 0
#      while i<len(atoms):
#          if atoms[i].isType("plusminus") and atoms[i+1].isType("plusminus"):
#              atoms.pop(i+1)
#              continue
#          i+=1

#      i = 0
#      while i<len(atoms):
#          if atoms[i].isType("plusminus") and atoms[i+1].isType("Whitespace"):
#              atoms.pop(i+1)
#              continue
#          i+=1


# def synEmptyBlocks(atoms):
#      """Erases empty blocks."""
#      i = 0
#      changes = True
#      while changes:
#          changes = False
#          while i<len(atoms):
#              if atoms[i].isType("Token (") and atoms[i+1].isType("Token )"):
#                  atoms.pop(i)
#                  atoms.pop(i)
#                  changes = True
#                  continue
#              i+=1
#          i = 0
#          while i<len(atoms):
#              if atoms[i].isType("Token (") and atoms[i+1].isType("Whitespace") and atoms[i+2].isType("Token )"):
#                  atoms.pop(i)
#                  atoms.pop(i)
#                  atoms.pop(i)
#                  changes = True
#                  continue
#              i+=1
#          synWhitespaces(atoms)



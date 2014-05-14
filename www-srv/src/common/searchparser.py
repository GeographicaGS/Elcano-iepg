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

    def parse(self, precedence):
        while self.noType():
            for i in range(0, len(self.__atoms)):
                a = self.__atoms[i]
                if a.getType()==None:
                    o = a.parse(precedence)
                    atoms = []
                    for k in range(0, i):
                        atoms.append(self.__atoms[k])
                    for k in o:
                        atoms.append(k)
                    for k in range(i+1, len(self.__atoms)):
                        atoms.append(self.__atoms[k])
                    self.__atoms = atoms
                    break

    def noType(self):
        for i in self.__atoms:
            if i.getType()==None:
                return True

        return False

    def getAtoms(self):
        return(self.__atoms)

    def str(self):
        for i in self.__atoms:
            print(i)


class Atom(object):
    __syntax = None
    __type = None
    __hash = None

    def __init__(self, syntax, type=None):
         self.__syntax = syntax
         self.__type = type
         self.__hash = hashlib.md5(syntax+str(type)+str(datetime.datetime.now())).hexdigest()

    def getHash(self):
        return(self.__hash)

    def getSyntax(self):
        return(self.__syntax)

    def getType(self):
        return(self.__type)

    def setType(self, type):
        self.__type = type

    def parse(self, precedence):
        for t in precedence:
            out = t(self)
            if isinstance(out, list):
                return(out)

        return(out)

    def __str__(self):
        return("Type: {}, Syntax: {}, Hash: {}".format(self.__type, self.__syntax, self.__hash))


def rulePlusMinus(atom):
    string = atom.getSyntax()
    i = 0
    tokens = ["+","-"]
    out = []
    while i<len(string):
        b = 0
        while b<len(tokens):
            if string[i]==tokens[b]:
                e1 = string[0:i]
                e2 = string[i+1:]
                if e1<>"":
                    out.append(Atom(e1))
                out.append(Atom(tokens[b], type="Token"))
                if e2<>"":
                    out.append(Atom(e2))
                i = len(string)
                b = len(tokens)
            b+=1
        i+=1

    if out<>[]:
        return(out)
    else:
        return(atom)

def ruleBlock(atom):
    """Return splitted string based on closing parenthesses."""
    blocks=['(',')','[',']','"','"']
    open = 0
    begin = -1
    end = -1
    openItem = ""
    closeItem = ""
    string = atom.getSyntax()
    
    i = 0
    while i<len(string): 
        if string[i]==openItem and openItem<>closeItem:
            open+=1
        if string[i]==closeItem and openItem<>closeItem:
            open-=1
        if string[i]==closeItem and openItem==closeItem:
            end = i
            i = len(string)
        if open==0 and begin<>-1:
            end = i
            i = len(string)
        if openItem=="":
            for b in range(0, len(blocks), 2):
                if string[i]==blocks[b]:
                    openItem = blocks[b]
                    closeItem = blocks[b+1]
                    open+=1
                    begin = i
        i+=1

    if begin<>-1 and end<>-1:
        out = []
        e1 = string[0:begin]
        e2 = string[begin+1:end]
        e3 = string[end+1:]
        o = Atom(openItem, type="Block")
        c = Atom(closeItem, type="Block")
        o.closingAtom = c.getHash()
        c.openingAtom = o.getHash()
        if e1<>'':
            out.append(Atom(e1))
        out.append(o)
        if e2<>'':
            if openItem==closeItem:
                out.append(Atom(e2, type="Literal"))
            else:
                out.append(Atom(e2))
        out.append(c)
        if e3<>'':
            out.append(Atom(e3))
        return(out)
    else:
        return(atom)
 

def ruleDefault(atom):
    """Default parsing."""
    atom.setType("Literal")
    return([atom])

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

    def parse(self, tokenizers, syntax):
        for t in tokenizers:
            i = 0
            while i<len(self.__atoms):
                if not self.__atoms[i].hasTypes():
                    o = t(self.__atoms[i])
                    if o<>None:
                        atoms = []
                        for k in range(0, i):
                            atoms.append(self.__atoms[k])
                        for k in o:
                            atoms.append(k)
                        for k in range(i+1, len(self.__atoms)):
                            atoms.append(self.__atoms[k])
                        self.__atoms = atoms
                    else:
                        i+=1
                else:
                    i+=1

        for t in syntax:
            t(self.__atoms)


        return(self.__atoms)

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

    def __init__(self, syntax, types=[]):
         self.__syntax = syntax
         self.__types = types
         self.__hash = hashlib.md5(syntax+str(types)+str(datetime.datetime.now())).hexdigest()

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


def cleanUp(atoms):
    pass
    #     if atoms[i].isType('Token "'):
    #         atoms.pop(i)
    #         continue
    #     if atoms[i].isType("Comma") and atoms[i+1].isType("Whitespace"):
    #         atoms.pop(i+1)
    #         continue
    #     if atoms[i].isType("plusminus") and atoms[i+1].isType("plusminus"):
    #         atoms.pop(i+1)
    #         continue
    #     if atoms[i].isType("plusminus") and atoms[i+1].isType("Whitespace"):
    #         atoms.pop(i+1)
    #         continue
    #     if atoms[i].isType("Whitespace") and atoms[i+1].isType("plusminus"):
    #         atoms.pop(i)
    #         continue

    #     if atoms[i].isType("Token -") and atoms[i+1].isType("Literal"):
    #         a = Atom(atoms[i].getSyntax()+atoms[i+1].getSyntax(), types=["NOT AND"])
    #         a.literal = atoms[i+1].getSyntax()
    #         atoms.pop(i)
    #         atoms.pop(i)
    #         atoms.insert(i, a)
    #         continue
    #     if atoms[i].isType("Token +") and atoms[i+1].isType("Literal"):
    #         a = Atom(atoms[i].getSyntax()+atoms[i+1].getSyntax(), types=["AND"])
    #         a.literal = atoms[i+1].getSyntax()
    #         atoms.pop(i)
    #         atoms.pop(i)
    #         atoms.insert(i, a)
    #         continue

    #     i+=1

    # return(atoms)
        



def tokenPlusMinus(atom):
    string = atom.getSyntax()
    i = 0
    tokens = ["+","Token +","-","Token -"]
    out = []
    while i<len(string):
        b = 0
        while b<len(tokens):
            if string[i]==tokens[b]:
                e1 = string[0:i]
                e2 = string[i+1:]
                if e1<>"":
                    out.append(Atom(e1))
                out.append(Atom(tokens[b], types=[tokens[b+1], "plusminus"]))
                if e2<>"":
                    out.append(Atom(e2))
                i = len(string)
                b = len(tokens)
            b+=2
        i+=1

    if out<>[]:
        return(out)
    else:
        return(None)


def tokenWhiteSpace(atom):
    """Process whitespaces."""
    string = atom.getSyntax()
    i = string.find(" ")
    e1 = string[0:i]
    e2 = string[i+1:]
    out = []
    if i<>-1:
        if e1<>'':
            out.append(Atom(e1))
        out.append(Atom(" ", types=["Whitespace"]))
        if e2<>'':
            out.append(Atom(e2))
        return(out)
    else:
        return(None)


def tokenComma(atom):
    """Process commas."""
    string = atom.getSyntax()
    i = string.find(",")
    e1 = string[0:i]
    e2 = string[i+1:]
    out = []
    if i<>-1:
        if e1<>'':
            out.append(Atom(e1))
        out.append(Atom(",", types=["Comma"]))
        if e2<>'':
            out.append(Atom(e2))
        return(out)
    else:
        return(None)


def tokenBlock(atom):
    """Return splitted string based on closing parenthesses."""
    blocks=['(','Token (',')','Token )','[','Token [',']','Token ]','"','Token "','"','Token "']
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
            for b in range(0, len(blocks), 4):
                if string[i]==blocks[b]:
                    openItem = blocks[b]
                    openType = blocks[b+1]
                    closeItem = blocks[b+2]
                    closeType = blocks[b+3]
                    open+=1
                    begin = i
        i+=1

    if begin<>-1 and end<>-1:
        out = []
        e1 = string[0:begin]
        e2 = string[begin+1:end]
        e3 = string[end+1:]
        o = Atom(openItem, types=[openType,"Block"])
        c = Atom(closeItem, types=[closeType,"Block"])
        o.openingAtom = o.getHash()
        o.closingAtom = c.getHash()
        c.openingAtom = o.getHash()
        c.closingAtom = c.getHash()
        if e1<>'':
            out.append(Atom(e1))
        out.append(o)
        if e2<>'':
            if openItem==closeItem:
                out.append(Atom(e2, types=["Literal"]))
            else:
                out.append(Atom(e2))
        out.append(c)
        if e3<>'':
            out.append(Atom(e3))
        return(out)
    else:
        return(None)
 

def tokenDefault(atom):
    """Default parsing."""
    atom.addType("Literal")
    return([atom])


def synWhitespaces(atoms):
    """Process whitespaces."""
    i = 0
    while i<len(atoms):
        if atoms[i].isType("Whitespace") and i==0:
            atoms.pop(i)
            continue
        if atoms[i].isType("Whitespace") and i==len(atoms)-1:
            atoms.pop(i)
            continue
        if atoms[i].isType("Whitespace") and atoms[i+1].isType("Whitespace"):
            atoms.pop(i+1)
            continue

        i+=1


def synQuotes(atoms):
    """Erases quotes."""
    i = 0
    while i<len(atoms):
        if atoms[i].isType('Token "'):
            atoms.pop(i)
            continue
        i+=1


def synPlusMinus(atoms):
    """Erases consecutives +,- tokens."""
    i = 0
    while i<len(atoms):
        if atoms[i].isType("plusminus") and atoms[i+1].isType("plusminus"):
            atoms.pop(i+1)
            continue
        i+=1

    i = 0
    while i<len(atoms):
        if atoms[i].isType("plusminus") and atoms[i+1].isType("Whitespace"):
            atoms.pop(i+1)
            continue
        i+=1


def synEmptyBlocks(atoms):
    """Erases empty blocks."""
    i = 0
    changes = True
    while changes:
        changes = False
        while i<len(atoms):
            if atoms[i].isType("Token (") and atoms[i+1].isType("Token )"):
                atoms.pop(i)
                atoms.pop(i)
                changes = True
                continue
            i+=1
        i = 0
        while i<len(atoms):
            if atoms[i].isType("Token (") and atoms[i+1].isType("Whitespace") and atoms[i+2].isType("Token )"):
                atoms.pop(i)
                atoms.pop(i)
                atoms.pop(i)
                changes = True
                continue
            i+=1
        synWhitespaces(atoms)

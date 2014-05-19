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

                # import ipdb
                # ipdb.set_trace()

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
        



# def tokenPlusMinus(atom):
#     string = atom.getSyntax()
#     i = 0
#     tokens = ["+","Token +","-","Token -"]
#     out = []
#     while i<len(string):
#         b = 0
#         while b<len(tokens):
#             if string[i]==tokens[b]:
#                 e1 = string[0:i]
#                 e2 = string[i+1:]
#                 if e1<>"":
#                     out.append(Atom(e1))
#                 out.append(Atom(tokens[b], types=[tokens[b+1], "plusminus"]))
#                 if e2<>"":
#                     out.append(Atom(e2))
#                 i = len(string)
#                 b = len(tokens)
#             b+=2
#         i+=1

#     if out<>[]:
#         return(out)
#     else:
#         return(None)


# def tokenWhiteSpace(atom):
#     """Process whitespaces."""
#     string = atom.getSyntax()
#     i = string.find(" ")
#     e1 = string[0:i]
#     e2 = string[i+1:]
#     out = []
#     if i<>-1:
#         if e1<>'':
#             out.append(Atom(e1))
#         out.append(Atom(" ", types=["Whitespace"]))
#         if e2<>'':
#             out.append(Atom(e2))
#         return(out)
#     else:
#         return(None)


# def tokenComma(atom):
#     """Process commas."""
#     string = atom.getSyntax()
#     i = string.find(",")
#     e1 = string[0:i]
#     e2 = string[i+1:]
#     out = []
#     if i<>-1:
#         if e1<>'':
#             out.append(Atom(e1))
#         out.append(Atom(",", types=["Comma"]))
#         if e2<>'':
#             out.append(Atom(e2))
#         return(out)
#     else:
#         return(None)


# def tokenDoubleQuotes(atom):
#     """Literate context within double quotes."""
#     s = atom.getSyntax()
#     begin = -1
#     end = -1

#     i = 0
#     n = 0
#     while i<len(s):
#         if s[i]=='"':
#             n+=1
#             error = i
#         i+=1

#     if n%2==1:
#         raise ParserError("Syntax error: Mismatch double quotes at character "+str(error))

#     i = 0
#     while i<len(s):
#         if s[i]=='"' and begin==-1:
#             begin = i
#             i+=1
#             continue
#         if s[i]=='"' and begin<>-1:
#             end = i
#             out = []
#             e1 = s[0:begin]
#             e2 = s[end+1:]
#             openAtom = Atom('"', types=["Double Quotes", "Block"])
#             closeAtom = Atom('"', types=["Double Quotes", "Block"])
#             openAtom.setOpenAtom(openAtom.getHash())
#             openAtom.setCloseAtom(closeAtom.getHash())
#             closeAtom.setOpenAtom(openAtom.getHash())
#             closeAtom.setCloseAtom(closeAtom.getHash())
#             if e1<>"":
#                 out.append(Atom(e1))
#             out.append(openAtom)
#             out.append(Atom(s[begin+1:end], types=["Literal"]))
#             out.append(closeAtom)
#             if e2<>"":
#                 out.append(Atom(e2))
#             return(out)
#         i+=1
    
#     if (begin<>-1 and end==-1):
#         out = s[0:begin]+" "+s[begin+1:]
#         return([Atom(out)])
        
#     return(None)


# def tokenParenthesses(atom):
#     """Return splitted string based on closing parenthesses."""
#     opened = 0
#     begin = -1
#     end = -1
#     s = atom.getSyntax()
    
#     i = 0
#     nopen = 0
#     nclose = 0
#     while i<len(s):
#         if s[i]=="(":
#             nopen+=1
#             error = i
#         if s[i]==")":
#             nclose+=1
#             error = i
#         i+=1

#     if nopen<>nclose:
#         raise ParserError("Syntax error: Mismatch parenthesses at character "+str(error))

#     i = 0
#     while i<len(s):
#         if s[i]=="(":
#             if opened==0:
#                 begin = i
#             opened+=1
#         if s[i]==")":
#             opened-=1
#             if opened==0:
#                 end = i
#         if begin<>-1 and end<>-1:
#             out = []
#             e1 = s[0:begin]
#             e2 = s[end+1:]
#             openAtom = Atom('(', types=["Open Parenthesses", "Block"])
#             closeAtom = Atom(')', types=["Close Parenthesses", "Block"])
#             openAtom.setOpenAtom(openAtom.getHash())
#             openAtom.setCloseAtom(closeAtom.getHash())
#             closeAtom.setOpenAtom(openAtom.getHash())
#             closeAtom.setCloseAtom(closeAtom.getHash())
#             if e1<>"":
#                 out.append(Atom(e1))
#             out.append(openAtom)
#             out.append(Atom(s[begin+1:end]))
#             out.append(closeAtom)
#             if e2<>"":
#                 out.append(Atom(e2))
#             return(out)
#         i+=1

#     return(None)


# def tokenDefault(atom):
#      """Default parsing."""
#      atom.addType("Literal")
#      return([atom])


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


class ParserError(Exception):
    def __init__(self, error):
        Exception.__init__(self)
        self.error = error
        
    def __str__(self):
        return(self.error)

# coding=UTF8

import parser
import ipdb
reload(parser)

def parseSearchString(searchString):
    p = parser.Parser(searchString)
    a = p.parse([parser.tokenBlock, parser.tokenPlusMinus, parser.tokenComma, 
                 parser.tokenWhiteSpace, parser.tokenDefault], [parser.synQuotes, parser.synWhitespaces])
    p.str()
    return(a)


        
    




atoms = parseSearchString('   -+-     we  +++-    "jjerw kkekjr"')
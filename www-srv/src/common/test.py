# coding=UTF8

import parser
import ipdb
reload(parser)

def parseSearchString(searchString):
    p = parser.Parser(searchString)
    a = p.parse([{"token": "(",
                  "types": ["Open Parenthesses", "Block"]},
                 {"token": ")",
                  "types": ["Close Parenthesses", "Block"]},
                 {"token": " ",
                  "types": ["Whitespace"]},
                 {"token": '"',
                  "types": ["Double quote", "Block"]},
                 {"token": "+",
                  "types": ["Plus", "Plusminus"]},
                 {"token": "-",
                  "types": ["Minus", "Plusminus"]},
                 {"token": ",",
                  "types": ["Comma"]}], [])

# , parser.tokenPlusMinus, parser.tokenComma, 
#                  parser.tokenWhiteSpace, parser.tokenDefault], [])

# [parser.synQuotes, parser.synWhitespaces,
#                                                                 parser.synEmptyBlocks, 
#                                                                 parser.synPlusMinus])
    p.str()
    return(a)


        
    





atoms = parseSearchString('()"kkdjf jjjer "kkd,12,23"(ekekr)+++----"')

import searchparser
import ipdb
reload(searchparser)

p = searchparser.Parser('+a+b+e+g-e-w(-s-g)')
p.parse([searchparser.ruleBlock, searchparser.rulePlusMinus, searchparser.ruleDefault])
p.str()

from common.flux import Flux

flux = Flux()
inputfilename = "/Users/alasarr/Desktop/ultimosdatos.xlsx"
outputfilename = "/Users/alasarr/Desktop/calculus.xlsx"

flux.calculusFromXLSXToDatabase(inputfilename)
flux.updateRedisCache()
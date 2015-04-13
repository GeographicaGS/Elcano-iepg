from common.flux import Flux

flux = Flux()
inputfilename = "../../database/flux/year2014.xlsx"
#outputfilename = "/Users/alasarr/Desktop/calculus.xlsx"

flux.calculusFromXLSXToDatabase(inputfilename)
flux.updateRedisCache()
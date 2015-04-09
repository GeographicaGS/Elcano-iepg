from common.flux import Flux

flux = Flux()
inputfilename = "/Users/alasarr/Desktop/ultimosdatos.xlsx"
outputfilename = "/Users/alasarr/Desktop/calculus.xlsx"


#flux.calculusFromXLSXToXLSX(inputfilename,outputfilename)


flux.calculusFromXLSXToDatabase(inputfilename)
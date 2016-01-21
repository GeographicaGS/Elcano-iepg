from common.flux import Flux
inputfilename = "../../database/flux/year2016.xlsx"

flux = Flux()

#flux.calculusFromXLSXToWholeApplication(inputfilename)

outputfilename = "/Users/alasarr/Desktop/calculus.xlsx"
flux.calculusFromXLSXToXLSX(inputfilename,outputfilename)

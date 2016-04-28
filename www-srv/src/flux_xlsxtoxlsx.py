from common.flux import Flux
inputfilename = "data_calculus/year2015.xlsx"

flux = Flux()

#flux.calculusFromXLSXToWholeApplication(inputfilename)

outputfilename = "data_calculus/calculus2015.xlsx"
flux.calculusFromXLSXToXLSX(inputfilename,outputfilename)

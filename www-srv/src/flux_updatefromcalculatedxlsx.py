#!/usr/bin/python

"""
Loads a calculated XLSX into the database.

Usage:

flux_updatefromcalculatedxlsx.py calculus2015.xlxs [# of years in IEPG] [# of countries in IEPG]
    [# of years in IEPE] [# of countries in IEPE]

"""

import common.flux as flux
import sys

fileName = sys.argv[1]
nIepgYears = int(sys.argv[2])
nIepgCountries = int(sys.argv[3])
nIepeYears = int(sys.argv[4])
nIepeCountries = int(sys.argv[5])

print "Trying to import file %s with %s IEPG years, %s IEPG countries, %s IEPE years, and %s IEPE countries" % \
  (fileName, nIepgYears, nIepgCountries, nIepeYears, nIepeCountries)

f = flux.Flux()

o = f.loadCalculatedXlsxToDatabase(fileName, nIepgYears, nIepgCountries, nIepeYears, nIepeCountries)

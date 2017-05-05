#!/usr/bin/python

"""
Loads a calculated XLSX into the database.

Usage:

flux_updatefromcalculatedxlsx.py calculus2015.xlxs [# of years in IEPG] [# of countries in IEPG]
    [# of years in IEPE] [# of countries in IEPE]

"""

import argparse
import common.flux as flux


def run():
    
    descr = "Loads a calculated XLSX into the database"
    arg_parser = argparse.ArgumentParser(description=descr)
    
    arg_parser.add_argument('file_name', type=str, help='XLSX filename')
    arg_parser.add_argument('n_iepg_years', type=int, help='# of years in IEPG')
    arg_parser.add_argument('n_iepg_countries', type=int, help='# of countries in IEPG')
    arg_parser.add_argument('n_iepe_years', type=int, help='# of years in IEPE')
    arg_parser.add_argument('n_iepe_countries', type=int, help='# of countries in IEPE')
    
    args = arg_parser.parse_args()

    fileName = args.file_name
    nIepgYears = args.n_iepg_years
    nIepgCountries = args.n_iepg_countries
    nIepeYears = args.n_iepe_years
    nIepeCountries = args.n_iepe_countries

    print("Trying to import file %s with %s IEPG years, %s IEPG countries, %s IEPE years and %s IEPE countries" % \
      (fileName, nIepgYears, nIepgCountries, nIepeYears, nIepeCountries))

    f = flux.Flux()

    o = f.loadCalculatedXlsxToDatabase(fileName, nIepgYears, nIepgCountries, nIepeYears, nIepeCountries)


if __name__ == '__main__':
    run()
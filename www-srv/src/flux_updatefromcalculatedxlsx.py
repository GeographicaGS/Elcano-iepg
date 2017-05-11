#!/usr/bin/python

"""
Loads a calculated XLSX into the database.

usage: flux_updatefromcalculatedxlsx.py [-h] [-p]
                                        file_name n_iepg_years
                                        n_iepg_countries n_iepe_years
                                        n_iepe_countries

Loads a calculated XLSX into the database

positional arguments:
  file_name             XLSX filename
  n_iepg_years          # of years in IEPG
  n_iepg_countries      # of countries in IEPG
  n_iepe_years          # of years in IEPE
  n_iepe_countries      # of countries in IEPE

optional arguments:
  -h, --help            show this help message and exit
  -p, --print_nc        print new countries

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
    arg_parser.add_argument('-p', '--print_nc',  action="store_true", help='print new countries')
    
    args = arg_parser.parse_args()

    fileName = args.file_name
    nIepgYears = args.n_iepg_years
    nIepgCountries = args.n_iepg_countries
    nIepeYears = args.n_iepe_years
    nIepeCountries = args.n_iepe_countries
    printNewCountries = args.print_nc

    print("Trying to import file %s with %s IEPG years, %s IEPG countries, %s IEPE years and %s IEPE countries" % \
      (fileName, nIepgYears, nIepgCountries, nIepeYears, nIepeCountries))

    f = flux.Flux()

    o = f.loadCalculatedXlsxToDatabase(fileName, nIepgYears, nIepgCountries, nIepeYears, 
        nIepeCountries, printNewCountries=printNewCountries)
    
    f.updateRedisCache()
    

if __name__ == '__main__':
    run()
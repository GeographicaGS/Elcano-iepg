# coding=UTF8
import common.arrayops as arrayops
import flux_lib.data.excel_utils as excel_utils, flux_lib.data.core as core
import ast
import numpy as np
from model.fluxmodel import FluxModel
from model.iepgdatamodel import IepgDataModel
from maplex.maplexmodel import MaplexModel
from varengine import varengine as varengine
from common import const as const
from common import config
import redis
from pythonhelpers.database import datacache
from maplex import maplex
import copy
from model.base.PostgreSQL.PostgreSQLModel import PostgreSQLModel

class Flux(object):

    # HERE STARTS THE CODE TO IMPORT THE NEW CALCULATED XLSX
    # ---
    # For the new XLSX

    # This lists are the names of tabs found in the XLSX

    __iepgSheetsNames = [
        "Energy IEPG", "Primary Goods IEPG", "Manufactures IEPG", "Services IEPG",
        "Investments IEPG", "Troops IEPG", "Military Equipment IEPG", "Migrations IEPG",
        "Tourism IEPG", "Sports IEPG", "Culture IEPG", "Information IEPG",
        "Technology IEPG", "Science IEPG", "Education IEPG", "Development Coop. IEPG",
        "Economic IEPG", "Military IEPG", "Soft IEPG", "IEPG",

        # "Energy IEPG QUOTE", "Primary Goods IEPG QUOTE", "Manufactures IEPG QUOTE", "Services IEPG QUOTE",
        # "Investments IEPG QUOTE", "Troops IEPG QUOTE", "Military Equipment IEPG QUOTE",
        # "Migrations IEPG QUOTE", "Tourism IEPG QUOTE", "Sports IEPG QUOTE",
        # "Culture IEPG QUOTE", "Information IEPG QUOTE", "Technology IEPG QUOTE",
        # "Science IEPG QUOTE", "Education IEPG QUOTE", "Development Coop. IEPG QUOTE",
        "Economic IEPG QUOTE", "Military IEPG QUOTE", "Soft IEPG QUOTE",
        "IEPG IEPG QUOTE",

        "Energy IEPG CONTRIBUTION", "Primary Goods IEPG CONTRIBUTION",
        "Manufactures IEPG CONTRIBUTION", "Services IEPG CONTRIBUTION",
        "Investments IEPG CONTRIBUTION", "Troops IEPG CONTRIBUTION",
        "Military E. IEPG CONTRIBUTION", "Migrations IEPG CONTRIBUTION",
        "Tourism IEPG CONTRIBUTION", "Sports IEPG CONTRIBUTION", "Culture IEPG CONTRIBUTION",
        "Information IEPG CONTRIBUTION", "Technology IEPG CONTRIBUTION",
        "Science IEPG CONTRIBUTION", "Education IEPG CONTRIBUTION",
        "Devel. C. IEPG CONTRIBUTION", "Economic IEPG CONTRIBUTION",
        "Military IEPG CONTRIBUTION", "Soft IEPG CONTRIBUTION"]

    __iepeSheetsNames = [
        "Energy IEPE", "Primary Goods IEPE", "Manufactures IEPE", "Services IEPE",
        "Investments IEPE", "Troops IEPE", "Military Equipment IEPE", "Migrations IEPE",
        "Tourism IEPE", "Sports IEPE", "Culture IEPE", "Information IEPE",
        "Technology IEPE", "Science IEPE", "Education IEPE", "Development Coop. IEPE",
        "Economic IEPE", "Military IEPE", "Soft IEPE", "IEPE",

        # "Energy IEPE QUOTE", "Primary Goods IEPE QUOTE",
        # "Manufactures IEPE QUOTE", "Services IEPE QUOTE",
        # "Investments IEPE QUOTE", "Troops IEPE QUOTE",
        # "Migrations IEPE QUOTE", "Tourism IEPE QUOTE", "Sports IEPE QUOTE",
        # "Culture IEPE QUOTE", "Information IEPE QUOTE", "Technology IEPE QUOTE",
        # "Science IEPE QUOTE", "Education IEPE QUOTE", "Development Coop. IEPE QUOTE",
        "Economic IEPE QUOTE", "Military IEPE QUOTE", "Soft IEPE QUOTE",
        "IEPE IEPE QUOTE",

        "Energy IEPE CONTRIBUTION", "Primary Goods IEPE CONTRIBUTION",
        "Manufactures IEPE CONTRIBUTION", "Services IEPE CONTRIBUTION",
        "Investments IEPE CONTRIBUTION", "Troops IEPE CONTRIBUTION",
        "Military E. IEPE CONTRIBUTION", "Migrations IEPE CONTRIBUTION",
        "Tourism IEPE CONTRIBUTION", "Sports IEPE CONTRIBUTION", "Culture IEPE CONTRIBUTION",
        "Information IEPE CONTRIBUTION", "Technology IEPE CONTRIBUTION",
        "Science IEPE CONTRIBUTION", "Education IEPE CONTRIBUTION",
        "Devel. C. IEPE CONTRIBUTION", "Economic IEPE CONTRIBUTION",
        "Military IEPE CONTRIBUTION", "Soft IEPE CONTRIBUTION"]

    # This are used in the processing of the new calculated XLSX
    IEPGData = None
    IEPEData = None


    # For the new XLSX, gets an XLSX cell and output a intelligible Python value
    def getCellValue(self, cell):
        if cell.ctype==0:
            return None
        else:
            return cell.value


    # Reads the XLSX
    def readComputedXLSX(self, filename, iepgYearsN, iepgCountriesN,
             iepeYearsN, iepeCountriesN):
        """
        Reads the whole data set.

        - filename: sheet file name
        - iepgYearsN: number of years in IEPG
        - iepgCountriesN: number of countries in IEPG
        - iepeYearsN: number of years in IEPE
        - iepeCountriesN: number of countries in IEPE
        """

        self.IEPGData = dict()
        self.IEPEData = dict()

        for i in self.__iepgSheetsNames:
            self.IEPGData[i] = self.__readSheet(filename, i, iepgYearsN+1, iepgCountriesN+1)

        for i in self.__iepeSheetsNames:
            self.IEPEData[i] = self.__readSheet(filename, i, iepeYearsN+1, iepeCountriesN+1)


    # This is the importer function of the calculated XLSX to the database

    def loadCalculatedXlsxToDatabase(self, filename, iepgYearsN, iepgCountriesN,
                                     iepeYearsN, iepeCountriesN):

        print "Reading XLSX..."

        self.readComputedXLSX(filename, iepgYearsN, iepgCountriesN,
                  iepeYearsN, iepeCountriesN)

        print "Finished reading XLSX."

        # Access to database objects
        pg = PostgreSQLModel()
        fm = FluxModel()

        # Backup old schema and drop all data in the production one
        fm.prepareSchemaIEPGDataRedux()

        # Write IEPG data

        print "Processing IEPG..."
        print "Reading IEPG years and countries..."
        
        # Get countries and codes from database (master table)
        q = pg.query("""
            select xlsx_column_name, iso_3166_1_2_code
            from iepg_data_redux.master_country;""")
        
        codes_all = q.result()
        
        countries_db = [dc['xlsx_column_name'] for dc in codes_all]
        
        ctrys_codes_db = dict((i['xlsx_column_name'], i['iso_3166_1_2_code']) for i in codes_all)

        # Get IEPG years and countries
        years = [int(year.value) for year in self.IEPGData["Energy IEPG"][0][1:]]
        
        countries = [str(ctry[0].value.encode('UTF-8')) for ctry in self.IEPGData["Energy IEPG"][1:]]
        
        countries_errors = set(countries).difference(set(countries_db))
        
        if len(countries_errors) > 0:
            print "Error: You must repair this countries in XLS before execute data load: %s" % countries_errors
            return
            
        codes = [ctrys_codes_db[ct] for ct in countries]

        print "Finished reading IEPG years and countries. %s countries processed." % len(codes)

        print "Generating IEPG data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code": codes[c],
                    "date_in": '%s-01-01' % years[y],
                    "date_out": '%s-12-31' % years[y],
                    "energy": self.getCellValue(self.IEPGData["Energy IEPG"][c+1][y+1]),
                    "primary_goods": self.getCellValue(self.IEPGData["Primary Goods IEPG"][c+1][y+1]),
                    "manufactures": self.getCellValue(self.IEPGData["Manufactures IEPG"][c+1][y+1]),
                    "services": self.getCellValue(self.IEPGData["Services IEPG"][c+1][y+1]),
                    "investments": self.getCellValue(self.IEPGData["Investments IEPG"][c+1][y+1]),
                    "troops": self.getCellValue(self.IEPGData["Troops IEPG"][c+1][y+1]),
                    "military_equipment": self.getCellValue(self.IEPGData["Military Equipment IEPG"][c+1][y+1]),
                    "migrations": self.getCellValue(self.IEPGData["Migrations IEPG"][c+1][y+1]),
                    "tourism": self.getCellValue(self.IEPGData["Tourism IEPG"][c+1][y+1]),
                    "sports": self.getCellValue(self.IEPGData["Sports IEPG"][c+1][y+1]),
                    "culture": self.getCellValue(self.IEPGData["Culture IEPG"][c+1][y+1]),
                    "information": self.getCellValue(self.IEPGData["Information IEPG"][c+1][y+1]),
                    "technology": self.getCellValue(self.IEPGData["Technology IEPG"][c+1][y+1]),
                    "science": self.getCellValue(self.IEPGData["Science IEPG"][c+1][y+1]),
                    "education": self.getCellValue(self.IEPGData["Education IEPG"][c+1][y+1]),
                    "cooperation": self.getCellValue(self.IEPGData["Development Coop. IEPG"][c+1][y+1]),
                    "economic_presence": self.getCellValue(self.IEPGData["Economic IEPG"][c+1][y+1]),
                    "military_presence": self.getCellValue(self.IEPGData["Military IEPG"][c+1][y+1]),
                    "soft_presence": self.getCellValue(self.IEPGData["Soft IEPG"][c+1][y+1]),
                    "iepg": self.getCellValue(self.IEPGData["IEPG"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPG data."

        print "Writing IEPG data to database..."

        fm.addDataIEPG(data)

        print "Finished writing IEPG data to database."


        # IEPG quota data

        print "Generating IEPG quota data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code": codes[c],
                    "date_in": "%s-01-01" % years[y],
                    "date_out": "%s-12-31" % years[y],
                    "economic_quota": self.getCellValue(self.IEPGData["Economic IEPG QUOTE"][c+1][y+1]),
                    "military_quota": self.getCellValue(self.IEPGData["Military IEPG QUOTE"][c+1][y+1]),
                    "soft_quota": self.getCellValue(self.IEPGData["Soft IEPG QUOTE"][c+1][y+1]),
                    "global_quota": self.getCellValue(self.IEPGData["IEPG IEPG QUOTE"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPG quota data."

        print "Writing IEPG quote data to database..."

        fm.addDataIEPGQuote(data)

        print "Finished writing IEPG quote data to database."


        # IEPG contribution data

        print "Generating IEPG contribution data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code" : codes[c],
                    "date_in": '%s-01-01' % years[y],
                    "date_out": '%s-12-31' % years[y],
                    "energy" : self.getCellValue(self.IEPGData["Energy IEPG CONTRIBUTION"][c+1][y+1]),
                    "primary_goods" : self.getCellValue(self.IEPGData["Primary Goods IEPG CONTRIBUTION"][c+1][y+1]),
                    "manufactures" : self.getCellValue(self.IEPGData["Manufactures IEPG CONTRIBUTION"][c+1][y+1]),
                    "services" : self.getCellValue(self.IEPGData["Services IEPG CONTRIBUTION"][c+1][y+1]),
                    "investments" : self.getCellValue(self.IEPGData["Investments IEPG CONTRIBUTION"][c+1][y+1]),
                    "troops" : self.getCellValue(self.IEPGData["Troops IEPG CONTRIBUTION"][c+1][y+1]),
                    "military_equipment" : self.getCellValue(self.IEPGData["Military E. IEPG CONTRIBUTION"][c+1][y+1]),
                    "migrations" : self.getCellValue(self.IEPGData["Migrations IEPG CONTRIBUTION"][c+1][y+1]),
                    "tourism" : self.getCellValue(self.IEPGData["Tourism IEPG CONTRIBUTION"][c+1][y+1]),
                    "sports" : self.getCellValue(self.IEPGData["Sports IEPG CONTRIBUTION"][c+1][y+1]),
                    "culture" : self.getCellValue(self.IEPGData["Culture IEPG CONTRIBUTION"][c+1][y+1]),
                    "information" : self.getCellValue(self.IEPGData["Information IEPG CONTRIBUTION"][c+1][y+1]),
                    "technology" : self.getCellValue(self.IEPGData["Technology IEPG CONTRIBUTION"][c+1][y+1]),
                    "science" : self.getCellValue(self.IEPGData["Science IEPG CONTRIBUTION"][c+1][y+1]),
                    "education" : self.getCellValue(self.IEPGData["Education IEPG CONTRIBUTION"][c+1][y+1]),
                    "cooperation" : self.getCellValue(self.IEPGData["Devel. C. IEPG CONTRIBUTION"][c+1][y+1]),
                    "economic_contribution" : self.getCellValue(self.IEPGData["Economic IEPG CONTRIBUTION"][c+1][y+1]),
                    "military_contribution" : self.getCellValue(self.IEPGData["Military IEPG CONTRIBUTION"][c+1][y+1]),
                    "soft_contribution" : self.getCellValue(self.IEPGData["Soft IEPG CONTRIBUTION"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPG contribution data."

        print "Writing IEPG contribution data to database..."

        fm.addDataIEPGContribituon(data)

        print "Finished writing IEPG contribution to database."

        print "IEPG added successfully"


        # Calculus IEPE

        years = []
        codes = []
        countries = []

        print "Processing IEPE..."
        print "Reading IEPE years and countries..."

        # Get IEPE years and countries
        
        years = [int(year.value) for year in self.IEPEData["Energy IEPE"][0][1:]]
        
        countries = [str(ctry[0].value.encode('UTF-8')) for ctry in self.IEPEData["Energy IEPE"][1:]]
        
        countries_errors = set(countries).difference(set(countries_db))
        
        if len(countries_errors) > 0:
            print "Error: You must repair this countries in XLS before execute data load: %s" % countries_errors
            return
            
        codes = [ctrys_codes_db[ct] for ct in countries]

        print "Finished reading IEPE years and countries. %s countries processed." % len(codes)

        print "Generating IEPE data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code": codes[c],
                    "date_in": '%s-01-01' % years[y],
                    "date_out": '%s-12-31' % years[y],
                    "energy": self.getCellValue(self.IEPEData["Energy IEPE"][c+1][y+1]),
                    "primary_goods": self.getCellValue(self.IEPEData["Primary Goods IEPE"][c+1][y+1]),
                    "manufactures": self.getCellValue(self.IEPEData["Manufactures IEPE"][c+1][y+1]),
                    "services": self.getCellValue(self.IEPEData["Services IEPE"][c+1][y+1]),
                    "investments": self.getCellValue(self.IEPEData["Investments IEPE"][c+1][y+1]),
                    "troops": self.getCellValue(self.IEPEData["Troops IEPE"][c+1][y+1]),
                    "military_equipment": self.getCellValue(self.IEPEData["Military Equipment IEPE"][c+1][y+1]),
                    "migrations": self.getCellValue(self.IEPEData["Migrations IEPE"][c+1][y+1]),
                    "tourism": self.getCellValue(self.IEPEData["Tourism IEPE"][c+1][y+1]),
                    "sports": self.getCellValue(self.IEPEData["Sports IEPE"][c+1][y+1]),
                    "culture": self.getCellValue(self.IEPEData["Culture IEPE"][c+1][y+1]),
                    "information": self.getCellValue(self.IEPEData["Information IEPE"][c+1][y+1]),
                    "technology": self.getCellValue(self.IEPEData["Technology IEPE"][c+1][y+1]),
                    "science": self.getCellValue(self.IEPEData["Science IEPE"][c+1][y+1]),
                    "education": self.getCellValue(self.IEPEData["Education IEPE"][c+1][y+1]),
                    "cooperation": self.getCellValue(self.IEPEData["Development Coop. IEPE"][c+1][y+1]),
                    "economic_presence": self.getCellValue(self.IEPEData["Economic IEPE"][c+1][y+1]),
                    "military_presence": self.getCellValue(self.IEPEData["Military IEPE"][c+1][y+1]),
                    "soft_presence": self.getCellValue(self.IEPEData["Soft IEPE"][c+1][y+1]),
                    "iepe": self.getCellValue(self.IEPEData["IEPE"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPE data."

        print "Writing IEPE data to database..."

        fm.addDataIEPE(data)

        print "Finished writing IEPE data to database."


        # IEPE quota data

        print "Generating IEPE quota data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code": codes[c],
                    "date_in": "%s-01-01" % years[y],
                    "date_out": "%s-12-31" % years[y],
                    "economic_quota": self.getCellValue(self.IEPEData["Economic IEPE QUOTE"][c+1][y+1]),
                    "soft_quota": self.getCellValue(self.IEPEData["Soft IEPE QUOTE"][c+1][y+1]),
                    "global_quota": self.getCellValue(self.IEPEData["IEPE IEPE QUOTE"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPE quota data."

        print "Writing IEPE quote data to database..."

        fm.addDataIEPEQuote(data)

        print "Finished writing IEPE quote data to database."


        # IEPE contribution data

        print "Generating IEPE contribution data..."

        data = []

        for y in range(0, len(years)):
            for c in range(0, len(codes)):
                d = {
                    "code" : codes[c],
                    "date_in": '%s-01-01' % years[y],
                    "date_out": '%s-12-31' % years[y],
                    "energy" : self.getCellValue(self.IEPEData["Energy IEPE CONTRIBUTION"][c+1][y+1]),
                    "primary_goods" : self.getCellValue(self.IEPEData["Primary Goods IEPE CONTRIBUTION"][c+1][y+1]),
                    "manufactures" : self.getCellValue(self.IEPEData["Manufactures IEPE CONTRIBUTION"][c+1][y+1]),
                    "services" : self.getCellValue(self.IEPEData["Services IEPE CONTRIBUTION"][c+1][y+1]),
                    "investments" : self.getCellValue(self.IEPEData["Investments IEPE CONTRIBUTION"][c+1][y+1]),
                    "troops" : self.getCellValue(self.IEPEData["Troops IEPE CONTRIBUTION"][c+1][y+1]),
                    "military_equipment" : self.getCellValue(self.IEPEData["Military E. IEPE CONTRIBUTION"][c+1][y+1]),
                    "migrations" : self.getCellValue(self.IEPEData["Migrations IEPE CONTRIBUTION"][c+1][y+1]),
                    "tourism" : self.getCellValue(self.IEPEData["Tourism IEPE CONTRIBUTION"][c+1][y+1]),
                    "sports" : self.getCellValue(self.IEPEData["Sports IEPE CONTRIBUTION"][c+1][y+1]),
                    "culture" : self.getCellValue(self.IEPEData["Culture IEPE CONTRIBUTION"][c+1][y+1]),
                    "information" : self.getCellValue(self.IEPEData["Information IEPE CONTRIBUTION"][c+1][y+1]),
                    "technology" : self.getCellValue(self.IEPEData["Technology IEPE CONTRIBUTION"][c+1][y+1]),
                    "science" : self.getCellValue(self.IEPEData["Science IEPE CONTRIBUTION"][c+1][y+1]),
                    "education" : self.getCellValue(self.IEPEData["Education IEPE CONTRIBUTION"][c+1][y+1]),
                    "cooperation" : self.getCellValue(self.IEPEData["Devel. C. IEPE CONTRIBUTION"][c+1][y+1]),
                    "economic_contribution" : self.getCellValue(self.IEPEData["Economic IEPE CONTRIBUTION"][c+1][y+1]),
                    "military_contribution" : self.getCellValue(self.IEPEData["Military IEPE CONTRIBUTION"][c+1][y+1]),
                    "soft_contribution" : self.getCellValue(self.IEPEData["Soft IEPE CONTRIBUTION"][c+1][y+1])
                }

                data.append(d)

        print "Finished generating IEPE contribution data."

        print "Writing IEPE contribution data to database..."

        fm.addDataIEPEContribituon(data)

        print "Finished writing IEPE contribution to database."

        print "IEPE added successfully"


    ### HERE ENDS THE PROCESSING OF THE NEW, FULLY CALCULATED XSLX





    ### HERE STARTS OLD METHODS OF IEPG ENGINE

    __book = None
    __IEPGData = None
    __IEPEData = None
    __environment = dict()
    __variables = []
    __totalCountriesEu = []
    __euDataYears = None
    __missingEuCountries = None
    __euDataYearsStr = None
    __refYear = None


    def calculusFromXLSXToXLSX(self,infilename,outfilename):
        self.__createBookFromXLSX(infilename)
        self.__calculateIEPG()
        self.__calculateIEPE()
        self.__writeToXLSX(outfilename)

    def calculusFromXLSXToDatabase(self,infilename):
        self.__createBookFromXLSX(infilename)
        self.__calculateIEPG()
        self.__calculateIEPE()
        self.__writeToDatabase()

    def calculusFromXLSXToWholeApplication(self,infilename):
        self.calculusFromXLSXToDatabase(infilename)
        self.updateRedisCache()


    def __readSheet(self, filename, sheet, columns, rows):
        """
        Returns an array of rows and columns with contents of a sheet.

        - filename: XLSX file name
        - sheet: sheet name
        - columns: number of columns in sheet
        - rows: number of rows in sheet
        """
        self.__book = excel_utils.ExcelReader(filename, decimalSeparator=",")

        a, b = self.__book.rowReader(sheet, startCell=(0,0), dimensions=(rows, columns))

        return a


    def __createBookFromXLSX(self,filename):
        # Start the calculus
        self.__book = excel_utils.ExcelReader(filename,
                                       decimalSeparator=",")

        # prepare context variables
        #years = []
        #geoentities = []

        # Read metadata
        environmentEx,lastRowEnv = self.__book.rowReader("Metadata", startCell=(1,0), endMark="")
        variablesEx,lastRowVar = self.__book.rowReader("Metadata", startCell=(lastRowEnv+1,0), startMark="Filiation")

        environmentEx.pop(len(environmentEx)-1)
        variablesEx.pop(0)

        # Read configuration variables
        for i in environmentEx:
            self.__environment[i[0].value] = ast.literal_eval(unicode(i[1].value))

        self.__refYear = str(self.__environment["REFERENCE_YEAR"])

        # Read variables
        for i in variablesEx:
            self.__variables.append(core.Variable(i[0].value,
                                           getattr(core, i[4].value),
                                           getattr(np, i[5].value),
                                           self.__environment["LANGUAGE_CODES"],
                                           ast.literal_eval(i[1].value) if i[1].value!="" else None,
                                           ast.literal_eval(i[2].value) if i[2].value!="" else None,
                                           ast.literal_eval(i[3].value) if i[3].value!="" else None,
                                           ast.literal_eval(i[6].value) if i[6].value!="" else None))

        print self.__variables;

        # Process EUROPEAN_UNION environment variable to find missing countries in each year
        self.__totalCountriesEu = []
        [self.__totalCountriesEu.extend(i) for i in self.__environment["EUROPEAN_UNION"].values()]
        self.__totalCountriesEu = list(set(self.__totalCountriesEu))

        self.__missingEuCountries = {}
        for k,v in self.__environment["EUROPEAN_UNION"].iteritems():
            self.__missingEuCountries[k] = arrayops.arraySubstraction(self.__totalCountriesEu, v)

        # Also total years of EU data are encoded from the number of keys of EUROPEAN_UNION
        self.__euDataYears = len(self.__environment["EUROPEAN_UNION"].keys())
        self.__euDataYearsStr = [str(i) for i in self.__missingEuCountries.keys()]

        return self.__book


    def __calculateIEPG(self):

        # TODO: tenemos que hacer funcionar esto con los datos del 2014 para ver qué arroja esta función y simularlo

        if not self.__book:
            raise Exception('Book need to be created')


        # Prepare variables for IEPG calculus, excluding EU
        # All data for IEPG countries are loaded in data, but
        # not any EU IEPG-specific data
        data = core.GeoVariableArray()

        [data.merge(self.__book.readGeoVariableArray(".".join(x.filiation))) for x
         in self.__variables if x.filiation[0]=="IEPG"]

        # Get indexes of european countries for not to rely on GeoVariableArray indexing, and also european years
        #totalCountriesEuIdx = []
        #[totalCountriesEuIdx.append(data.geoentity.index(i)) for i in totalCountriesEu]

        # NOT SURE
        #euDataYearsIdx = []
        # for i in euDataYearsStr:
        #     for t in data.time:
        #         if str(t.start.year)==i:
        #             euDataYearsIdx.append(data.time.index(t))

        # missingEuCountriesIdx = {}
        # t = 0
        # for k,v in missingEuCountries.iteritems():
        #     missing = []
        #     [missing.append(data.geoentity.index(i)) for i in v]
        #     missingEuCountriesIdx[euDataYearsIdx[t]] = missing
        #     t+=1


        # Prepare and add data for EU
        data.addGeoentity(u"European Union")
        # Get the index of the EU for slicing
        euIndex = data.geoentity.index(u"European Union")

        dolarEx = np.array(self.__environment["EURO_DOLAR_ER"])

        # Initial load of EU data
        vectorVar = ["IEPG_EU.Economic.Energy",
                     "IEPG_EU.Economic.FLA",
                     "IEPG_EU.Economic.BVT",
                     "IEPG_EU.Economic.CMI",
                     "IEPG_EU.Economic.AVO",
                     "IEPG_EU.Economic.CHM",
                     "IEPG_EU.Economic.Manufactures",
                     "IEPG_EU.Economic.Machinery",
                     "IEPG_EU.Economic.MMA",
                     "IEPG_EU.Economic.NFM",
                     "IEPG_EU.Economic.PSP",
                     "IEPG_EU.Economic.NMG",
                     "IEPG_EU.Economic.Services",
                     "IEPG_EU.Economic.Investments",
                     "IEPG_EU.Soft.Culture",
                     "IEPG_EU.Soft.Information.News",
                     "IEPG_EU.Soft.Information.Intern"]
        tableVar = ["IEPG_EU.Military.Troops",
                    "IEPG_EU.Soft.InmigrationTotal",
                    "IEPG_EU.Soft.InmigrationIntra",
                    "IEPG_EU.Soft.Tourism",
                    "IEPG_EU.Soft.TechnologyTotal",
                    "IEPG_EU.Soft.TechnologyIntra",
                    "IEPG_EU.Soft.EducationTotal",
                    "IEPG_EU.Soft.EducationIntra"]

        euVector = core.GeoVariableArray()
        euTable = core.GeoVariableArray()
        [euVector.merge(self.__book.readGeoVariableArray(x)) for x in vectorVar]
        [euTable.merge(self.__book.readGeoVariableArray(x)) for x in tableVar]

        # EU IEPG Energy, loads EU data into "data" for IEPG calculation
        da = euVector.select(0,
                             None,
                             "IEPG_EU.Economic.Energy"
                         )*np.repeat(dolarEx,1,axis=0).reshape(self.__euDataYears,1)/1000

        #print da
        #print da.shape
        #print da[0,:,0]

        data[u"European Union",3:,"IEPG.Economic.Energy"]=da[0,:,0]

        # EU IEPG Culture, loads EU data into "data" for IEPG calculation
        da = euVector.select(0, None, ["IEPG_EU.Soft.Culture","IEPG_EU.Economic.Services"])* \
            np.repeat(dolarEx, 1, axis=0).reshape(self.__euDataYears,1)*1000000
        data[u"European Union",3:,"IEPG.Soft.Culture"]=da[0,:,0]

        # EU IEPG Services, loads EU data into "data" for IEPG calculation
        da = euVector.select(0, None, "IEPG_EU.Economic.Services") * np.repeat(dolarEx,1,axis=0).reshape(self.__euDataYears,1)
        data[u"European Union",3:,"IEPG.Economic.Services"]=da[0,:,0]

        # EU IEPG Investments, loads EU data into "data" for IEPG calculation
        da = euVector.select(0,
                             None,
                             [
                              "IEPG_EU.Economic.Investments"]
                         )*np.repeat(dolarEx,1,axis=0).reshape(self.__euDataYears,1)

        data[u"European Union",3:,"IEPG.Economic.Investments"]=da[0,:,0]

        # EU IEPG Primary Goods, loads EU data into "data" for IEPG calculation

        primaryG = np.nansum(euVector.select(
            None,
            None,
            ["IEPG_EU.Economic.FLA",
             "IEPG_EU.Economic.BVT",
             "IEPG_EU.Economic.CMI",
             "IEPG_EU.Economic.AVO",
             "IEPG_EU.Economic.NFM",
             "IEPG_EU.Economic.PSP",
             "IEPG_EU.Economic.NMG"]), axis=2)*dolarEx/1000

        data[u"European Union",3:,"IEPG.Economic.PrimaryGoods"]=primaryG

        # EU IEPG Manufactures, loads EU data into "data" for IEPG calculation
        man = np.nansum(euVector.select(None,None,
                                        ["IEPG_EU.Economic.CHM",
                                         "IEPG_EU.Economic.Manufactures",
                                         "IEPG_EU.Economic.Machinery",
                                         "IEPG_EU.Economic.MMA"]), axis=2) - \
            np.nansum(euVector.select(
                None,
                None,
                ["IEPG_EU.Economic.NFM",
                 "IEPG_EU.Economic.PSP"]), axis=2)

        man = man*np.array(dolarEx)/1000

        data[u"European Union",3:,"IEPG.Economic.Manufactures"]=man


        # IEPG EU Troops & military equipment, Science, and Cooperation
        data[u"European Union",3:,"IEPG.Military.Troops"] = np.nansum(euTable[:,:,"IEPG_EU.Military.Troops"], axis=0).flatten()

        # europeanIndices = [0,6,8,10,14,17,18,21,22,23,25,27,28,29,30,35,38,42,43,44,46,51,54,55,57,58,59,63]
        # bulgariaIndex = 3
        # croatiaIndex = 5
        # romaniaIndex = 26
        variablesFromGlobal = ["IEPG.Military.Support.AircraftC",
                               "IEPG.Military.Support.Amphibius",
                               "IEPG.Military.Support.Frigates",
                               "IEPG.Military.Support.Destroyer",
                               "IEPG.Military.Support.Cruisers",
                               "IEPG.Military.Support.Submarine",
                               "IEPG.Military.Support.Aeroplane",
                               "IEPG.Military.Support.Airtanker",
                               "IEPG.Soft.Science",
                               "IEPG.Soft.DevelopmentC"]


        for x in variablesFromGlobal:

            da = data.getSubset(self.__totalCountriesEu,self.__euDataYearsStr,x)
            da.sort()
            da = self.__clearMissingEuCountries(da, self.__missingEuCountries)
            da = np.nansum(da.data, axis=0).flatten()
            data[u"European Union",3:,x] = da

        # Inmigration
        data[u"European Union",3:,"IEPG.Soft.Migrations"] = np.nansum(
            (euTable[:,:,"IEPG_EU.Soft.InmigrationTotal"] - \
             euTable[:,:,"IEPG_EU.Soft.InmigrationIntra"]), axis=0).flatten()

        # Tourism
        data[u"European Union",3:,"IEPG.Soft.Tourism"] = np.nansum(
            euTable[:,:,"IEPG_EU.Soft.Tourism"], axis=0).flatten()/1000

        # Information
        data[u"European Union",3:,"IEPG.Soft.Information.News"] = euVector[0,:,"IEPG_EU.Soft.Information.News"]
        data[u"European Union",3:,"IEPG.Soft.Information.Internet"] = euVector[0,:,"IEPG_EU.Soft.Information.Intern"]

        #print "News: ", data[u"European Union",3:,"IEPG.Soft.Information.News"]
        #print "Internet: ", data[u"European Union",3:,"IEPG.Soft.Information.Internet"]

        # Technology
        data[u"European Union",3:,"IEPG.Soft.Technology"] = np.nansum(
            (euTable[:,:,"IEPG_EU.Soft.TechnologyTotal"] - \
             euTable[:,:,"IEPG_EU.Soft.TechnologyIntra"]), axis=0).flatten()

        # Education
        data[u"European Union",3:,"IEPG.Soft.Education"] = np.nansum(
            (euTable[:,:,"IEPG_EU.Soft.EducationTotal"] - \
             euTable[:,:,"IEPG_EU.Soft.EducationIntra"]), axis=0).flatten()


        shape = data.shape

        # Normal calculus
        normal = ["IEPG.Economic.Energy",
                  "IEPG.Economic.PrimaryGoods",
                  "IEPG.Economic.Manufactures",
                  "IEPG.Economic.Services",
                  "IEPG.Economic.Investments",
                  "IEPG.Military.Troops",
                  "IEPG.Soft.Migrations",
                  "IEPG.Soft.Tourism",
                  "IEPG.Soft.Culture",
                  "IEPG.Soft.Technology",
                  "IEPG.Soft.Science",
                  "IEPG.Soft.Education",
                  "IEPG.Soft.DevelopmentC"]

        for i in normal:
            #print i
            #print data[u"European Union",3:,i]
            # print data[u"United States of America",self.__refYear,i]
            # print "max: ", np.nanmax(data[:euIndex,self.__refYear,i])

            if i+"Est" in data.variable:
                d = np.fmax(data[:,:,i]*1000.0/np.nanmax(data[:euIndex,self.__refYear,i]),
                            data[:,:,i+"Est"])
            else:
                d = data[:,:,i]*1000.0/np.nanmax(data[:euIndex,self.__refYear,i])

            data.addVariable(i+"_IEPG", data=d)

        #print data[u"European Union",3:,"IEPG.Economic.Services_IEPG"]

        # Information calculus
        refYearIndex = data.getTimeIndex(self.__refYear)[0]

        #print "Max News: ",np.nanmax(data[:euIndex,self.__refYear,"IEPG.Soft.Information.News"])
        infointernet = data[:,:,"IEPG.Soft.Information.Internet"]*1000.0/np.nanmax(data[:euIndex,self.__refYear,"IEPG.Soft.Information.Internet"])
        infonews = data[:,:,"IEPG.Soft.Information.News"]*1000.0/np.nanmax(data[:euIndex,self.__refYear,"IEPG.Soft.Information.News"])
        #print "Internet 0-1000:", infointernet[euIndex,:,0]
        #print "News 0-1000:", infonews[euIndex,:,0]
        info = infointernet*0.5 + infonews*0.5
        #print info[euIndex,:,0]
        info = info * 1000 / np.nanmax(info[:euIndex,refYearIndex,:])

        #print info[euIndex,:,0]

        # countryIdx = data.geoentity.index(u"Germany")
        # print "Germany", countryIdx
        # print "InternetCrud: ",  data[countryIdx,-1,"IEPG.Soft.Information.Internet"]
        # print "NewsCrud: ", data[countryIdx,-1,"IEPG.Soft.Information.News"]
        # print "Internet: ", infointernet[countryIdx,-1,0]
        # print "News: ", infonews[countryIdx,-1,0]
        # print "Total: ", info[countryIdx,-1,0]

        data.addVariable("IEPG.Soft.Information_IEPG", data=info)

        # Sports calculus
        # This is the calculus for the sports coefficient
        linearCoef = self.__environment["SPORTS_LINEAR_COEFICIENT"]
        medals_fifa = self.__environment["SPORTS_MEDALS_FIFA_COEFICIENTS"]

        sports = ((medals_fifa[0]/np.repeat( \
                                   np.nansum(data[:euIndex,:,"IEPG.Soft.Support.Olimpics"], axis=0).reshape(1,shape[1]),
                                   shape[0], axis=0).reshape(shape[0],shape[1])* \
                   10000*data[:,:,"IEPG.Soft.Support.Olimpics"].reshape(shape[0],shape[1]))+ \
                  (medals_fifa[1]/np.repeat( \
                                np.nansum(data[:euIndex,:,"IEPG.Soft.Support.FIFAPoints"], axis=0).reshape(1,shape[1]),
                                             shape[0], axis=0).reshape(shape[0],shape[1])* \
                       10000*data[:,:,"IEPG.Soft.Support.FIFAPoints"].reshape(shape[0],shape[1])))* \
                       np.repeat(np.array(linearCoef).reshape(1,shape[1]), shape[0], axis=0)

        data.addVariable("IEPG.Soft.SportsCoef", data=sports)

        # This is the sum of coeficients for european countries to calculate the EU IEPG
        euIepgSportsCoef = data.getSubset(self.__totalCountriesEu, self.__euDataYearsStr, "IEPG.Soft.SportsCoef")
        euIepgSportsCoef.sort()
        euIepgSportsCoef = self.__clearMissingEuCountries(euIepgSportsCoef, self.__missingEuCountries)
        #print np.nansum(euIepgSportsCoef.data, axis=0)*0.7
        euIepgSportsCoef = (np.nansum(euIepgSportsCoef.data, axis=0)*.7).flatten()
        data[u"European Union",3:,"IEPG.Soft.SportsCoef"] = euIepgSportsCoef

        #print data.select(data.geoentity.index(u"Estados Unidos de América"),"2010","IEPG.Soft.SportsCoef")
        #print np.nanmax(data[:euIndex,refYear,"IEPG.Soft.SportsCoef"])

        # Final IEPG sports calculus
        data.addVariable("IEPG.Soft.Sports_IEPG", data=
                         data[:,:,"IEPG.Soft.SportsCoef"]*1000.0/ \
                         np.nanmax(data[:euIndex,self.__refYear,"IEPG.Soft.SportsCoef"]))

        # euIepgSportsCoef.sort()
        # euIepgSportsCoef = self.__clearMissingEuCountries(euIepgSportsCoef, missingEuCountries)
        # test = np.nansum(euIepgSportsCoef.data,axis=0)

        # euIepgSportsCoef = (np.nansum(euIepgSportsCoef.data, axis=0)*.7).flatten()
        # euIepgSportsCoef = euIepgSportsCoef * 1000.0 /  np.nanmax(data[:euIndex,refYear,"IEPG.Soft.Sports_IEPG"])

        # data[u"European Union",3:,"IEPG.Soft.Sports_IEPG"] = euIepgSportsCoef


        # Military equipment
        militaryEquipment = ['IEPG.Military.Support.AircraftC',
                             'IEPG.Military.Support.Amphibius',
                             'IEPG.Military.Support.Frigates',
                             'IEPG.Military.Support.Destroyer',
                             'IEPG.Military.Support.Cruisers',
                             'IEPG.Military.Support.Submarine',
                             'IEPG.Military.Support.Aeroplane',
                             'IEPG.Military.Support.Airtanker']

        militaryCoefs = []
        militaryCoefsEquip = []

        for i in militaryEquipment:
            militaryCoefs.append(np.nansum(data[:euIndex,self.__refYear,tuple(militaryEquipment)])/ \
                                 np.nansum(data[:euIndex,self.__refYear,i]))

        militaryTotal = np.nansum(np.array(militaryCoefs))

        for i in militaryCoefs:
            militaryCoefsEquip.append(i*1000/militaryTotal)

        ae = np.zeros((shape[0],shape[1]))

        for i in range(0, len(militaryCoefsEquip)):
            ae+=militaryCoefsEquip[i]*np.nan_to_num(data[:,:,militaryEquipment[i]].reshape(shape[0],shape[1]))

        data.addVariable("MilitaryPoints", data=ae)
        data.addVariable("IEPG.Military.MilitaryEquipment_IEPG", data=
                            data[:,:,"MilitaryPoints"]*1000.0/ \
                            np.nanmax(data[:euIndex,self.__refYear,"MilitaryPoints"]))


        # Dimensions and Index
        cEconomic = self.__environment["ECONOMIC_COEFICIENTS"]
        vEconomic = ["Energy","PrimaryGoods","Manufactures","Services","Investments"]
        cMilitary = self.__environment["MILITARY_COEFICIENTS"]
        vMilitary = ["Troops", "MilitaryEquipment"]
        cSoft = self.__environment["SOFT_COEFICIENTS"]
        vSoft = ["Migrations", "Tourism", "Sports", "Culture", "Information", "Technology", "Science",
                 "Education", "DevelopmentC"]
        cIndex = self.__environment["DIMENSION_COEFICIENTS"]

        a = np.zeros((shape[0],shape[1]))

        for i in range(0, len(cEconomic)):
            #print vEconomic[i]
            #print data[u"Germany",:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]
            a+=data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"].reshape(shape[0],shape[1])*cEconomic[i]

        data.addVariable("IEPG.Global.Economic", data=a/100.0)

        a = np.zeros((shape[0],shape[1]))
        for i in range(0, len(cMilitary)):
            a+=data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"].reshape(shape[0],shape[1])*cMilitary[i]

        data.addVariable("IEPG.Global.Military", data=a/100.0)

        a = np.zeros((shape[0],shape[1]))
        for i in range(0, len(cSoft)):
            #print "IEPG.Soft."+vSoft[i]+"_IEPG"
            #print "DATA: ", data[u"United Arab Emirates",:,"IEPG.Soft."+vSoft[i]+"_IEPG"]
            a+=data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"].reshape(shape[0],shape[1])*cSoft[i]



        data.addVariable("IEPG.Global.Soft", data=a/100.0)

        data.addVariable("IEPG.Global.IEPG", data=(data[:,:,"IEPG.Global.Economic"]*cIndex[0]+
                                                   data[:,:,"IEPG.Global.Military"]*cIndex[1]+
                                                   data[:,:,"IEPG.Global.Soft"]*cIndex[2])/100.0)

        # Quota
        variable = [
            'IEPG.Economic.Energy_IEPG',
            'IEPG.Economic.PrimaryGoods_IEPG',
            'IEPG.Economic.Manufactures_IEPG',
            'IEPG.Economic.Services_IEPG',
            'IEPG.Economic.Investments_IEPG',
            'IEPG.Military.Troops_IEPG',
            'IEPG.Military.MilitaryEquipment_IEPG',
            'IEPG.Soft.Migrations_IEPG',
            'IEPG.Soft.Tourism_IEPG',
            'IEPG.Soft.Culture_IEPG',
            'IEPG.Soft.Information_IEPG',
            'IEPG.Soft.Technology_IEPG',
            'IEPG.Soft.Science_IEPG',
            'IEPG.Soft.Education_IEPG',
            'IEPG.Soft.DevelopmentC_IEPG',
            'IEPG.Soft.Sports_IEPG',
            'IEPG.Global.Economic',
            'IEPG.Global.Military',
            'IEPG.Global.Soft',
            'IEPG.Global.IEPG']


        for i in variable:

            a = data[:,:,i].reshape(shape[0],shape[1])/ \
                (np.repeat(np.nansum(data[:euIndex,:,i], axis=0).reshape(1,shape[1]), shape[0], axis=0))

            # Copy array
            euData = data[:,:,i].reshape(shape[0],shape[1]).copy()

            # set UE countries data to NAN. Improve that with a better numpy solution.
            timeIdx = 3
            for year in self.__environment["EUROPEAN_UNION"]:
                geoentityIdx = [data.geoentity.index(x) for x in self.__environment["EUROPEAN_UNION"][year]]
                euData[geoentityIdx,timeIdx] = np.nan
                timeIdx += 1

            b = euData / \
                (np.repeat(np.nansum(euData[:euIndex], axis=0).reshape(1,shape[1]), shape[0], axis=0))

            a[euIndex,3:] = b[euIndex,3:]

            a *= 100

            data.addVariable(i+"_QUOTE", data=a)


        # Contributions
        if not "CONTRIBUTIONS_METHOD" in self.__environment or \
            self.__environment["CONTRIBUTIONS_METHOD"]!="GLOBAL_COEFICIENTS":

            cPresenceEconomic = []
            cPresenceMilitary = []
            cPresenceSoft = []

            for i in range(0, len(cEconomic)):
                cPresenceEconomic.append(cEconomic[i]*cIndex[0]/10000.0)

            for i in range(0, len(cMilitary)):
                cPresenceMilitary.append(cMilitary[i]*cIndex[1]/10000.0)

            for i in range(0, len(cSoft)):
                cPresenceSoft.append(cSoft[i]*cIndex[2]/10000.0)


            pcdEconomic = 0
            pcdMilitary = 0
            pcdSoft = 0
            for i in range(0, len(vEconomic)):
                pcdEconomic+=np.nansum(data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"])*cPresenceEconomic[i]

            for i in range(0, len(vMilitary)):
                pcdMilitary+=np.nansum(data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"])*cPresenceMilitary[i]

            for i in range(0, len(vSoft)):
                pcdSoft+=np.nansum(data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"])*cPresenceSoft[i]

            tci = pcdEconomic+pcdMilitary+pcdSoft

            for i in range(0, len(vEconomic)):
                a = data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]*cEconomic[i]/tci
                a *= 100
                data.addVariable("IEPG.Economic."+vEconomic[i]+"_CON", data=a)

            for i in range(0, len(vMilitary)):
                a = data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"]*cMilitary[i]/tci
                a *= 100
                data.addVariable("IEPG.Military."+vMilitary[i]+"_CON", data=a)

            for i in range(0, len(vSoft)):
                a = data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"]*cSoft[i]/tci
                a *= 100
                data.addVariable("IEPG.Soft."+vSoft[i]+"_CON", data=a)

            eco_con = np.zeros((shape[0],shape[1],1)) * 100
            mil_con = np.zeros((shape[0],shape[1],1)) * 100
            soft_con = np.zeros((shape[0],shape[1],1)) * 100

            data.addVariable("IEPG.Global.Economic_CON", data=eco_con)
            data.addVariable("IEPG.Global.Military_CON", data=mil_con)
            data.addVariable("IEPG.Global.Soft_CON", data=soft_con)

        else:
            economicGlobalCoeficients = self.__environment["ECONOMIC_GLOBAL_COEFICIENTS"]
            militaryGlobalCoeficients = self.__environment["MILITARY_GLOBAL_COEFICIENTS"]
            softGlobalCoeficients = self.__environment["SOFT_GLOBAL_COEFICIENTS"]

            total_contributions = np.zeros((shape[0],shape[1]))

            for i in range(0, len(vEconomic)):
                total_contributions += data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"].reshape(shape[0],shape[1])*economicGlobalCoeficients[i]

            for i in range(0, len(vMilitary)):
                total_contributions += data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"].reshape(shape[0],shape[1])*militaryGlobalCoeficients[i]

            for i in range(0, len(vSoft)):
                total_contributions += data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"].reshape(shape[0],shape[1])*softGlobalCoeficients[i]

            total_contributions = total_contributions.reshape(shape[0],shape[1],1)

            # calculate variables contributions

            for i in range(0, len(vEconomic)):
                a = data[:,:,"IEPG.Economic."+vEconomic[i]+"_IEPG"]*economicGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPG.Economic."+vEconomic[i]+"_CON", data=a)

            for i in range(0, len(vMilitary)):
                a = data[:,:,"IEPG.Military."+vMilitary[i]+"_IEPG"]*militaryGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPG.Military."+vMilitary[i]+"_CON", data=a)

            for i in range(0, len(vSoft)):
                a = data[:,:,"IEPG.Soft."+vSoft[i]+"_IEPG"]*softGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPG.Soft."+vSoft[i]+"_CON", data=a)

            # calculate dimension contributions
            eco_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vEconomic)):
                eco_con += data[:,:,"IEPG.Economic."+vEconomic[i]+"_CON"]

            mil_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vMilitary)):
                mil_con += data[:,:,"IEPG.Military."+vMilitary[i]+"_CON"]

            soft_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vSoft)):
                soft_con += data[:,:,"IEPG.Soft."+vSoft[i]+"_CON"]

            data.addVariable("IEPG.Global.Economic_CON", data=eco_con)
            data.addVariable("IEPG.Global.Military_CON", data=mil_con)
            data.addVariable("IEPG.Global.Soft_CON", data=soft_con)

        data.sort()

        self.__IEPGData = data

        return self.__IEPGData


    def __calculateIEPE(self):
        # IEPG data needed for sports coefficients
        # IEPE Calculus starts here

        # Keep IEPG data for sports coefficients
        #self.__IEPGData = data

        # Prepare variables for IEPE calculus
        data = core.GeoVariableArray()
        [data.merge(self.__book.readGeoVariableArray(".".join(x.filiation))) for x
        in self.__variables if x.filiation[0]=="IEPE"]

        shape = data.shape

        # Previous aggregation
        # Primary goods
        primaryG = np.nansum(data.select(None,None,["IEPE.Economic.FLA","IEPE.Economic.BVT","IEPE.Economic.CMI", \
                                                    "IEPE.Economic.AVO","IEPE.Economic.NFM","IEPE.Economic.PSP", \
                                                    "IEPE.Economic.NMG"]), axis=2)
        data.addVariable("IEPE.Economic.PrimaryGoods", data=primaryG)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Economic.PrimaryGoods")

        # Manufactures
        man = np.nansum(data.select(None,None,["IEPE.Economic.CHM", "IEPE.Economic.ManufacturesPre", \
                                               "IEPE.Economic.Machinery", "IEPE.Economic.MMA"]), axis=2) - \
              np.nansum(data.select(None,None,["IEPE.Economic.NFM","IEPE.Economic.PSP"]), axis=2)
        data.addVariable("IEPE.Economic.Manufactures", data=man)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Economic.Manufactures")

        # Normal calculus
        normal = ["IEPE.Economic.Energy",
                  "IEPE.Economic.PrimaryGoods",
                  "IEPE.Economic.Manufactures",
                  "IEPE.Economic.Services",
                  "IEPE.Economic.Investments",
                  "IEPE.Soft.Migrations",
                  "IEPE.Soft.Tourism",
                  "IEPE.Soft.Culture",
                  #"IEPE.Soft.Information",
                  "IEPE.Soft.Technology",
                  "IEPE.Soft.Science",
                  "IEPE.Soft.Education"]


        for i in normal:
            d = data[:,:,i]*1000.0/np.nanmax(data[:,self.__refYear,i])
            data.addVariable(i+"_IEPE", data=d)
            data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable=i+"_IEPE")

        # Information calculus
        refYearIndex = data.getTimeIndex(self.__refYear)[0]

        infointernet = data[:,:,"IEPE.Soft.Information.Internet"]*1000.0/np.nanmax(data[:,self.__refYear,"IEPE.Soft.Information.Internet"])
        infonews = data[:,:,"IEPE.Soft.Information.News"]*1000.0/np.nanmax(data[:,self.__refYear,"IEPE.Soft.Information.News"])
        info = infointernet*0.5 + infonews*0.5
        info = info * 1000 / np.nanmax(info[:,refYearIndex,:])
        data.addVariable("IEPE.Soft.Information_IEPE", data=info)


        # Dummy zero military equipment, troops, and development cooperation
        zeroes = np.zeros((shape[0],shape[1]))
        data.addVariable("IEPE.Military.Troops_IEPE", data=zeroes)
        data.addVariable("IEPE.Military.MilitaryEquipment_IEPE", data=zeroes)
        data.addVariable("IEPE.Soft.DevelopmentC_IEPE", data=zeroes)

        # IEPE Sports calculus
        euIepgSportsCoef = self.__IEPGData.getSubset(self.__totalCountriesEu, self.__euDataYearsStr, "IEPG.Soft.SportsCoef")
        euIepgSportsCoef.sort()
        euIepgSportsCoef = self.__clearMissingEuCountries(euIepgSportsCoef, self.__missingEuCountries)
        euIepgSportsCoef = euIepgSportsCoef.data*1000.0/np.nanmax(euIepgSportsCoef.select(None, self.__refYear, 0))
        data.addVariable("IEPE.Soft.Sports_IEPE", data=euIepgSportsCoef)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Soft.Sports_IEPE")

        # Dimensions and Index
        cEconomic = self.__environment["ECONOMIC_COEFICIENTS"]
        vEconomic = ["Energy","PrimaryGoods","Manufactures","Services","Investments"]
        cMilitary = self.__environment["MILITARY_COEFICIENTS"]
        vMilitary = ["Troops", "MilitaryEquipment"]
        cSoft = self.__environment["SOFT_COEFICIENTS"]
        vSoft = ["Migrations", "Tourism", "Sports", "Culture", "Information", "Technology", "Science",
                 "Education","DevelopmentC"]
        cIndex = self.__environment["DIMENSION_COEFICIENTS"]

        a = np.zeros((shape[0],shape[1]))
        for i in range(0, len(cEconomic)):
            a+=data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"].reshape(shape[0],shape[1])*cEconomic[i]

        data.addVariable("IEPE.Global.Economic", data=a/100.0)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Global.Economic")

        a = np.zeros((shape[0],shape[1]))
        for i in range(0, len(cMilitary)):
            a+=data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"].reshape(shape[0],shape[1])*cMilitary[i]

        data.addVariable("IEPE.Global.Military", data=a/100.0)

        a = np.zeros((shape[0],shape[1]))
        for i in range(0, len(cSoft)):
            a+=data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"].reshape(shape[0],shape[1])*cSoft[i]

        data.addVariable("IEPE.Global.Soft", data=a/100.0)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Global.Soft")

        data.addVariable("IEPE.Global.IEPE", data=(data[:,:,"IEPE.Global.Economic"]*cIndex[0]+
                                                   data[:,:,"IEPE.Global.Military"]*cIndex[1]+
                                                   data[:,:,"IEPE.Global.Soft"]*cIndex[2])/100.0)
        data = self.__clearMissingEuCountries(data, self.__missingEuCountries, variable="IEPE.Global.IEPE")

        # Quota
        variable = [
            'IEPE.Economic.Energy_IEPE',
            'IEPE.Economic.PrimaryGoods_IEPE',
            'IEPE.Economic.Manufactures_IEPE',
            'IEPE.Economic.Services_IEPE',
            'IEPE.Economic.Investments_IEPE',
            'IEPE.Military.Troops_IEPE',
            'IEPE.Military.MilitaryEquipment_IEPE',
            'IEPE.Soft.Migrations_IEPE',
            'IEPE.Soft.Tourism_IEPE',
            'IEPE.Soft.Culture_IEPE',
            'IEPE.Soft.Information_IEPE',
            'IEPE.Soft.Technology_IEPE',
            'IEPE.Soft.Science_IEPE',
            'IEPE.Soft.Education_IEPE',
            'IEPE.Soft.DevelopmentC_IEPE',
            'IEPE.Soft.Sports_IEPE',
            'IEPE.Global.Economic',
            'IEPE.Global.Military',
            'IEPE.Global.Soft',
            'IEPE.Global.IEPE']

        for i in variable:
            a = data[:,:,i].reshape(shape[0],shape[1])/ \
                (np.repeat(np.nansum(data[:,:,i], axis=0).reshape(1,shape[1]), shape[0], axis=0))

            a *= 100

            data.addVariable(i+"_QUOTE", data=a)

         # Contributions

        if not "CONTRIBUTIONS_METHOD" in self.__environment or \
            self.__environment["CONTRIBUTIONS_METHOD"]!="GLOBAL_COEFICIENTS":

            cPresenceEconomic = []
            cPresenceMilitary = []
            cPresenceSoft = []

            for i in range(0, len(cEconomic)):
                cPresenceEconomic.append(cEconomic[i]*cIndex[0]/10000.0)

            for i in range(0, len(cMilitary)):
                cPresenceMilitary.append(cMilitary[i]*cIndex[1]/10000.0)

            for i in range(0, len(cSoft)):
                cPresenceSoft.append(cSoft[i]*cIndex[2]/10000.0)

            pcdEconomic = 0
            pcdMilitary = 0
            pcdSoft = 0
            for i in range(0, len(vEconomic)):
                pcdEconomic+=np.nansum(data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"])*cPresenceEconomic[i]

            for i in range(0, len(vMilitary)):
                pcdMilitary+=np.nansum(data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"])*cPresenceMilitary[i]

            for i in range(0, len(vSoft)):
                pcdSoft+=np.nansum(data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"])*cPresenceSoft[i]

            tci = pcdEconomic+pcdMilitary+pcdSoft

            for i in range(0, len(vEconomic)):
                a = data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"]*cEconomic[i]/tci
                a *= 100
                data.addVariable("IEPE.Economic."+vEconomic[i]+"_CON", data=a)

            for i in range(0, len(vMilitary)):
                a = data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"]*cMilitary[i]/tci
                a *= 100
                data.addVariable("IEPE.Military."+vMilitary[i]+"_CON", data=a)

            for i in range(0, len(vSoft)):
                a = data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"]*cSoft[i]/tci
                a *= 100
                data.addVariable("IEPE.Soft."+vSoft[i]+"_CON", data=a)

        else:
            economicGlobalCoeficients = self.__environment["ECONOMIC_GLOBAL_COEFICIENTS"]
            militaryGlobalCoeficients = self.__environment["MILITARY_GLOBAL_COEFICIENTS"]
            softGlobalCoeficients = self.__environment["SOFT_GLOBAL_COEFICIENTS"]

            total_contributions = np.zeros((shape[0],shape[1]))

            for i in range(0, len(vEconomic)):
                total_contributions += data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"].reshape(shape[0],shape[1])*economicGlobalCoeficients[i]

            for i in range(0, len(vMilitary)):
                total_contributions += data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"].reshape(shape[0],shape[1])*militaryGlobalCoeficients[i]

            for i in range(0, len(vSoft)):
                total_contributions += data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"].reshape(shape[0],shape[1])*softGlobalCoeficients[i]

            total_contributions = total_contributions.reshape(shape[0],shape[1],1)

            # calculate variables contributions
            for i in range(0, len(vEconomic)):
                a = data[:,:,"IEPE.Economic."+vEconomic[i]+"_IEPE"]*economicGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPE.Economic."+vEconomic[i]+"_CON", data=a)

            for i in range(0, len(vMilitary)):
                a = data[:,:,"IEPE.Military."+vMilitary[i]+"_IEPE"]*militaryGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPE.Military."+vMilitary[i]+"_CON", data=a)

            for i in range(0, len(vSoft)):
                a = data[:,:,"IEPE.Soft."+vSoft[i]+"_IEPE"]*softGlobalCoeficients[i]/total_contributions
                a *= 100
                data.addVariable("IEPE.Soft."+vSoft[i]+"_CON", data=a)

            # calculate dimension contributions
            eco_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vEconomic)):
                eco_con += data[:,:,"IEPE.Economic."+vEconomic[i]+"_CON"]

            mil_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vMilitary)):
                mil_con += data[:,:,"IEPE.Military."+vMilitary[i]+"_CON"]

            soft_con = np.zeros((shape[0],shape[1],1))
            for i in range(0, len(vSoft)):
                soft_con += data[:,:,"IEPE.Soft."+vSoft[i]+"_CON"]

            data.addVariable("IEPE.Global.Economic_CON", data=eco_con)
            data.addVariable("IEPE.Global.Military_CON", data=mil_con)
            data.addVariable("IEPE.Global.Soft_CON", data=soft_con)

        # Set to nan
        variables_tonan = [
            'IEPE.Military.Troops_IEPE',
            'IEPE.Military.MilitaryEquipment_IEPE',
            'IEPE.Soft.DevelopmentC_IEPE',
            'IEPE.Global.Military',

            'IEPE.Military.Troops_IEPE_QUOTE',
            'IEPE.Military.MilitaryEquipment_IEPE_QUOTE',
            'IEPE.Soft.DevelopmentC_IEPE_QUOTE',
            'IEPE.Global.Military_QUOTE',

            'IEPE.Military.Troops_CON',
            'IEPE.Military.MilitaryEquipment_CON',
            'IEPE.Soft.DevelopmentC_CON',
            'IEPE.Global.Military_CON']

        for variable in variables_tonan:
            data[:,:,variable] *= np.nan

        data.sort()

        self.__IEPEData = data

        return self.__IEPEData


    # Clears data for non present countries in EU for certain years
    def __clearMissingEuCountries(self,array, missingEuCountries, variable=0):
        for k,v in missingEuCountries.iteritems():
            for i in v:
                array[i, str(k), variable] = np.nan

        return array


    def __writeToXLSX(self,outfilename):

        ew = excel_utils.ExcelWriter(outfilename)
        ew.addStyle("header", {
            "bg_color": "#08608C",
            "font_color": "white",
            "valign": "vcenter",
            "align": "center",
            "size": 12
        })
        self.__createXLSXSheetsForIEPG(ew)
        self.__createXLSXSheetsForIEPE(ew)

        ew.closeWorkbook()


    def __applyStylesXLSXSheets(self,ew,sheets):
        for name,sheet in sheets.iteritems():
            ew.setColumnStyle(sheet, 0, 0, 25)
            ew.setRowStyle(sheet, 0, 20, style="header")

    def __createXLSXSheetsForIEPG(self,ew):

        if not self.__IEPGData:
            raise Exception('No __IEPGData')

        sheets = ew.writeGeoVariableArray(self.__IEPGData, variable=['IEPG.Economic.Energy_IEPG',
                                                          'IEPG.Economic.PrimaryGoods_IEPG',
                                                          'IEPG.Economic.Manufactures_IEPG',
                                                          'IEPG.Economic.Services_IEPG',
                                                          'IEPG.Economic.Investments_IEPG',
                                                          'IEPG.Military.Troops_IEPG',
                                                          'IEPG.Military.MilitaryEquipment_IEPG',
                                                          'IEPG.Soft.Migrations_IEPG',
                                                          'IEPG.Soft.Tourism_IEPG',
                                                          'IEPG.Soft.Sports_IEPG',
                                                          'IEPG.Soft.Culture_IEPG',
                                                          'IEPG.Soft.Information_IEPG',
                                                          'IEPG.Soft.Technology_IEPG',
                                                          'IEPG.Soft.Science_IEPG',
                                                          'IEPG.Soft.Education_IEPG',
                                                          'IEPG.Soft.DevelopmentC_IEPG',
                                                          'IEPG.Global.Economic',
                                                          'IEPG.Global.Military',
                                                          'IEPG.Global.Soft',
                                                          'IEPG.Global.IEPG',
                                                          'IEPG.Economic.Energy_IEPG_QUOTE',
                                                          'IEPG.Economic.PrimaryGoods_IEPG_QUOTE',
                                                          'IEPG.Economic.Manufactures_IEPG_QUOTE',
                                                          'IEPG.Economic.Services_IEPG_QUOTE',
                                                          'IEPG.Economic.Investments_IEPG_QUOTE',
                                                          'IEPG.Military.Troops_IEPG_QUOTE',
                                                          'IEPG.Military.MilitaryEquipment_IEPG_QUOTE',
                                                          'IEPG.Soft.Migrations_IEPG_QUOTE',
                                                          'IEPG.Soft.Tourism_IEPG_QUOTE',
                                                          'IEPG.Soft.Sports_IEPG_QUOTE',
                                                          'IEPG.Soft.Culture_IEPG_QUOTE',
                                                          'IEPG.Soft.Information_IEPG_QUOTE',
                                                          'IEPG.Soft.Technology_IEPG_QUOTE',
                                                          'IEPG.Soft.Science_IEPG_QUOTE',
                                                          'IEPG.Soft.Education_IEPG_QUOTE',
                                                          'IEPG.Soft.DevelopmentC_IEPG_QUOTE',
                                                          'IEPG.Global.Economic_QUOTE',
                                                          'IEPG.Global.Military_QUOTE',
                                                          'IEPG.Global.Soft_QUOTE',
                                                          'IEPG.Global.IEPG_QUOTE',
                                                          'IEPG.Economic.Energy_CON',
                                                          'IEPG.Economic.PrimaryGoods_CON',
                                                          'IEPG.Economic.Manufactures_CON',
                                                          'IEPG.Economic.Services_CON',
                                                          'IEPG.Economic.Investments_CON',
                                                          'IEPG.Military.Troops_CON',
                                                          'IEPG.Military.MilitaryEquipment_CON',
                                                          'IEPG.Soft.Migrations_CON',
                                                          'IEPG.Soft.Tourism_CON',
                                                          'IEPG.Soft.Sports_CON',
                                                          'IEPG.Soft.Culture_CON',
                                                          'IEPG.Soft.Information_CON',
                                                          'IEPG.Soft.Technology_CON',
                                                          'IEPG.Soft.Science_CON',
                                                          'IEPG.Soft.Education_CON',
                                                          'IEPG.Soft.DevelopmentC_CON',
                                                          'IEPG.Global.Economic_CON',
                                                          'IEPG.Global.Military_CON',
                                                          'IEPG.Global.Soft_CON'],
                                          sheetName=['Energy IEPG',
                                                     'Primary Goods IEPG',
                                                     'Manufactures IEPG',
                                                     'Services IEPG',
                                                     'Investments IEPG',
                                                     'Troops IEPG',
                                                     'Military Equipment IEPG',
                                                     'Migrations IEPG',
                                                     'Tourism IEPG',
                                                     'Sports IEPG',
                                                     'Culture IEPG',
                                                     'Information IEPG',
                                                     'Technology IEPG',
                                                     'Science IEPG',
                                                     'Education IEPG',
                                                     'Development Coop. IEPG',
                                                     'Economic IEPG',
                                                     'Military IEPG',
                                                     'Soft IEPG',
                                                     'IEPG',
                                                     'Energy IEPG QUOTE',
                                                     'Primary Goods IEPG QUOTE',
                                                     'Manufactures IEPG QUOTE',
                                                     'Services IEPG QUOTE',
                                                     'Investments IEPG QUOTE',
                                                     'Troops IEPG QUOTE',
                                                     'Military Equipment IEPG QUOTE',
                                                     'Migrations IEPG QUOTE',
                                                     'Tourism IEPG QUOTE',
                                                     'Sports IEPG QUOTE',
                                                     'Culture IEPG QUOTE',
                                                     'Information IEPG QUOTE',
                                                     'Technology IEPG QUOTE',
                                                     'Science IEPG QUOTE',
                                                     'Education IEPG QUOTE',
                                                     'Development Coop. IEPG QUOTE',
                                                     'Economic IEPG QUOTE',
                                                     'Military IEPG QUOTE',
                                                     'Soft IEPG QUOTE',
                                                     'IEPG IEPG QUOTE',
                                                     'Energy IEPG CONTRIBUTION',
                                                     'Primary Goods IEPG CONTRIBUTION',
                                                     'Manufactures IEPG CONTRIBUTION',
                                                     'Services IEPG CONTRIBUTION',
                                                     'Investments IEPG CONTRIBUTION',
                                                     'Troops IEPG CONTRIBUTION',
                                                     'Military E. IEPG CONTRIBUTION',
                                                     'Migrations IEPG CONTRIBUTION',
                                                     'Tourism IEPG CONTRIBUTION',
                                                     'Sports IEPG CONTRIBUTION',
                                                     'Culture IEPG CONTRIBUTION',
                                                     'Information IEPG CONTRIBUTION',
                                                     'Technology IEPG CONTRIBUTION',
                                                     'Science IEPG CONTRIBUTION',
                                                     'Education IEPG CONTRIBUTION',
                                                     'Devel. C. IEPG CONTRIBUTION',
                                                     'Economic IEPG CONTRIBUTION',
                                                     'Military IEPG CONTRIBUTION',
                                                     'Soft IEPG CONTRIBUTION'])


        self.__applyStylesXLSXSheets(ew,sheets)
        return sheets

    def __createXLSXSheetsForIEPE(self,ew):

        if not self.__IEPEData:
            raise Exception('No __IEPEData')

        sheets = ew.writeGeoVariableArray(self.__IEPEData, variable=['IEPE.Economic.Energy_IEPE',
                                                      'IEPE.Economic.PrimaryGoods_IEPE',
                                                      'IEPE.Economic.Manufactures_IEPE',
                                                      'IEPE.Economic.Services_IEPE',
                                                      'IEPE.Economic.Investments_IEPE',
                                                      'IEPE.Military.Troops_IEPE',
                                                      'IEPE.Military.MilitaryEquipment_IEPE',
                                                      'IEPE.Soft.Migrations_IEPE',
                                                      'IEPE.Soft.Tourism_IEPE',
                                                      'IEPE.Soft.Sports_IEPE',
                                                      'IEPE.Soft.Culture_IEPE',
                                                      'IEPE.Soft.Information_IEPE',
                                                      'IEPE.Soft.Technology_IEPE',
                                                      'IEPE.Soft.Science_IEPE',
                                                      'IEPE.Soft.Education_IEPE',
                                                      'IEPE.Soft.DevelopmentC_IEPE',
                                                      'IEPE.Global.Economic',
                                                      'IEPE.Global.Military',
                                                      'IEPE.Global.Soft',
                                                      'IEPE.Global.IEPE',
                                                      'IEPE.Economic.Energy_IEPE_QUOTE',
                                                      'IEPE.Economic.PrimaryGoods_IEPE_QUOTE',
                                                      'IEPE.Economic.Manufactures_IEPE_QUOTE',
                                                      'IEPE.Economic.Services_IEPE_QUOTE',
                                                      'IEPE.Economic.Investments_IEPE_QUOTE',
                                                      'IEPE.Military.Troops_IEPE_QUOTE',
                                                      'IEPE.Military.MilitaryEquipment_IEPE_QUOTE',
                                                      'IEPE.Soft.Migrations_IEPE_QUOTE',
                                                      'IEPE.Soft.Tourism_IEPE_QUOTE',
                                                      'IEPE.Soft.Sports_IEPE_QUOTE',
                                                      'IEPE.Soft.Culture_IEPE_QUOTE',
                                                      'IEPE.Soft.Information_IEPE_QUOTE',
                                                      'IEPE.Soft.Technology_IEPE_QUOTE',
                                                      'IEPE.Soft.Science_IEPE_QUOTE',
                                                      'IEPE.Soft.Education_IEPE_QUOTE',
                                                      'IEPE.Soft.DevelopmentC_IEPE_QUOTE',
                                                      'IEPE.Global.Economic_QUOTE',
                                                      'IEPE.Global.Military_QUOTE',
                                                      'IEPE.Global.Soft_QUOTE',
                                                      'IEPE.Global.IEPE_QUOTE',
                                                      'IEPE.Economic.Energy_CON',
                                                      'IEPE.Economic.PrimaryGoods_CON',
                                                      'IEPE.Economic.Manufactures_CON',
                                                      'IEPE.Economic.Services_CON',
                                                      'IEPE.Economic.Investments_CON',
                                                      'IEPE.Military.Troops_CON',
                                                      'IEPE.Military.MilitaryEquipment_CON',
                                                      'IEPE.Soft.Migrations_CON',
                                                      'IEPE.Soft.Tourism_CON',
                                                      'IEPE.Soft.Sports_CON',
                                                      'IEPE.Soft.Culture_CON',
                                                      'IEPE.Soft.Information_CON',
                                                      'IEPE.Soft.Technology_CON',
                                                      'IEPE.Soft.Science_CON',
                                                      'IEPE.Soft.Education_CON',
                                                      'IEPE.Soft.DevelopmentC_CON',
                                                      'IEPE.Global.Economic_CON',
                                                        'IEPE.Global.Military_CON',
                                                        'IEPE.Global.Soft_CON'],
                                      sheetName=['Energy IEPE',
                                                 'Primary Goods IEPE',
                                                 'Manufactures IEPE',
                                                 'Services IEPE',
                                                 'Investments IEPE',
                                                 'Troops IEPE',
                                                 'Military Equipment IEPE',
                                                 'Migrations IEPE',
                                                 'Tourism IEPE',
                                                 'Sports IEPE',
                                                 'Culture IEPE',
                                                 'Information IEPE',
                                                 'Technology IEPE',
                                                 'Science IEPE',
                                                 'Education IEPE',
                                                 'Development Coop. IEPE',
                                                 'Economic IEPE',
                                                 'Military IEPE',
                                                 'Soft IEPE',
                                                 'IEPE',
                                                 'Energy IEPE QUOTE',
                                                 'Primary Goods IEPE QUOTE',
                                                 'Manufactures IEPE QUOTE',
                                                 'Services IEPE QUOTE',
                                                 'Investments IEPE QUOTE',
                                                 'Troops IEPE QUOTE',
                                                 'Military Equip. IEPE QUOTE',
                                                 'Migrations IEPE QUOTE',
                                                 'Tourism IEPE QUOTE',
                                                 'Sports IEPE QUOTE',
                                                 'Culture IEPE QUOTE',
                                                 'Information IEPE QUOTE',
                                                 'Technology IEPE QUOTE',
                                                 'Science IEPE QUOTE',
                                                 'Education IEPE QUOTE',
                                                 'Development Coop. IEPE QUOTE',
                                                 'Economic IEPE QUOTE',
                                                 'Military IEPE QUOTE',
                                                 'Soft IEPE QUOTE',
                                                 'IEPE IEPE QUOTE',
                                                 'Energy IEPE CONTRIBUTION',
                                                 'Primary Goods IEPE CONTRIBUTION',
                                                 'Manufactures IEPE CONTRIBUTION',
                                                 'Services IEPE CONTRIBUTION',
                                                 'Investments IEPE CONTRIBUTION',
                                                 'Troops IEPE CONTRIBUTION',
                                                 'Military E. IEPE CONTRIBUTION',
                                                 'Migrations IEPE CONTRIBUTION',
                                                 'Tourism IEPE CONTRIBUTION',
                                                 'Sports IEPE CONTRIBUTION',
                                                 'Culture IEPE CONTRIBUTION',
                                                 'Information IEPE CONTRIBUTION',
                                                 'Technology IEPE CONTRIBUTION',
                                                 'Science IEPE CONTRIBUTION',
                                                 'Education IEPE CONTRIBUTION',
                                                 'Devel. C. IEPE CONTRIBUTION',
                                                 'Economic IEPE CONTRIBUTION',
                                                    'Military IEPE CONTRIBUTION',
                                                    'Soft IEPE CONTRIBUTION'])

        self.__applyStylesXLSXSheets(ew,sheets)
        return sheets


    def __selectData(self,geovariablearray,country,time,variable):
        data = geovariablearray.select(country,time,variable)[0,0,0]
        return data if not np.isnan(data) else None


    def __getCountryCodeByCountryName(self,countryName,maplexModel=None):
        if not maplexModel:
            maplexModel = MaplexModel()

        if countryName==u"Iran (Islamic Republic of)":
            countryName=u"Iran"
        elif countryName==u"Korea":
            countryName=u"South Korea"
        elif countryName==u"Russian Federation":
            countryName=u"Russia"
        elif countryName==u"United Republic of Tanzania":
            countryName=u"Tanzania"
        elif countryName==u"Venezuela (Bolivarian Republic of)":
            countryName=u"Venezuela"
        elif countryName==u"Viet Nam":
            countryName=u"Vietnam"

        # if countryName==u"Kazajistán":
        #     return self.__getCountryCodeByCountryName(u"Kazajstán",maplexModel)
        # el
        if countryName==u"European Union":
            return "XBEU"
        else:
            geoentity = maplexModel.getIdGeoentityByName(countryName,2)
            if not geoentity:
                raise Exception('Not found geoentity for ' + countryName)

            geoentity_id = geoentity[0]["id_geoentity"]

            geoentity_names = maplexModel.getGeoentityNames(geoentity_id,1)
            if not geoentity_names:
                raise Exception('Not found geoentity code name for ' + countryName)

            return geoentity_names[0]["names"][0]


    def __writeToDatabase(self):

        fm = FluxModel()
        #im = IepgDataModel()
        mm = MaplexModel()

        fm.prepareSchemaIEPGDataRedux()

        # ADD IEPG
        print "Adding IEPG data"
        datadb = []
        for countryname in self.__IEPGData.geoentity:

            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPGData.time)):
                year = str(self.__IEPGData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPGData.time[idx].start,
                    "date_out" : self.__IEPGData.time[idx].end,
                    "energy" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Energy_IEPG"),
                    "primary_goods" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.PrimaryGoods_IEPG"),
                    "manufactures" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Manufactures_IEPG"),
                    "services" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Services_IEPG"),
                    "investments" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Investments_IEPG"),
                    "troops" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Military.Troops_IEPG"),
                    "military_equipment" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Military.MilitaryEquipment_IEPG"),
                    "migrations" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Migrations_IEPG"),
                    "tourism" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Tourism_IEPG"),
                    "sports" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Sports_IEPG"),
                    "culture" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Culture_IEPG"),
                    "information" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Information_IEPG"),
                    "technology" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Technology_IEPG"),
                    "science" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Science_IEPG"),
                    "education" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Education_IEPG"),
                    "cooperation" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.DevelopmentC_IEPG"),
                    "economic_presence" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Economic"),
                    "military_presence" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Military"),
                    "soft_presence" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Soft"),
                    "iepg" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.IEPG")
                }

                datadb.append(el)

        fm.addDataIEPG(datadb)
        print "IEPG added successfully"

        # END ADD IEPG

        # # ADD IEPE
        print "Adding IEPE"
        datadb = []
        for countryname in self.__IEPEData.geoentity:

            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPEData.time)):
                year = str(self.__IEPEData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPEData.time[idx].start,
                    "date_out" : self.__IEPEData.time[idx].end,
                    "energy" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Energy_IEPE"),
                    "primary_goods" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.PrimaryGoods_IEPE"),
                    "manufactures" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Manufactures_IEPE"),
                    "services" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Services_IEPE"),
                    "investments" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Investments_IEPE"),
                    "troops" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Military.Troops_IEPE"),
                    "military_equipment" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Military.MilitaryEquipment_IEPE"),
                    "migrations" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Migrations_IEPE"),
                    "tourism" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Tourism_IEPE"),
                    "sports" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Sports_IEPE"),
                    "culture" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Culture_IEPE"),
                    "information" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Information_IEPE"),
                    "technology" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Technology_IEPE"),
                    "science" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Science_IEPE"),
                    "education" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Education_IEPE"),
                    "cooperation" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.DevelopmentC_IEPE"),
                    "economic_presence" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Economic"),
                    "military_presence" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Military"),
                    "soft_presence" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Soft"),
                    "iepe" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.IEPE")
                }

                datadb.append(el)

        fm.addDataIEPE(datadb)
        print "IEPE added successfully"

        # ADD IEPG Quote
        print "Adding IEPG Quote"
        datadb = []
        for countryname in self.__IEPGData.geoentity:

            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPGData.time)):
                year = str(self.__IEPGData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPGData.time[idx].start,
                    "date_out" : self.__IEPGData.time[idx].end,
                    "economic_quota" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Economic_QUOTE"),
                    "military_quota" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Military_QUOTE"),
                    "soft_quota" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Soft_QUOTE"),
                    "global_quota" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.IEPG_QUOTE"),
                }

                datadb.append(el)

        fm.addDataIEPGQuote(datadb)
        print "IEPG Quote added successfully"

        print "Adding IEPE Quotes"
        datadb = []
        for countryname in self.__IEPEData.geoentity:

            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPEData.time)):
                year = str(self.__IEPEData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPEData.time[idx].start,
                    "date_out" : self.__IEPEData.time[idx].end,
                    "economic_quota" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Economic_QUOTE"),
                    "soft_quota" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Soft_QUOTE"),
                    "global_quota" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.IEPE_QUOTE"),
                }

                datadb.append(el)

        fm.addDataIEPEQuote(datadb)
        print "IEPE Quotes added successfully"

        # ADD IEPG CONTRIBUTIONS
        print "Adding IEPG contributions"
        datadb = []
        for countryname in self.__IEPGData.geoentity:
            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPGData.time)):
                year = str(self.__IEPGData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPGData.time[idx].start,
                    "date_out" : self.__IEPGData.time[idx].end,
                    "energy" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Energy_CON"),
                    "primary_goods" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.PrimaryGoods_CON"),
                    "manufactures" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Manufactures_CON"),
                    "services" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Services_CON"),
                    "investments" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Economic.Investments_CON"),
                    "troops" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Military.Troops_CON"),
                    "military_equipment" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Military.MilitaryEquipment_CON"),
                    "migrations" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Migrations_CON"),
                    "tourism" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Tourism_CON"),
                    "sports" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Sports_CON"),
                    "culture" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Culture_CON"),
                    "information" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Information_CON"),
                    "technology" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Technology_CON"),
                    "science" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Science_CON"),
                    "education" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.Education_CON"),
                    "cooperation" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Soft.DevelopmentC_CON"),
                    "economic_contribution" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Economic_CON"),
                    "military_contribution" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Military_CON"),
                    "soft_contribution" : self.__selectData(self.__IEPGData,countryname,year,"IEPG.Global.Soft_CON")
                }

                datadb.append(el)

        fm.addDataIEPGContribituon(datadb)
        print "IEPG Contributions added successfully"
        # END ADD IEPG Contributions

        # ADD IEPE CONTRIBUTIONS
        print "Adding IEPE contributions"
        datadb = []
        for countryname in self.__IEPEData.geoentity:

            countrycode = self.__getCountryCodeByCountryName(countryname,mm)

            for idx in range(0, len(self.__IEPEData.time)):
                year = str(self.__IEPEData.time[idx].start.year)
                el = {
                    "code" : countrycode,
                    "date_in" : self.__IEPEData.time[idx].start,
                    "date_out" : self.__IEPEData.time[idx].end,
                    "energy" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Energy_CON"),
                    "primary_goods" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.PrimaryGoods_CON"),
                    "manufactures" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Manufactures_CON"),
                    "services" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Services_CON"),
                    "investments" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Economic.Investments_CON"),
                    "troops" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Military.Troops_CON"),
                    "military_equipment" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Military.MilitaryEquipment_CON"),
                    "migrations" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Migrations_CON"),
                    "tourism" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Tourism_CON"),
                    "sports" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Sports_CON"),
                    "culture" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Culture_CON"),
                    "information" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Information_CON"),
                    "technology" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Technology_CON"),
                    "science" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Science_CON"),
                    "education" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.Education_CON"),
                    "cooperation" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Soft.DevelopmentC_CON"),
                    "economic_contribution" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Economic_CON"),
                    "military_contribution" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Military_CON"),
                    "soft_contribution" : self.__selectData(self.__IEPEData,countryname,year,"IEPE.Global.Soft_CON")
                    # "economic_contribution" : None,
                    # "military_contribution" : None,
                    # "soft_contribution" : None
                }

                datadb.append(el)

        fm.addDataIEPEContribituon(datadb)
        print "IEPE Contributions added successfully"

        # END ADD IEPG Contributions

    def updateRedisCache(self):

        print "Updating redis cache"
        connclient = redis.StrictRedis(host=config.RedisConfig["host"], port=config.RedisConfig["port"], db=0)
        mc = datacache.RedisDataCache(connclient, prefix="iepg_", timeout=None)

        dataSets = dict()
        dataInterface = varengine.DataInterfacePostgreSql()
        tables = {
            "iepg": "iepg_data",
            "iepe": "iepe_data",
            "context": "pob_pib",
            #"iepe_individual_contribution": "iepe_individual_contribution",
            "iepe_quota": "iepe_quota",
            "iepe_relative_contribution": "iepe_relative_contribution",
            #"iepg_individual_contribution": "iepg_individual_contribution",
            "iepg_quota": "iepg_quota",
            "iepg_relative_contribution": "iepg_relative_contribution"
        }

        # @@@YEARS To be edited to add new years to the application
        years = {
            "iepg": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013,2014,2015],
            "iepe": [2005, 2010, 2011, 2012, 2013,2014,2015],
            "context": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013,2014,2015],
            #"iepe_individual_contribution": [2005, 2010, 2011, 2012, 2013],
            "iepe_quota": [2005, 2010, 2011, 2012, 2013],
            "iepe_relative_contribution": [2005, 2010, 2011, 2012, 2013,2014,2015],
            #"iepg_individual_contribution": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013],
            "iepg_quota": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013,2014,2015],
            "iepg_relative_contribution": [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013,2014,2015]
        }

        blockFunctions = {
            "iepg": {
                "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
                "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
            },
            "context": {
                "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM", "XBEU"],
                "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
            },
            "iepg_quota": {
                "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
                "function": "blockfunc::common.blockfunctions.blockFunctionLumpSum"
            },
            "iepg_relative_contribution": {
                "variables": ["energy", "primary_goods", "manufactures", "services", "investments",
                              "troops", "military_equipment", "migrations", "tourism", "sports", "culture",
                              "information", "technology", "science", "education", "cooperation"],
                "blocks": ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"],
                "function": "blockfunc::common.blockfunctions.blockFunctionRelativeContributions"
            }
        }

        for fam in const.variableNames.keys():
            dataSets[fam] = varengine.DataSet(fam)
            dataSets[fam].context["dataSets"] = dataSets

            mapping = dict()
            dataInterface.readAll("iepg_data_redux."+tables[fam],
                                  "code", "date_in", "date_out")
            for k,var in const.variableNames[fam].iteritems():
                v = varengine.Variable(k, True, "float", dataSet=dataSets[fam])
                v.loadFromDataInterface(dataInterface, var["column"])
                if fam in blockFunctions:
                    d = blockFunctions[fam]
                    for y in years[fam]:
                        for b in d["blocks"]:
                            if "variables" in d:
                                if k in d["variables"]:
                                    v.addValue(b, y, d["function"], None)
                            else:
                                v.addValue(b, y, d["function"], None)

        for dsKey, dataSet in dataSets.iteritems():
            dataSet.addToContext("const", const.variableNames)
            for varKey, variable in dataSet.variables.iteritems():
                variable.processData()
            dataSet.dropContext()

        for y in const.years:
            ds = dataSets["iepg_relative_contribution"]
            for b in ["XBAP", "XBSA", "XBNA", "XBE2", "XBLA", "XBMM"]:
                for c, dim in const.dimensions.iteritems():
                    data = 0
                    for var in dim:
                        v = ds.variables[var].getData(code=b, year=y)[str(b)+"@"+str(y)]["value"]
                        data = v+data if v else data
                    ds.variables[c].addValue(b, y, "float", data)

        for dsKey in dataSets:
            mc.set(dsKey, dataSets[dsKey], 0)


        blocks = [maplex.getGeoentityNames(i["id_geoentity_block"], 1)[0]["names"][0] for i in maplex.getBlocks()]
        blocksNoEu = copy.deepcopy(blocks)
        blocksNoEu.remove("XBEU")
        countriesAndEu = dataSets["iepg"].variables["energy"].getVariableCodes()
        countriesAndEu = arrayops.arraySubstraction(countriesAndEu, blocks)
        countriesAndEu.append("XBEU")
        countries = copy.deepcopy(countriesAndEu)
        countries.remove("XBEU")
        blocksAndCountries = copy.deepcopy(countries)
        blocksAndCountries.extend(blocks)

        isoToSpanish, spanishToIso = maplex.getTranslationTable(1, idNameFamilyB=3)
        isoToSpanish = {key: value for key,value in isoToSpanish.iteritems() if key in blocksAndCountries}
        spanishToIso = {key: value for key,value in spanishToIso.iteritems() if value in blocksAndCountries}

        isoToEnglish, englishToIso = maplex.getTranslationTable(1, idNameFamilyB=2)
        isoToEnglish = {key: value for key,value in isoToEnglish.iteritems() if key in blocksAndCountries}
        englishToIso = {key: value for key,value in englishToIso.iteritems() if value in blocksAndCountries}

        isoToGeoentity, geoentityToIso = maplex.getTranslationTable(1)
        isoToGeoentity = {key: value for key,value in isoToGeoentity.iteritems() if key in blocksAndCountries}
        geoentityToIso = {key: value for key,value in geoentityToIso.iteritems() if value in blocksAndCountries}

        mc.set("blocks", blocks, 0)
        mc.set("blocksNoEu", blocksNoEu, 0)
        mc.set("countriesAndEu", countriesAndEu, 0)
        mc.set("countries", countries, 0)
        mc.set("blocksAndCountries", blocksAndCountries, 0)
        mc.set("isoToSpanish", isoToSpanish, 0)
        mc.set("spanishToIso", spanishToIso, 0)
        mc.set("isoToEnglish", isoToEnglish, 0)
        mc.set("englishToIso", englishToIso, 0)
        mc.set("isoToGeoentity", isoToGeoentity, 0)
        mc.set("geoentityToIso", geoentityToIso, 0)

        print "Update redis cache successfully"

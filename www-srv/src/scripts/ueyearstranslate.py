# coding=UTF8
from flux_lib.data import excel_utils

def __cast(value, typeA, typeB):
      """Casts a type to a type. Types can be either Excel cell types,
      Python base types or Numpy types.

      """

      # print "A : ", typeA
      # print
      # print "B : ", typeB
      # print
      # print "VAL : ", value
      # print

      if typeA==0:
          if typeB==np.float64 or typeB==np.float32 or typeB==np.int32 or \
             typeB==np.uint64 or typeB==np.int64:
              return np.nan
          if typeB==str:
              return ""
      if typeA==1:
          if typeB==str:
              return unicode(value)
          if typeB==np.int32:
              if isinstance(value, unicode) and value=="":
                  return np.nan
              else:
                  return np.int32(value)
          if typeB==np.float32:
              return np.float32(self.__analyzeStringNumber(value))
          if typeB==np.float64:
              return np.float64(self.__analyzeStringNumber(value))
      if typeA==2:
          if typeB==np.float32:
              return np.float32(value)
          if typeB==np.float64:
              return np.float64(value)
          if typeB==np.int32:
              return np.int32(value)
          if typeB==np.uint64:
              return np.uint64(value)
          if typeB==np.int64:
              return np.int64(value)
          if typeB==str:
              return str(value)
      if typeA==str:
          if typeB==np.int32:
              return np.int32(value)
      if typeA==int:
          if typeB==np.float64:
              return np.float64(value)

array = {2005: [u"Alemania",u"Austria",u"Bélgica",u"Chipre",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Suecia"], 2010: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"], 2011: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"], 2012: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"], 2013: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Croacia",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"], 2014: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Croacia",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"], 2015: [u"Alemania",u"Austria",u"Bélgica",u"Bulgaria",u"Chipre",u"Croacia",u"Dinamarca",u"Eslovaquia",u"Eslovenia",u"España",u"Estonia",u"Finlandia",u"Francia",u"Grecia",u"Hungría",u"Irlanda",u"Italia",u"Letonia",u"Lituania",u"Luxemburgo",u"Malta",u"Países Bajos",u"Polonia",u"Portugal",u"Reino Unido",u"República Checa",u"Rumanía",u"Suecia"]}

filename = "../../database/flux/year2016.xlsx"

book = excel_utils.ExcelReader(filename, 
                                       decimalSeparator=",")
r = book.rowReader("Country Codes (Global)", startCell=(1,0), endMark="")
data = [[__cast(x[0].value, x[0].ctype, str),__cast(x[1].value, x[1].ctype, str)] for x in r[0]]

def getCountryEN(esname):
  for row in data:
    if row[0]==esname:
      return row[1]
  return None

response = {}
for year in array:
  response[year] = []
  for country_es in array[year]:
    name = getCountryEN(country_es)
    if not name:
      print "Not found " + country_es
    else:
      response[year].append(name)

print response

#print getCountryEN(u"Suecia")

#print data
#print array
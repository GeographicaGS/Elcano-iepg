# coding=UTF8

import common.helpers as helpers
reload(helpers)

# print helpers.blocksSumCalculateData("XBME", 2013, "iepg", "energy")

a = ["XBLA", "XBEU"]
a.extend(helpers.getIepgCountries())

b = helpers.getBlocksCountries(a, 1990, countryFilter=["AT", "AU", "BE", "SG", "VN", "US"])

print(helpers.getBlocksFromCountryList(b))

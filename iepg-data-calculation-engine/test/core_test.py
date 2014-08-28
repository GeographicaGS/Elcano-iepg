# coding=UTF8

import unittest
import numpy as np, numpy.testing as npt
import data.core as core
reload(core)

class TestTime(unittest.TestCase):
    def test_initialization(self):
        a = core.Time("2013-02-01 12:23:21|2014-02-02 14:21:32")
        self.assertEqual(str(a), "Time: 2013-02-01 12:23:21 | 2014-02-02 14:21:32")

        # a = core.Time("2013-02-01 12:23|2014-02-02 14:21")
        # self.assertEqual(str(a), "Time: 2013-02-01 12:23:00 | 2014-02-02 14:21:59")

        # a = core.Time("2013-02-01 12|2014-02-02 14")
        # self.assertEqual(str(a), "Time: 2013-02-01 12:00:00 | 2014-02-02 14:59:59")

        # a = core.Time("2013-02-01|2014-02-02")
        # self.assertEqual(str(a), "Time: 2013-02-01 00:00:00 | 2014-02-02 23:59:59")

        # a = core.Time("2013-02|2014-02")
        # self.assertEqual(str(a), "Time: 2013-02-01 00:00:00 | 2014-02-28 23:59:59")

        # a = core.Time("1999-02|2000-02")
        # self.assertEqual(str(a), "Time: 1999-02-01 00:00:00 | 2000-02-29 23:59:59")

        # a = core.Time("1999|2000")
        # self.assertEqual(str(a), "Time: 1999-01-01 00:00:00 | 2000-12-31 23:59:59")

        # a = core.Time("2013-02-01 12:23:21")
        # self.assertEqual(str(a), "Time: 2013-02-01 12:23:21 | 2013-02-01 12:23:21")

        # a = core.Time("2012-02")
        # self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2012-02-29 23:59:59")

        # a = core.Time("2011-02")
        # self.assertEqual(str(a), "Time: 2011-02-01 00:00:00 | 2011-02-28 23:59:59")

        # a = core.Time("2013")
        # self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | 2013-12-31 23:59:59")

        # a = core.Time("2013|")
        # self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | None")

        # a = core.Time("|2013")
        # self.assertEqual(str(a), "Time: None | 2013-12-31 23:59:59")

        # a = core.Time("2013-12-20|2013")
        # self.assertEqual(str(a), "Time: 2013-12-20 00:00:00 | 2013-12-31 23:59:59")

        # a = core.Time("2012-02-29 12:12|2012-02-29")
        # self.assertEqual(str(a), "Time: 2012-02-29 12:12:00 | 2012-02-29 23:59:59")

        # a = core.Time("2012-02-29 13:23:12|2014")
        # self.assertEqual(str(a), "Time: 2012-02-29 13:23:12 | 2014-12-31 23:59:59")

        # a = core.Time("2013|2011")
        # self.assertEqual(str(a), "Time: None | None")

        # a = core.Time("2012-02|1Y")
        # self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2013-02-01 23:59:59")

        # a = core.Time("2012-02|1Y1M1W1D1H1m1S")
        # self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2013-03-09 01:01:01")

        # a = core.Time("2013", "2015")
        # self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | 2015-12-31 23:59:59")


class TestGeoVariableArray(unittest.TestCase):
    def test_initialization(self):
        # Contructor tests
        print "Testing constructor..."

        a = core.GeoVariableArray()
        self.assertEqual(a.geoentity, None)
        self.assertEqual(a.time, None)
        self.assertEqual(a.variable, None)
        self.assertEqual(a.shape, None)
        self.assertEqual(a.data, None)

        a = core.GeoVariableArray(geoentity="ES")
        self.assertEqual(a.geoentity, ["ES"])
        self.assertEqual(a.time, None)
        self.assertEqual(a.variable, None)
        self.assertEqual(a.shape, None)
        self.assertEqual(a.data, None)

        a = core.GeoVariableArray(geoentity=["ES","US"], time="2014")
        self.assertEqual(a.geoentity, ["ES","US"])
        self.assertEqual([str(x) for x in a.time], ['Time: 2014-01-01 00:00:00 | 2014-12-31 23:59:59'])
        self.assertEqual(a.variable, None)
        self.assertEqual(a.shape, None)
        self.assertEqual(a.data, None)

        a = core.GeoVariableArray(geoentity=["ES","US"], time=["2014","2015"], variable="V0")
        self.assertEqual(a.geoentity, ["ES","US"])
        self.assertEqual([str(x) for x in a.time], ['Time: 2014-01-01 00:00:00 | 2014-12-31 23:59:59', \
                                                    'Time: 2015-01-01 00:00:00 | 2015-12-31 23:59:59'])
        self.assertEqual(a.variable, ["V0"])
        self.assertEqual(a.shape, (2,2,1))
        self.assertEqual([str(a()[0,0,0]), str(a()[1,1,0])], ['nan','nan'])

        a = core.GeoVariableArray(geoentity=["ES","US"], time=["2014","2015"], variable=["V0","V1"])
        self.assertEqual(a.geoentity, ["ES","US"])
        self.assertEqual([str(x) for x in a.time], ['Time: 2014-01-01 00:00:00 | 2014-12-31 23:59:59', \
                                                    'Time: 2015-01-01 00:00:00 | 2015-12-31 23:59:59'])
        self.assertEqual(a.variable, ["V0","V1"])
        self.assertEqual(a.shape, (2,2,2))
        self.assertEqual([str(a()[0,0,0]), str(a()[1,1,1])], ['nan','nan'])

        a = core.GeoVariableArray(geoentity=["ES","US"], time=["2014","2015"], variable=["V0","V1"],
                                  data=[0.000,0.001,0.010,0.011,0.100,0.101,0.110,0.111])
        self.assertEqual(a.geoentity, ["ES","US"])
        self.assertEqual([str(x) for x in a.time], ['Time: 2014-01-01 00:00:00 | 2014-12-31 23:59:59', \
                                                    'Time: 2015-01-01 00:00:00 | 2015-12-31 23:59:59'])
        self.assertEqual(a.variable, ["V0","V1"])
        self.assertEqual(a.shape, (2,2,2))
        self.assertEqual([a()[0,0,0], a()[1,1,1]], [0.000,0.111])

        # Add data from scratch test
        print "Add data from scratch..."

        a = core.GeoVariableArray()

        a.addGeoentity("ES")
        self.assertEqual(a(), None)
        self.assertEqual(a.geoentity, ["ES"])

        a.addTime("2011")
        self.assertEqual(a(), None)
        self.assertEqual([str(x) for x in a.time], ['Time: 2011-01-01 00:00:00 | 2011-12-31 23:59:59'])

        a.addVariable("V0", data=[0.000])
        self.assertEqual(a()[0,0,0], 0)
        self.assertEqual(a.variable, ["V0"])

        a.addGeoentity("DE", data=[0.100])
        self.assertEqual([a()[0,0,0], a()[1,0,0]], [0,0.1])
        self.assertEqual(a.geoentity, ["ES","DE"])

        a.addTime("2012", data=[0.010,0.110])
        npt.assert_almost_equal(a(), [[[0],[0.01]],[[0.1],[0.11]]])
        self.assertEqual([str(x) for x in a.time], ['Time: 2011-01-01 00:00:00 | 2011-12-31 23:59:59',
                                                    'Time: 2012-01-01 00:00:00 | 2012-12-31 23:59:59'])

        a.addVariable("V1", data=[0.001,0.011,0.101,0.111])
        npt.assert_almost_equal(a(), [[[0,0.001],[0.01,0.011]],[[0.1,0.101],[0.11,0.111]]])
        self.assertEqual(a.variable, ["V0","V1"])

        # Indexing
        a = core.GeoVariableArray(geoentity=["ES","EN","US"], 
                                  time=["2011","2012","2013"], variable=["V0","V1","V2"],
                                  data=[0.000,0.100,0.200, \
                                        0.010,0.110,0.210, \
                                        0.020,0.120,0.220, \
                                        0.001,0.101,0.201, \
                                        0.011,0.111,0.211, \
                                        0.021,0.121,0.221, \
                                        0.002,0.102,0.202, \
                                        0.012,0.112,0.212, \
                                        0.022,0.122,0.222])

        self.assertEqual(a.shape, (3,3,3))

                  
        print a()
        



if __name__ == "__main__":
    unittest.main()


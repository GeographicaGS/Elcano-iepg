# coding=UTF8

import unittest
import core
reload(core)

class TestTime(unittest.TestCase):
    def test_initialization(self):
        a = core.Time("2013-02-01 12:23:21|2014-02-02 14:21:32")
        self.assertEqual(str(a), "Time: 2013-02-01 12:23:21 | 2014-02-02 14:21:32")

        a = core.Time("2013-02-01 12:23|2014-02-02 14:21")
        self.assertEqual(str(a), "Time: 2013-02-01 12:23:00 | 2014-02-02 14:21:59")

        a = core.Time("2013-02-01 12|2014-02-02 14")
        self.assertEqual(str(a), "Time: 2013-02-01 12:00:00 | 2014-02-02 14:59:59")

        a = core.Time("2013-02-01|2014-02-02")
        self.assertEqual(str(a), "Time: 2013-02-01 00:00:00 | 2014-02-02 23:59:59")

        a = core.Time("2013-02|2014-02")
        self.assertEqual(str(a), "Time: 2013-02-01 00:00:00 | 2014-02-28 23:59:59")

        a = core.Time("1999-02|2000-02")
        self.assertEqual(str(a), "Time: 1999-02-01 00:00:00 | 2000-02-29 23:59:59")

        a = core.Time("1999|2000")
        self.assertEqual(str(a), "Time: 1999-01-01 00:00:00 | 2000-12-31 23:59:59")

        a = core.Time("2013-02-01 12:23:21")
        self.assertEqual(str(a), "Time: 2013-02-01 12:23:21 | 2013-02-01 12:23:21")

        a = core.Time("2012-02")
        self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2012-02-29 23:59:59")

        a = core.Time("2011-02")
        self.assertEqual(str(a), "Time: 2011-02-01 00:00:00 | 2011-02-28 23:59:59")

        a = core.Time("2013")
        self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | 2013-12-31 23:59:59")

        a = core.Time("2013|")
        self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | None")

        a = core.Time("|2013")
        self.assertEqual(str(a), "Time: None | 2013-12-31 23:59:59")

        a = core.Time("2013-12-20|2013")
        self.assertEqual(str(a), "Time: 2013-12-20 00:00:00 | 2013-12-31 23:59:59")

        a = core.Time("2012-02-29 12:12|2012-02-29")
        self.assertEqual(str(a), "Time: 2012-02-29 12:12:00 | 2012-02-29 23:59:59")

        a = core.Time("2012-02-29 13:23:12|2014")
        self.assertEqual(str(a), "Time: 2012-02-29 13:23:12 | 2014-12-31 23:59:59")

        a = core.Time("2013|2011")
        self.assertEqual(str(a), "Time: None | None")

        a = core.Time("2012-02|1Y")
        self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2013-02-01 23:59:59")

        a = core.Time("2012-02|1Y1M1W1D1H1m1S")
        self.assertEqual(str(a), "Time: 2012-02-01 00:00:00 | 2013-03-09 01:01:01")

        a = core.Time("2013", "2015")
        self.assertEqual(str(a), "Time: 2013-01-01 00:00:00 | 2015-12-31 23:59:59")



if __name__ == "__main__":
    unittest.main()


# coding=UTF8

import core as c
reload(c)

# Constructors
d = c.Time("2014-01-01 02:12")
print d
print

d = c.Time("|2014-01-01 3:11")
print d
print

d = c.Time("2013-01-01 8:23|2014-01-01")
print d
print

d = c.Time("2013-01-01 15:12|")
print d
print

d = c.Time("2013-01-01 15:12|2013-01-01 15:12")
print d
print

d = c.Time(None, "2013-01-01 15:34")
print d
print

d = c.Time("2013-01-01", "2014-02-01")
print d
print

d = c.Time(2013,01,01)
print d
print

d = c.Time(2013,01,01,None)
print d
print

d = c.Time(2013,01,01,15,12)
print d
print

d = c.Time(2013,01,01,15,12,None)
print d
print

d = c.Time(2013,01,01,2014,01,01)
print d
print

d = c.Time(2013,01,01,15,12,2014,01,01,14,21)
print d
print

d = c.Time(None,2014,01,01,14,21)
print d
print

d = c.Time(None,2014,01,01)
print d
print



# Operators

print c.Time("2013-01-01|2014-01-01")/"2013-01-01|2014-01-01"
print c.Time("2013-07-01")/c.Time("2013-07-01")

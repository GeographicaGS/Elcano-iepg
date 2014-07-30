# coding=UTF8

"""

Time and TimeLapse class.

"""
import datetime

class Time(object):
    time = None

    def __init__(self, time):
        """Constructor."""
        if time<>None:
            self.time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')

    def __str__(self):
        return(str(self.time))



class TimeLapse(object):
    dateIn = None        # Both Time objects
    dateOut = None

    def __init__(self):
        """Constructor."""
        self.dateIn = None
        self.dateOut = None

    def initByStrings(self, dateIn=None, dateOut=None):
        """Constructor by strings."""
        self.dateIn = Time(dateIn) if dateIn else None
        self.dateOut = Time(dateOut) if dateOut else None

    def initByTime(self, dateIn=None, dateOut=None):
        """Constructor by Time objects."""
        self.dateIn = dateIn
        self.dateOut = dateOut

    def __str__(self):
        """Return string representation."""
        return(str(self.dateIn)+"|"+str(self.dateOut)) 

    def getSqlFilter(self, fields):
        """Returns a SQL filter."""
        bindings = []
        sql = ""
        if self.dateIn:
            sql += fields[0]+">=%s"
            bindings.append(self.dateIn.time)
        if self.dateOut:
            if sql<>"":
                sql += " and "
            sql += fields[1]+"<=%s"
            bindings.append(self.dateOut.time)

        return({"sql":sql, "bindings": bindings})

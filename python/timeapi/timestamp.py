import datetime
from time import time as tsmp

def full():
    n = datetime.datetime.now()
    y = n.year
    m = n.month
    d = n.day
    h = n.hour
    mi = n.minute
    s = n.second
    da = "-"
    string = str(y)+da+str(m)+da+str(d)+da+str(h)+da+str(mi)+da+str(s)
    return string

def date():
    n = datetime.datetime.now()
    y = n.year
    m = n.month
    d = n.day
    da = "-"
    string = str(y)+da+str(m)+da+str(d)
    return string

def time():
    n = datetime.datetime.now()
    h = n.hour
    mi = n.minute
    s = n.second
    da = "-"
    string = str(h)+da+str(mi)+da+str(s)
    return string

def timestamp():
    string = tsmp()
    return string


# Interactions With CSV
from numpy import genfromtxt

def readdata(fname, incStr=False): 
# read from fname
    if incStr:
        return genfromtxt(fname, skip_header=1, dtype=None, delimiter=',')
    else:
        temp = genfromtxt(fname, skip_header=1, delimiter=',')
        return temp[:,5:]
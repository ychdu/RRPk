# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:47:26 2015

@author: AMD
"""

#imports
import numpy
from iwcsv import readdata

# from scipy import linalg
def standarize1(arr):
    a = arr.mean(axis=0)
    b = arr.std(axis=0)
    trainn = (arr - a[None,:])/b[None,:]
    return trainn, a[-1], b[-1]

def standarize2(arr):
    a = arr.min(axis=0)
    trainn = train - a
    b = trainn.max(axis=0)
    trainn = trainn / b
    return trainn, a[-1], b[-1]

def testw():
    wr = random.random(9)
    p = random.random((9,9))
    r = numpy.dot(p,wr)
    pr = numpy.concatenate((p, r[:, None]), axis=1)
    prn, a, b = standarize1(pr)
    pn = prn[:,:-1]
    rn = prn[:,-1:]
    w = numpy.linalg.lstsq(pn,rn)[0]
    rt = numpy.dot(pn,w)*b+a
    print r - rt.T

    

train = readdata('train.csv')
param = train[:,:-1]
price = train[:,-1:]
trainn, a, b = standarize1(train)
paramn = trainn[:,:-1]
pricen = trainn[:,-1:]#.reshape(-1,1)

w = numpy.linalg.lstsq(paramn, pricen)[0]

pricet = numpy.absolute(numpy.dot(paramn,w)*b+a)

"""
trainn2, a2, b2 = standarize2(train)

paramn2 = trainn2[:,:-1]
pricen2 = trainn2[:,-1:]

w2 = numpy.linalg.lstsq(paramn2, pricen2)[0]

pricet2 = numpy.absolute(numpy.dot(paramn2,w2)*b2+a2)

"""
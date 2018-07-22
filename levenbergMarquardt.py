# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 05:58:08 2017

@author: JUNAID
"""
def finFValue(x0):
    v=1/4*(x0**4)+1/3*(x0**3)-1/2*(x0**2)
    return v

def finDerivativeValue(x0):
    v=(x0**3)+(x0**2)-(x0)
    return v

def newXVal(x,d,a):
    v=x+(a*d)
    return v

#alfa=0.3
#alfa=2
#alfa=0.3
alfa=0.8
#x0=-1.0
#x0=-0.7
#x0=-0.445
#x0=-0.278
################
#p2
#x0=-1.0
#x0=1.0
#x0=3.0
#x0=69.0
#################
#x0=0.0
################
#x0=0.5
#x0=0.4
#x0=0.2592
x0=0.5
iterations=4
def gradientDescent(x0,alfa,iterations):
    for i in range(iterations):
        fVal=finFValue(x0)
        print("function Value:")
        print(fVal)
        derVal=finDerivativeValue(x0)
        print("derivative value:")
        print(derVal)
        newX=newXVal(x0,derVal,alfa)
        print("new x value:")
        print(newX)
        fVal=finFValue(newX)
        print("function updated Value:")
        print(fVal)
        x0=newX

gradientDescent(x0,alfa,iterations)
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 01:28:51 2017

@author: JUNAID
"""

import numpy as np
import cv2

X=list()
X.append([974.64,84.79,1.0])
X.append([1002.11,81.85,1.0])
X.append([938.91,60.76,1.0])
X.append([940.81,55.39,1.0])
X.append([982.48,48.33,1.0])

XPrime=list()
XPrime.append([1010.37,81.95,1.0])
XPrime.append([1151.48,75.10,1.0])
XPrime.append([973.68,58.05,1.0])
XPrime.append([975.28,52.61 ,1.0])
XPrime.append([1018.36,53.09,1.0])

n=5 # because we have 5 points

A=np.zeros((2*n,9))
for i in range(n):
    A[2*i]=[0.0,0.0,0.0,-1.0*(XPrime[i][2])*(X[i][0]),-1.0*(XPrime[i][2])*(X[i][1]),-1.0*(XPrime[i][2])*(X[i][2]),(XPrime[i][1])*(X[i][0]),(XPrime[i][1])*(X[i][1]),(XPrime[i][1])*(X[i][2])]
    A[2*i+1]=[(XPrime[i][2])*(X[i][0]),(XPrime[i][2])*(X[i][1]),(XPrime[i][2])*(X[i][2]),0.0,0.0,0.0,-1.0*(XPrime[i][0])*(X[i][0]),-1.0*(XPrime[i][0])*(X[i][1]),-1.0*(XPrime[i][0])*(X[i][2])]
    
# now we habe A now we can compute SVD of A
U,S,V=cv2.SVDecomp(A)
h=V[8]
H=h.reshape((3,3))
print("homography transformation matrix H is: ")
print(H)
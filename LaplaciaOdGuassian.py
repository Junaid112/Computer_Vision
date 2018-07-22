# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:56:34 2017

@author: JUNAID
"""

import numpy as np
import math 


L=[[0,1,0],[1,-4,1],[0,1,0]]

G=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0625,0.125,0.0625,0.0],[0.0,0.125,0.25,0.125,0.0],[0.0,0.0625,0.125,0.0625,0.0],[0.0,0.0,0.0,0.0,0.0]]


LOG=np.zeros((5,5),dtype=float)
print(LOG)
size=len(LOG)
sizeL=len(L)
for m in range(size):
    for n in range(size):
        sumVal=0
        for i in range(sizeL):
            for j in range(sizeL):
                sumVal=sumVal+(L[i][j]*G[m-i][n-j])
        LOG[m][n]=sumVal

#now I have final LOG matrix
print(LOG)
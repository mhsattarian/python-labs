#!/usr/bin/env python
# coding: utf-8


import numpy as np 
import matplotlib.pyplot as plt


a=[[11,12,13],[21,22,23],[31,32,33]]
a


#every elment if of the same type 
A=np.array(a)
A


A.ndim


A.shape


A.size


A[1,2]


A[1][2]


A[0][0]


A[0][0:2]


A[1:3,2]


X=np.array([[1,0],[0,1]]) 
X


Y=np.array([[2,1],[1,2]]) 
Y


Z=X+Y
Z


Y=np.array([[2,1],[1,2]]) 
Y


Z=2*Y
Z


Y=np.array([[2,1],[1,2]]) 
Y


X=np.array([[1,0],[0,1]]) 
X


Z=X*Y
Z


A=np.array([[0,1,1],[1,0,1]])
A


B=np.array([[1,1],[1,1],[-1,1]])
B


Z=np.dot(A,B)
Z


np.sin(Z)


C=np.array([[1,1],[2,2],[3,3]])
C


C.T





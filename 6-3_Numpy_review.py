#!/usr/bin/env python
# coding: utf-8

import numpy as np


my_list = [0,1,2,3,4]


type(my_list)


np.arange(0,10)


np.arange(0,10,2)


np.zeros((5,5))+5


np.ones((2,4))*7


np.random.randint(0,10)


np.random.randint(0,10,(3,3))


np.linspace(0,10,6)


np.linspace(0,10,101)


np.random.seed(101) # watch video for details
arr = np.random.randint(0,100,10)


arr


arr2 = np.random.randint(0,100,10)


arr2


arr.max()


arr.min()


arr.mean()


arr.argmin()


arr.argmax()


arr.reshape(2,5)


mat = np.arange(0,100).reshape(10,10)


mat


row = 0
col = 1


mat[row,col]


# With Slices
mat[:,col:col+1]


mat[row,:]


mat[0:3,0:3]


a=mat > 50


mat[mat<30]


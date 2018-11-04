#!/usr/bin/env python
# coding: utf-8

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


def Plotvec1(u,z,v):
    #this function is used in code 
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05,color ='r', head_length=0.1)
    plt.text(*(u+0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05,color ='b', head_length=0.1)
    plt.text(*(v+0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z+0.1), 'z')
    plt.ylim(-2,2)
    plt.xlim(-2,2)



def Plotvec2(a,b):
    #this function is used in code 
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05,color ='r', head_length=0.1)
    plt.text(*(a+0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05,color ='b', head_length=0.1)
    plt.text(*(b+0.1), 'b')

    plt.ylim(-2,2)
    plt.xlim(-2,2)


a=["0",1,"two","3",4]


print("a[0]:",a[0])
print("a[1]:",a[1])
print("a[2]:",a[2])
print("a[3]:",a[3])
print("a[4]:",a[4])


import numpy as np 


a=np.array([0,1,2,3, 4])
a


print("a[0]:",a[0])
print("a[1]:",a[1])
print("a[2]:",a[2])
print("a[3]:",a[3])
print("a[4]:",a[4])


a


type(a)


a.dtype


b=np.array([3.1,11.02,6.2, 213.2,5.2])


type(b)


b.dtype


c=np.array([20,1,2,3,4])
c


c[0]=100
c


c[4]=0
c


d=c[1:4]
d


c[3:5]=300,400
c


select=[0,2,3]


d=c[select]
d


c[select]=100000
c


a=np.array([0,1,2,3, 4])
a


a.size


a.ndim


a.shape


a=np.array([1,-1,1,-1])


mean=a.mean()
mean


standard_deviation=a.std()
standard_deviation


b=np.array([1,2,3,4,5])
b


max_b=b.max()


max_b=b.min()


u=np.array([1,0])
u


v=np.array([0,1])
v


z=u+v
z


Plotvec1(u,z,v)





y=np.array([1,2])
y


z=2*y
z





u=np.array([1,2])
u


v=np.array([3,2])
v


z=u*v
z





np.dot(u,v)














u=np.array([1,2,3,-1]) 
u


u+1


np.pi


x=np.array([0,np.pi/2 , np.pi] )


y=np.sin(x)
y


np.linspace(-2,2,num=5)


np.linspace(-2,2,num=9)


x=np.linspace(0,2*np.pi,num=100)


y=np.sin(x)


plt.plot(x,y)





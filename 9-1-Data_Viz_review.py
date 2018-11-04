#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')


x = np.arange(0,10)


y = x**2


y


x


y


plt.plot(x,y)
plt.show()


plt.plot(x,y,'*')


plt.plot(x,y,'b*')


plt.plot(x,y,'r--')
plt.xlim(2,4)
plt.ylim(3,20)
plt.title("Zoomed")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


mat = np.arange(0,100).reshape(10,10)


plt.imshow(mat)


mat = np.random.randint(0,100,(10,10))


plt.imshow(mat)


plt.imshow(mat)
plt.colorbar()





df = pd.read_csv('salaries.csv')


df


df.plot(x='Salary',y='Age',kind='scatter')


df.plot(x='Salary',kind='hist')





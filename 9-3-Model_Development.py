#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# path of data 
path = 'clean_df.csv'
df = pd.read_csv(path)
df.head()


from sklearn.linear_model import LinearRegression


lm = LinearRegression()
lm


X = df[['highway-mpg']]
Y = df['price']


lm.fit(X,Y)


Yhat=lm.predict(X)
Yhat[0:5]   


lm.intercept_


lm.coef_














Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]


lm.fit(Z, df['price'])


lm.intercept_


lm.coef_





# import the visualization package: seaborn
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)


plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)





width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()


Y_hat = lm.predict(Z)


plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()


def PlotPolly(model,independent_variable,dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable,dependent_variabble,'.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_axis_bgcolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
    
print("done")


x = df['highway-mpg']
y = df['price']
print("done")


# Here we use a polynomial of the 3rd order (cubic) 
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)


PlotPolly(p,x,y, 'highway-mpg')


np.polyfit(x, y, 3)





from sklearn.preprocessing import PolynomialFeatures


pr=PolynomialFeatures(degree=2)
pr


Z_pr=pr.fit_transform(Z)


Z.shape


Z_pr.shape


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]


pipe=Pipeline(Input)
pipe


pipe.fit(Z,y)


ypipe=pipe.predict(Z)
ypipe[0:4]


#highway_mpg_fit
lm.fit(X, Y)
# Find the R^2
lm.score(X, Y)


Yhat=lm.predict(X)
Yhat[0:4]


from sklearn.metrics import mean_squared_error


#mean_squared_error(Y_true, Y_predict)
mean_squared_error(df['price'], Yhat)


# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
lm.score(Z, df['price'])


Y_predict_multifit = lm.predict(Z)


mean_squared_error(df['price'], Y_predict_multifit)


from sklearn.metrics import r2_score


r_squared = r2_score(y, p(x))
r_squared


mean_squared_error(df['price'], p(x))


import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


new_input=np.arange(1,100,1).reshape(-1,1)


lm.fit(X, Y)
lm


yhat=lm.predict(new_input)
yhat[0:5]


plt.plot(new_input,yhat)
plt.show()





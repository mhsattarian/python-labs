#!/usr/bin/env python
# coding: utf-8

import numpy as np


from sklearn.preprocessing import MinMaxScaler


data = np.random.randint(0,100,(10,2))


data


scaler_model = MinMaxScaler()


scaler_model.fit(data)


scaler_model.transform(data)


# In one step
result = scaler_model.fit_transform(data)


result


import pandas as pd


data = pd.DataFrame(data=np.random.randint(0,101,(50,4)),columns=['f1','f2','f3','label'])


data.head()


x = data[['f1','f2','f3']] # Alternatively x = data.drop('label',axis=1)
y = data['label']


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)


X_train.shape


X_test.shape


y_train.shape


y_test.shape


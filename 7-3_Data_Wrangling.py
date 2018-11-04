#!/usr/bin/env python
# coding: utf-8

import pandas as pd


filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df = pd.read_csv(filename, names = headers)
print("Done")


# To see what the data set looks like, we'll use the head() method.
df.head()


import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)


missing_data = df.isnull()
missing_data.head(5)


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    


avg_1 = df["normalized-losses"].astype("float").mean(axis = 0)


df["normalized-losses"].replace(np.nan, avg_1, inplace = True)


avg_2=df['bore'].astype('float').mean(axis=0)


df['bore'].replace(np.nan, avg_2, inplace= True)





avg_4=df['horsepower'].astype('float').mean(axis=0)


df['horsepower'].replace(np.nan, avg_4, inplace= True)


avg_5=df['peak-rpm'].astype('float').mean(axis=0)


df['peak-rpm'].replace(np.nan, avg_5, inplace= True)


df['num-of-doors'].value_counts()


df['num-of-doors'].value_counts().idxmax()


#replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace = True)


# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace = True)

# reset index, because we droped two rows
df.reset_index(drop = True, inplace = True)


df.head()


df.dtypes



df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print("Done")


df.dtypes


df.head()


# transform mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data 
df.head()





# replace (origianl value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()





#!/usr/bin/env python
# coding: utf-8

# import pandas library
import pandas as pd


# import pandas library
import pandas as pd
# read the online file by the URL provides above, and assign it to variable "df"
path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(path,header=None)
print("Done")


# show the first 5 rows using dataframe.head() method
df.head(5)





# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
headers


df.columns = headers
df.head(10)


df.dropna(subset=["price"], axis=0)





# check the data type of data frame "df" by .dtypes
df.dtypes


df.describe()


# describe all the columns in "df" 
df.describe(include = "all")





# look at the info of "df"
df.info





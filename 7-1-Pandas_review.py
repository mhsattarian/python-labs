#!/usr/bin/env python
# coding: utf-8

import pandas as pd


df = pd.read_csv('salaries.csv')


df


df['Name']


df['Salary']


df[['Name','Age']]


df['Age']


df['Age'].mean()


df['Age'] > 30


age_filter = df['Age'] > 30


age_filter


df[df['Age'] < 30]


df[df['Age'] > 30]


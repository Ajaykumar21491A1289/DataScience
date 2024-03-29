# -*- coding: utf-8 -*-
"""cw.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18yywvwUSj_epxdBdFD2_zZnf0aV1mIjq

# **cleaning data frame**
"""

import pandas as pd
import numpy as np

df=pd.DataFrame(data=[np.arange(11,16),
             [np.nan,45,56,np.nan,67],
             [56,90,np.nan,67,np.nan]],
             index=['A','B','C'],
             columns=['P','Q','R','S','T'])

df

df.isnull()

df.isna()

df.notnull()

df.fillna(99)

df.isnull().sum().sum()#to print how many empty are there

df

df['P'].isnull().sum()

df.iloc[2:4].sum()

df.iloc[1:2].isnull().sum()

df

df['P']#to access data row wise

df[['P','Q']]

df.loc['A']#location is used for the column wise data to access

df.loc[['A','B']]

df

df.isnull()

df.isnull().sum().sum()#to count not a number values in entier data frame



df.isna().sum()

df.describe()

df.fillna(np.mean(df))

df.dropna()

df

df.dropna(axis=1)

df.dropna(axis=0)

df.fillna(55,inplace=True)

df

df1=pd.DataFrame(data=[np.arange(11,16),
             [np.nan,45,56,'',67],
             [56,90,np.nan,67,'']],
             index=['A','B','C'],
             columns=['P','Q','R','S','T'])

df1


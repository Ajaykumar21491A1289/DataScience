# -*- coding: utf-8 -*-
"""Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wQ4fHWyeWRvfYhsvb1ZPOXaCCo61DNV0
"""

import seaborn as sns
sns.set()

tips=sns.load_dataset('tips')

tips.head()

sns.displot(tips['total_bill'],bins=20,kde=True)

sns.jointplot(x='total_bill',y='tip',data=tips)

sns.pairplot(data=tips)

sns.pairplot(data=tips,hue='sex')

sns.rugplot(tips['total_bill'])

sns.displot(tips['total_bill'],kde=True)

sns.barplot(x='sex',y='total_bill',data=tips)

sns.countplot(x='sex',data=tips)

sns.boxplot(x='day',y='total_bill',data=tips)

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)

sns.stripplot(x='day',y='total_bill',data=tips,hue='sex')

sns.swarmplot(x='day',y='total_bill',data=tips)


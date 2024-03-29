# -*- coding: utf-8 -*-
"""DAWP Exp1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eWlKvbIcFMposCtoeu35GjAYPPt6WZBM

***Aim: Create a IPython notebookto work with following built-in data structures
(a)List (b)Tuple (c) Set (d) Dictionary ***
"""

numbers=[2,3,7,8,9,23,19,18,34,10]
numbers

type(numbers)

colors=['red','green','blue']
colors

#List from range()generator
a_list=list(range(11,18))
a_list

#Accessing elements
numbers[1]
numbers[-2]

#difference b/w print and with out print
print(numbers[1])
print(numbers[-2])
print(numbers)

#Slicing
print(numbers[1:4])
print(numbers[1:-4])
print(numbers[-1:4])
print(numbers[-4:-1])
print(numbers[9:10])
print(numbers[10:9])
print(numbers[::2])

print(numbers[2:-3])
print(numbers[6:-9])
print(numbers[-3:2])
print(numbers[-9:6])

"""**Adding and removing elements in lit**"""

colors

colors.append("yellow")
colors

colors.insert(2,'black')
colors

colors.remove('black')
colors

colors.pop()

colors.pop(2)

colors.pop()
colors

"""**Concatenation and combining list**

"""

a_list=[2,4,6,8]
b_list=[1,3,5,7]

"""**sorting a list**"""

a=[1,4,6,2,3,67,7]
a.sort()
a

b=['saw','small','he','foxes','six']#if same length occurs it will check for first occurence
b.sort(key=len)#it find out length of each element now length of b=[3,5,2,5,3]
b

"""**tuples**"""

tup1=(4,5,6,8,9)
print(tup1)

"""**sets**"""

s1={3,4,5,6}
s2={5,4,3,2,1}
s1.union(s2)

s1.intersection(s2)

s1.difference(s2)

s1.symmetric_difference(s2)

"""**Dictionary**"""

myd={'name':'ajay kumar','roll_no':21491289}
print(myd)
print(myd.keys())
print(myd.values())
print(myd.items())
print(myd['name'])
myd['year']=1
myd.update({'branch':'it','year':2})
print(myd)


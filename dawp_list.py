# -*- coding: utf-8 -*-
"""DAWP-list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vtvKfwOGKQI6tWlhVol1PIMzFhUXomBE

**list:
  -ordered,collection of similar(or)different data elements
  -supports indexing both +ve & -ve
  -mutable
  -created by using [] & seperated by ','
syntax:-
   variable=[v1,v2,v3,---vn]**
"""

even=[2,4,6,8,10]
my_list=[1201,'abc','it',True]

my_list

n=int(input("enter the n value"))
for i in range(0,n):
  for j in range(0,n):
    print("*",end=" ")
  print()

for i in range(0,n):
  for j in range(0,i+1):
    print('*',end=" ")
  print()

for i in range(0,n):
  for j in range(0,n-i):
    print("*",end=" ")
  print()

for i in range(0,n):
  for j in range(0,n-i):
    print(" ",end=" ")
  for k in range(0,i+1):
    print("*",end=" ")
  print()

a=float(int(input()))
print(type(a))

"""**prime numbers
**
"""

n=int(input())
for k in range(2,n*n):
  count=0
  for i in range(1,k+1):
    if(k%i==0):
      count+=1
  if(count==2):
    print(k)
    j+=1
  if(j==n):
    break


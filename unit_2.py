# -*- coding: utf-8 -*-
"""unit-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nQbViSOsASuvgfo5OKCNFJMmaofHQfoY

**universal functions of numpy**
"""

#unary functions
#is abs() - returns absolute  value
import numpy as np
print(np.abs(-2.56))
print(np.abs(np.array([2,-3,4,-5])))
print(np.abs(np.array([-2,3.5,6,-4.56])))

#fabs()-floating point absolute value
np.fabs(-4)
print(np.fabs(np.array([-3,2,-5,9])))
#print(np.fbs([-3.96,-11.5,12.7,-99.99]))

x=np.array([1,2,3,5])
y=np.array([4,0,6,8])
np.divide(x,y)

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:36:53 2021

@author: Aaron Ramirez
"""

import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
# from scipy.interpolate import interpld

data=pd.read_csv('salida.txt',header=1, delim_whitespace=True)
x= data.iloc[:,0]
y= data.iloc[:,1]
# print(data)
# print(x)
# print(y)

plt.plot(x,y,'ro')
plt.ylabel('frecuencia')
plt.xlabel('palabras')
plt.show

coeficientes=np.polyfit(x,y,1)
pilinomio=np.poly1d(coeficientes)
print(pilinomio)

f=interpld(x,y,1)
# print(f('click'))

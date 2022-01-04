# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:12:40 2021

@author: Aaron Ramirez
"""

import matplotlib.pyplot as plt 

filename = "salida.txt"
with open(filename) as f:
 mytext = f.read()
 
from wordcloud import WordCloud
wordcloud = WordCloud().generate(mytext)
#%pylab inline

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("resultado.png")
plt.show()
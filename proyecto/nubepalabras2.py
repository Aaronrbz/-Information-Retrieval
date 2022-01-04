# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:12:59 2021

@author: Aaron Ramirez
"""
import matplotlib.pyplot as plt 
import wordcloud as WordCloud


filename = "salida.txt"
with open(filename) as f:
 mytext = f.read()
 
 
# iniciar un objeto de nube de palabras
alice_wc = WordCloud(background_color='WHITE', max_words=274058, mask=alice_mask, stopwords=stopwords)

# generar la nube de palabras
alice_wc.generate(alice_novel)

# graficar la nube de palabras
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.savefig("resultado.png")
plt.show()
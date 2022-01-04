# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:16:05 2021

@author: Aaron Ramirez
"""
#Abrimos el documento de txt y lo guardamos en una variable
with open('Corpus.txt','r',encoding= "utf8") as miarchivo:
    texto = miarchivo.read()

#Importamos las librerias requeridas.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk

from collections import Counter
from collections import OrderedDict


#las cadenas a continuacion son las consultas que realizaremos
cadena='separation anxiety in infancy (i.e. up to two years of age) and in preschool children, particularly separation of a child from its mother'
#cadena='the toxicity of organic selenium compounds'
#cadena='language development in infancy and pre-school age'
#cadena= '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
#cadena='of not few so on where as no how d before shouldve has weren than will '
#cadena="Perro gato"





#obtenemos las stop_words en el mismo lenguaje que el corpus
stop_words= set(stopwords.words('english'))
word_tokens = word_tokenize(texto) #tookenizar significa utilizar toda la palabra y no solo un caracter
word_tokens1 = word_tokenize(cadena)

##### PREPROCESAMIENTO DEL TEXTO #####

word_tokens = list(filter(lambda token : token not in string.punctuation,word_tokens,)) #Eliminamos caracteres de puntuacón del corpus
word_tokens1= list(filter(lambda token : token not in string.punctuation,word_tokens1)) #Eliminamos caracteres de puntuación de la consulta
filtro=[] #Declaramos una variable de tipo lista que contendrá el corpus una vez finalizado el preprocesamiento
filtro1=[]  #Declaramos una variable de tipo lista que contendrá la consulta una vez finalizado el preprocesamiento
aux=[]#Utilizamos una variable auxiliar para realizar la consulta

for palabra in word_tokens: #iniciamos el ciclo para eliminar stop words
    if palabra not in stop_words:
        filtro.append(palabra)
        
for i in word_tokens1:
    if i not in stop_words:
        filtro1.append(i)
        
        
##### CONSULTA DE TEXTO #####        
for palabra1 in filtro1: #Recorremos la lista de consulta
    if (palabra1 in filtro): #Preguntamos si la palabra se encuentra en el corpus
        aux.append(filtro.index(palabra1)) # Si la consulta es verdadera obtenemos el indice

##### Imprimimos en donde se encuentran las coincidencias #####

if(len(aux)==0): #si la lista de coincidencias esta vacia se regresa que no hubo coincidencias
    print("Match not found")
else:
    for j in range(0,len(aux)):
        print("{} found on {}".format(filtro1[j],aux[j])) #Imprimimos Las coincidencias 



c=Counter(filtro) # Obtenemos la propiedad contador de la libreria usada
# fdist=nltk.FreqDist(filtro) # Usamos una funcion de la libreria para obtener la frecuencia el 
#                             #la distribución del corpues preprocesado
# fdist.plot(20,cumulative=True) #Graficamos los primeros 20 téminos más usuales



##### GUARDAMOS EL CORPUES PREPOSESADO #####
y=OrderedDict(c.most_common())

with open('salida.txt','w') as file:
    for k,v in y.items():
        file.write(f'{k} ' )
        
        
        
        
        
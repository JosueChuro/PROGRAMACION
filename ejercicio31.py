# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:57:38 2022

@author: Josue
"""
lista1=0
vector=0
import random 
while lista1>5 or lista1<30:    
    def vector (n):
        vector=[0]*n
        for i in range (n):
            vector[i] =random.randint(6,29)
        return vector
    print ("Ingrese el tamaño de la lista: ")
    n=int(input())
    resultado=vector(n)
    print(resultado)
    break
while vector>5 or vector<30:    
    j=str('Que operacion matematica desea hacer?: ')
print(j)
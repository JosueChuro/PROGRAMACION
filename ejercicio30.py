# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:36:39 2022

@author: Josue
"""

import random 

def vector (n):
    vector =[0]*n
    for i in range (n):
        vector[i] =random.randint(5,30)
    return vector
print ("Ingrese los numero aleatorio: ")
n=int(input())

aleatorios=vector(n)
print(aleatorios)
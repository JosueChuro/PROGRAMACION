# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:47:46 2022

@author: Josue
"""

n=[0]*7
for i in range (1,7):
    num=int(input("Ingrese un numero: "))
    n[i]=num
for i in range (7):
    print("El valor de",i,"de la lista es: ",n[i])
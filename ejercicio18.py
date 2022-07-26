# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:37:07 2022

@author: Josue
"""
numero = input("Ingrese un numero palidromo: ")

def palidromo_num (string):
    x=""
    for i in  string:
        x= i + x
    return x
if numero== palidromo_num (numero):
    print("El numero si es palidromo")
else:
    print("El numero no es palidromo")

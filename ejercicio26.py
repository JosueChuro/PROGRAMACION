# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:41:30 2022

@author: Josue
"""

def esPrimo(n):
    if n <=1:
        return False
    elif n==2:
        return True
    
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    

for i in range (0,51):
    print(i," ",esPrimo(i))
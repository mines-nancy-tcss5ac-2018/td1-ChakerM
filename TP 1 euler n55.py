# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:48:56 2018
probleme euler 55
@author: memmadi1u
"""

# verifie si le nombre est un palindrome
def verification(n):
    n=str(n)
    i=len(n)//2+1
    for j in range(i+1):
        if n[j] != n[-j]:
            return False
    return True
    
def verification50():
    i=0
    while i<51:

    
    
    

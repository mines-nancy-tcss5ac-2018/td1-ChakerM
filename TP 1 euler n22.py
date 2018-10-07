# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:39:52 2018
TP1 
@author: MEMMADI Chaker
"""

#trier les noms de la liste du fichier
def trier_liste():
    buffer=[]
    for line in open('p022_names.txt','r'):
        buffer.append(line)
    L= (buffer[0]).split(',')
    L.sort()
    return L

#on évalue chaque nom et on associe tous les scores dans une liste
def evalue(L):
    L2=[]
    for i in range(len(L)):
        S=0
        #la boucle suivante calcule le score d'un seul nom
        for j in range(1,len(L[i])-1): 
            S+=ord(L[i][j])-64       
        L2.append(S)
    return L2 #on obtient une liste avec les scores de chaque nom par ordre alphabétique

#fonction finale donnant le score des noms)
def solve():    
    S=0
    L= trier_liste()
    L2=evalue(L)
    for i in range(len(L)):
        S+=L2[i]*(i+1)
    return S

print(solve())
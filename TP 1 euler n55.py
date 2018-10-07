# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:48:56 2018
TP1
probleme euler 55
@author: MEMMADI Chaker
"""

# verify if n is a palyndrom
def verification(n):
    if str(n)[::-1]==str(n):
        return True
    else:
        return False
#verify if under 50 iterations the number does not become a palyndrom
def verification50(n):
    i=0
    while i<50:              # we iterate the process less than 50 iteration
        if verification(n):  # we test if the number is a palyndrom
            return False
        else:
            m=int(str(n)[::-1]) #m is the reversed number n
            n=n+m     
            i+=1
    return True   #if after 50 iterations there is no palyndrom it returns True   
            
def solve(): #final function that gives the number of Lychrel below ten-thousand 
    Lycherel_number=0
    for n in range(10000):
        if verification50(n):
            Lycherel_number+=1
    return Lycherel_number

print(solve())
                 
    

    
    
    

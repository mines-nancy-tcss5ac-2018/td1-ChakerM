# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

TP1
Euler n16

"""
"we want to solve the 16th Euler problem"

"this function return the sum of the digits of the number"

n=2**1000

def solve(n):
    S=0
    m=str(n)
    for i in range(len(m)):
        S+=int(m[i])
    return S

print(solve(n))
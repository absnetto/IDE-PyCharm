#coding:utf-8
from math import sqrt

def lista2(x):
    lista = list(x)
    a = ""
    b = ""
    count = 0
    for l in lista:
        if l == " ":
            count += 1
        elif count == 0:
            a += l
        #elif count == 1:
        else:
            b += l
    return float(a), float(b)

x1, y1 = lista2(input())
x2, y2 = lista2(input())

distancia = sqrt(((x2-x1)**2)+((y2-y1)**2))

print("%.4f" %distancia)

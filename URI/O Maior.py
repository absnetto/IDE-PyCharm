#coding:utf-8

def lista3(x):
    lista = list(x)
    a = ""
    b = ""
    c = ""
    count = 0
    for l in lista:
        if l == " ":
            count += 1
        elif count == 0:
            a += l
        elif count == 1:
            b += l
        else:
            c += l
    return int(a), int(b), int(c)

def maiorAB(x,y):
    return (x+y+abs(x-y))/2


a, b, c = lista3(input())

ab = maiorAB(a,b)
xc = maiorAB(ab,c)

print("%i eh o maior" %xc)


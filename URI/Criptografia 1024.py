#coding:utf-8

def passada1(texto):
    novotexto = ""
    for s in texto:
        if s.isalpha():
            s = chr(ord(s)+3)
        else:
            s = s
        novotexto += s
    return novotexto


def passada2(texto):
    novotexto = list(texto).sort(reverse=True)
    return novotexto


def passada3(texto):
    return texto


N = int(input())
qtde = 0
lista = []
while qtde < N:
    lista.append(input())
    qtde+=1


for l in lista:
    l = passada1(l)
    l = passada2(l)
    #x = passada3(l)
    print(l)

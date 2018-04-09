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
    texto2 = list(texto)
    texto2.reverse()
    novotexto = ""
    for s in texto2:
        novotexto += s

    return novotexto


def passada3(texto):
    tamanho = (len(texto))
    meio = tamanho//2
    texto1 = texto[0:meio]
    texto2 = texto[meio:tamanho] #meio+1 aqui no no item anterior...
    novotexto = ""
    for s in texto2:
        s = chr(ord(s)-1)
        novotexto += s

    return texto1+novotexto


N = int(input())
qtde = 0
lista = []
while qtde < N:
    if (1 <= N <= (10**4)):
        lista.append(input())
        qtde+=1
    else:
        break

for l in lista:
    l = passada1(l)
    l = passada2(l)
    l = passada3(l)
    print(l)

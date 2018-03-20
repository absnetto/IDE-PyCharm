# Escreva uma função que receba como argumento uma lista que
# poderá ter valores duplicados e retorne uma nova lista sem
# que haja valores iguais.
# Lista: [1,2,3,3,3,3,4,5]
# Retorno: [1, 2, 3, 4, 5]


def unico(l=[]):
    l = set(l)
    print(l)
    return l

lista = [1,2,3,3,3,3,4,5]
unico(lista)
print(lista)

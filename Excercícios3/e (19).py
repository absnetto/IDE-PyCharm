# Escreva uma função que imprima somente os números pares
# Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Saída: [2, 4, 6, 8]

def eh_par(*lista):
    lista = list(set(lista))
    lista.sort()
    par = []
    for x in lista:
        if  x%2==0:
            par.append(x)
    return par


print(eh_par(1,4,6,8,9,6,4,6,8,3))


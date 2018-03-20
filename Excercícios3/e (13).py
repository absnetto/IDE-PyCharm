# Escreva uma função que inverta a ordem dos elementos
# de uma lista manualmente. Não utilize a função interna
# do Python que faz inverção, crie o algoritmo que faça a inversão.
# Lista: "1234abcd"
# Saída: "dcba4321"


def inverte(*lista):
    listainvertida = ""
    tam = len(lista)

    while (tam > 0):
        listainvertida += lista[tam-1]
        tam -= 1

    return (listainvertida)

lista = tuple("1234abcd")
inverte(*lista)



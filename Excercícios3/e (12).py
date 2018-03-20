# Escreva uma função que multiplique todos os números de uma lista.

def somalista(*lista):
    soma = 1
    for l in lista:
        soma *= l
    return soma

lista = [1, 2, 3, 4, 5]

somalista(*lista)
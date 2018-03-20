# Escreva um função que some todos os números contidos numa lista.

def somalista(*lista):
    soma = 0
    for l in lista:
        soma += l
    return soma

lista = [1, 2, 3, 4, 5]

somalista(*lista)
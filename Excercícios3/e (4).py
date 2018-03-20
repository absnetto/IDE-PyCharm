# Escreva um algoritmo contendo uma função que necessite
# de três argumentos. Em seguida, imprima na tela os
# argumentos em ordem ascendente e, por fim, imprima a média aritmética:


def func(x, y, z):
    lista = [x, y, z]
    lista.sort()
    print(lista)

    media = (x+y+z)/3
    print(media)


func(5,10,1)

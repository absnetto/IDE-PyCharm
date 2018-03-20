# Escreva uma função que aceite Strings e calcule a quantidade
# de letras em mauisculas e minúsculas que a String possui.

def qtdeUpperLow(x):
    listax = list(tuple(x))
    low = 0
    upper = 0
    for a in listax:
        if a.islower():
            low += 1
        elif a.isupper():
            upper += 1

    print("O Total de Letras minúsculas é de", low, "e o total de letras maiúsculas é de", upper)
    return


frase = input("Digite uma frase: ")
qtdeUpperLow(frase)
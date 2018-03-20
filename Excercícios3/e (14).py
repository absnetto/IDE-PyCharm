# Escreva uma função que calcule o fatorial de
# um número (um inteiro não negativo). Envie o valor
# do número que será calculado como argumento da função.

def fatorial(x):
    x1 = x
    if (x >=0 and x <=1):
        return print("Fatorial de", x1 , "é 1")
    elif (x<0):
        print("O número não pode ser negativo!")
        return
    else:
        res = 1
        while (x > 1):
            res *= x
            x -= 1
        return print("Fatorial de", x1 , "é", res)


num = int(input("Qual número deseja como fatorial?:"))
fatorial(num)


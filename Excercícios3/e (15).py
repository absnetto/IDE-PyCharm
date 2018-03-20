# Escreva uma função que verifique se um número está num intervalo determinado.

def intervalo(num=0, intI=0, intF=0):
    menor = min(intI, intF)
    maior = max(intI, intF)

    if (menor <= num <= maior):
        print("Está na faixa")
    else:
        print("Não está na faixa")

intervalo(10,3,19)
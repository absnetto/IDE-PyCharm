# Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros
# e imprima na telas os números primos contidos nessa lista.


def eh_primo(*lista):
    #lista = list(lista)
    lista = list(set(lista))
    lista.sort()
    num_ini = 0
    num_fim = max(lista)
    primos = []
    multiplos = []
    contidos = []
    if num_fim > 0:
        #primos = []
        #multiplos = []

        for n in range(num_ini, num_fim + 1, 1):
            if n in multiplos:
                continue
            if (n > 1 and (n not in multiplos)):
                #primos += [str(n)]
                primos.append(n)
                #        if n<=11:
                multiplos += list(range(num_ini, num_fim + 1, n))
        #print(primos)
        #print(len(primos))


        #for l in lista:
        #    for p in primos:
        #        if (l == p):
        #            contidos.append(l)


    contidos = list(set(lista).intersection(primos))
    contidos.sort()
    print(contidos)


numeros = 1,2,3,56,89,100
eh_primo(*numeros)

# Escreva um algoritmo que encontre o maior dentre 3 números.
# Para facilitar a resolução do exercício utilize funções.

def max(x,y,z):
    num = [x,y,z]
    num.sort()
    return num[len(num)-1]

print(max(7,3,4))


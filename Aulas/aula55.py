'''num_ini = int(input("Digite o numero inicial: "))
num_fim = int(input("Digite o numero Final: "))

for n in range(num_ini ,num_fim + 1,1):1
    print(n)
''

num_ini = 0  #int(input("Digite o numero inicial: "))
num_fim = 100 #int(input("Digite o numero Final: "))
invert = False

for n in range(num_fim if invert else num_ini + 1 ,num_ini if invert else num_fim  + 1, 1 if not invert else -1):
    print(n)
'''

"""
num_ini = 0  #int(input("Digite o numero inicial: "))
num_fim = 100 #int(input("Digite o numero Final: "))

soma_par = 0
for n in range(num_ini,num_fim  + 1, 2):
    print(n)
    if n%2==0:
        soma_par += 1
print(soma_par)
"""

num_ini = 0
num_fim = 1

while num_fim != 0:
    num_fim = int(input("Type the final number: "))
    primos = []
    multiplos = []

    for n in range(num_ini, num_fim + 1, 1):
        if n in multiplos:
            continue
        if (n>1 and  (n not in multiplos)):
            primos += [str(n)]
#        if n<=11:
            multiplos += list(range(num_ini,num_fim+1,n))
    print(primos)
    print(len(primos))
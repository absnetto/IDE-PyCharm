pedido = 0
total = 0
while pedido < 2:
    x = input()
    lista = list(x)
    cod = ""
    num = ""
    val = ""
    count = 0
    for l in lista:
        if l == " ":
            count += 1
        elif count == 0:
            cod += l
        elif count == 1:
            num += l
        else:
            val += l

    num = int(num)
    val = float(val)
    total += (num*val)
    pedido += 1

print("VALOR A PAGAR: R$ %.2f" %total)

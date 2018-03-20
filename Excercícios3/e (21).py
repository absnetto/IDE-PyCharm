# Escreva uma função que tenha definida uma função em seu escopo.
# Invoque a função aninhada, retorne algum valor, imprima esse
# valor na tela e finalize a aplicação.


def func1():

    def func2():
        return "oi"

    print(func2())
    return

func1()



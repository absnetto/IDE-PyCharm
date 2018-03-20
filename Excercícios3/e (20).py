# Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

def palindromo(frase=""):
    fraseoriginal = frase.upper().replace(" ","")
    fraseinversa = ""
    for n in fraseoriginal[::-1]:
        fraseinversa += n
    if fraseoriginal==fraseinversa:
        print("A string é um palíndromo")
    else:
        print("A string não é um palíndromo")

palindromo("Ame ô poemA")
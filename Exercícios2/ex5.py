# coding: utf-8
# Faça um algoritmo que peça a idade do
# usuário e a idade da sua mãe. Em seguida,
# imprima na tela com quantos anos sua mãe o teve.

you = int(input("Digite sua idade:"))
mom = int(input("Digite a idade de sua mãe:"))

print("Quando você nasceu, sua mãe tinha aproximadamente %i anos." %(mom-you))

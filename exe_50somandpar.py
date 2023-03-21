#um programa que pegue 6 numeros eu some somente os pares

var_01 = (int(input('primeiro numero: ')))
var_02 = (int(input('segund numero: ')))
var_03 = (int(input('terceiro numero: ')))
var_04 = (int(input('quarto numero: ')))
var_05 = (int(input('quinto numero: ')))
var_06 = (int(input('sexto numero: ')))

numeros = [var_01 , var_02 , var_03 , var_04 , var_05 , var_06]

cont = 0
for c in numeros:
    if c % 2 ==0:
        cont = cont + c

print (f'A soma to total dos numeros pares é de {cont}')


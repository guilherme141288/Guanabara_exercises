#variavel para o valor do produto
var_01 = float(input('Qual é o preço do produto? '))

#variavel para adicionar o valor do desconto
var_03 = float(input('qual a porcentagem do desconto?'))
var_04 = 100 - var_03

#variavel para o calculo do desconto
var_02 = (var_01 / 100) * var_04

print (f'O produto que custava R${var_01}, com desconto de {var_03}% vai custar R$ {var_02:.2f}')
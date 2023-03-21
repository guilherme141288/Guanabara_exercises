#input do primeiro valor
var_01 = float(input('Qual o salário do funcionário? R$'))

#input do valor do aumento em porcentagem
var_02 = float(input('Qual a porcentagem do aumento? '))


#calculo para o novo valor
var_04 = (var_01 / 100) * var_02
var_05 = var_01 + var_04

print (f'{var_05:.2f}')
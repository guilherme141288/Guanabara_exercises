#input do numero
var_01 = int(input('Informe um numero: '))

print (f'Unidade: {var_01 // 1 % 10}')
print (f'Dezena: {var_01 // 10 % 10}')
print (f'Centena: {var_01 // 100 % 10}')
print (f'Milhar: {var_01 // 1000 % 10}')
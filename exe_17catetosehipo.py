#input do primeiro cateto
var_01 = float(input('Comprimento do cateto oposto: '))


#input do segundo cateto
var_02 = float(input('Comprimento do cateto adjacente: '))

#calculando e imprimindo
print (f'A hipotenusa vai medir {(var_01 ** 2 + var_02 ** 2) ** (1/2):.2f}')
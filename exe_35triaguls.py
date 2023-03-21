#testando se os numeros podem formar um triangulo

print ('~~'*30)
print ('Analizandor de triângulos')
print ('*-*'*20)

var_01 = float(input('Primeiro segmento: '))
var_02 = float(input('Segundo segmento: '))
var_03 = float(input('Terceiro segmento: '))

podem = '\033[4;35;40mPODEM\033[m'
nao_podem = '\33[4;35;40mNÃO PODEM\033[m'


if var_01 < var_02 + var_03 and var_02 < var_03 + var_01 and var_03 < var_02 + var_01:
    print(f'Os segmentos acima {podem} formar um triângulo')
else:
    print(f'Os segmentos acima {nao_podem} formar um triângulo')    
#R$60 por dia e R$0,15 por quilometro rodado

#input do dias 
var_01 = int(input('Quantos diass alugados? '))

#input dos quilometros rodados
var_02 = int(input('quantos KMs rodados? '))

#calculo do valor
print (f'O total a pagar é de R${(var_01 * 60) + (var_02 * 0.15):.1f}')
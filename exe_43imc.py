#calculando indice de massa corporal (IMC)

peso = float(input('Qual o peso? '))

altura = float(input('Qual a altura? '))

calculo = peso / (2 * altura)

print (f'O IMC dessa pessoa é de {calculo:.2f}')

if calculo <= 18.5: print('Abaixo do peso')
elif calculo <= 25 and calculo > 18.50: print('Peso ideal')
elif calculo <= 30 and calculo > 25: print ('Sobrepeso')
elif calculo <= 40 and calculo > 30: print ('Obesidade')
elif calculo >= 40: print ('Obesidade morbida')
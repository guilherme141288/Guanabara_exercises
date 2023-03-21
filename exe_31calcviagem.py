#input da distancia da viagem, essa distancia pode ser automatizada pegando valores do google maps

var_01 = float(input('Qual a distancia da viagem? '))

print (f'Você esta prestes a começar uma viagem de {var_01}Km.')

if var_01 <= 200:
    
    print(f'O preço da passagem será de R${var_01 * 0.50:.2f}')

elif var_01 > 201 :

    print(f'O preço da passagem será de {var_01 *0.45:.2f}')    


elif var_01 < 1000:

    print(f'O valor da passagem será de {var_01 * 0.30:.2f}')
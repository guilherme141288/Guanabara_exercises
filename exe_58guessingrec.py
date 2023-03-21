import random

print ('Sou seu computador...')

random_num = random.randint(1 , 10)

print ('''Acabei de pensar em um numero de 1 - 10
Será que voce consegue adivinhar?''')
print (random_num)
palpite = (int(input('Qual é seu palpite: ')))


tent = 1



while palpite != random_num:
    palpite = (int(input('Qual é seu palpite: ')))
    if palpite < random_num:
        print ('Mais... tente mais uma vez')
        tent = tent + 1
        
    elif palpite > random_num:
        print('menos...tente mais uma vez')
        tent = tent + 1
        
        

print (f'Acertou com {tent} tentativa(s). Parabéns')














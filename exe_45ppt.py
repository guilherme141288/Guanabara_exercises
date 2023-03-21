#jogo papel, pedra, tesoura> randomizando resultados


from random import randint
import random

print ('''Suas opções:
[ 0 ] PAPEL
[ 1 ] PEDRA
[ 2 ] TESOURA''')

jogada = int(input('Qual a sua jogada? '))
game =[ 'papel' , 'pedra' , 'tesoura' ]
computador = randint(0 , 2)
print (computador)
print (jogada)
print(f'computador jogou {game[computador]}')
print(f'o jogador jogou {game[jogada]}')

if computador == jogada:
    print ('Empate')
elif computador == 0 and jogada == 2:
    print ('Jogador venceu')
elif computador == 1 and jogada == 0:
    print ('Jogador venceu')
elif computador == 2 and jogada == 1:
    print('jogador vence')    
else:
    print ('Computador venceu')    

   
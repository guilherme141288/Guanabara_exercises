import random

var_01 = input('Primeiro aluno: ')
var_02 = input('Segundo aluno: ')
var_03 = input('Terceiro aluno: ')
var_04 = input('Quarto aluno: ')


var_05 = [var_01 , var_02 , var_03 , var_04]

#determinando o sorteado
print (f'O aluno escolhido foi {random.choice(var_05)}')
import random

var_01 = input('Primeiro: ')
var_02 = input('Segundo: ')
var_03 = input('Terceiro: ')
var_04 = input('Quarto: ')

#lista para sorteo da ordem
var_05 = [var_01, var_02 , var_03 , var_04]
random.shuffle(var_05)
print (f'a ordem da apresentação será {var_05}')
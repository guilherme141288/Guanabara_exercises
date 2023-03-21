#progressão aritmetica usando while loop
from time import sleep
print ('''Gerador de PA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

var_01 = int(input('Primeiro termo: '))
var_02 = int(input('Razão da PA: '))

termo = var_01
cont = 1

while cont <= 10:

    print (f'{termo} > ', end='')
    termo += var_02
    cont += 1
    

print ('FIM')
#calculando fatorial de um numero
#fatorial sendo aquele numero multiplicado pelos seus antecessores (ex: fatorial de 6 = 6 x 5 x 4 x 3 x 2 x 1 = 720)
import math

var_01 =  int(input('''Digite um numero para
calcular seu Fatorial: '''))
ac = var_01
while ac > 0:
    print (f'{ac}', end='')
    print (' x ' if ac > 1 else ' = ' , end='' )
    ac -= 1
       


fat = math.factorial(var_01)

print (f'{fat}')
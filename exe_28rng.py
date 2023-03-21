import random

#random number generator
var_01 = random.randint(0 , 5)

#input da escolha 
var_02 = int(input('Em que numero pensei? '))

if var_02 == var_01:
    print ('acerto mizeravi')
else:
    print('errou!!')


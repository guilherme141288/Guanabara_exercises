#progressao aritmetica com continuacao de razao

print ('''Gerador de PA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

var_01 = int(input('Primeiro termo: '))
var_02 = int(input('Razão da PA: '))

termo = var_01
cont = 1
total = 0
var_03 = 10

while var_03 != 0:
    total = total + var_03
    while cont <= total :
    
    
    
        print (f'{termo} > ', end='')
        termo += var_02
        cont += 1

    print ('PAUSA')

    var_03 = int(input('Quantos termos voçê quer mostrar a mais?  '))    


print (f'Progressão finalizada com {total} de termos mostrados')

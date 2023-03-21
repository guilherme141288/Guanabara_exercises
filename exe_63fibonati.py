#encontrando os termos de fibonatti

var_01 = int(input('Quantos termos você quer mostrar? '))

ini = 0
first = 1
then = ini + first
termos = 1

while termos <= var_01:
    print (f'{then} > ', end='')
    termos += 1
    
    then = ini + first
    ini = first
    first = then
print ('Fim')    
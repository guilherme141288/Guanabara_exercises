#identificando numero primo



input_numero = int(input('Digite o numero que deseja consultar: '))


tot = 0
for c in range (1 , input_numero + 1 ):
    if input_numero % c == 0:
        tot += 1
if tot == 2:
    
    print('é um numero primo')

else: print('não é um numero primo')
    
    #print(f' {c} ' , end='')
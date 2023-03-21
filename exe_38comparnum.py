#comparando 2 numeros inteiros

var_01 = int(input('Digite o primeiro numero: '))
var_02 = int(input('Digite o segundo numero: '))

if var_01 > var_02:
    print ('O primeiro valor é maior')
elif var_02 > var_01:
    print ('O segundo valor é maior')
elif var_01 == var_01:
    print ('Não existe valor maior, os dois são iguais')        
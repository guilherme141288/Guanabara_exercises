#conversor de bases numericas, transformando numero inteiros em BINARIO, OCTAL e HEXADECIMAL

var_01 = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversâo: 

[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para Hexadecimal''')

var_02 = int(input('Sua opção: '))

if var_02 == 1:
    print (f'{var_01} convertido para BINÁRIO é igual a {bin(var_01)[2:]}')

elif var_02 == 2:
    print (f'{var_01} convertido para OCTAL é igual {oct(var_01)[2:]}')

elif var_02 == 3:
    print (f'{var_01} convertido para HEXADECIMAL é igual a {hex(var_01)[2:]}')
else:
    ('Opção invalida, tente novamente')    
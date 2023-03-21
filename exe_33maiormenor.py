#identificando o maior e o menor valor

var_01 = int(input('Primeiro valor: '))
var_02 = int(input('Segundo valor: '))
var_03 = int(input('Terceiro valor: '))

#encontrando o menor o menor
menor = var_01
if var_02 < var_01 and var_02 < var_03:
    menor = var_02
if var_03 < var_01 and var_03 < var_02:
    menor = var_03    

#encontrando o maior
maior = var_01
if var_02 > var_01 and var_02 > var_03:
    maior = var_02
if var_03 > var_01 and var_03 > var_02:
    maior = var_03         

print (f'O menor valor digitado foi {menor}') 
print (f'O maior valor digitado foi {maior}')   


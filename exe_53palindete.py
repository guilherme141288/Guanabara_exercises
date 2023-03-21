#exercicio 53, playlist 'exercicios de python 3' #detector de Palindromo

var_01 = str(input('Digite uma frase: ')).strip().upper()

var_02 = var_01.split()

junto = "".join(var_02)
inverso = ""

for letra in range(len(junto) -1 , -1 , -1):
    inverso += junto[letra]

print(f'O contrario da frase {junto} é {inverso}')    

if junto == inverso:
    print('A frase digitada é um palindromo')
else:
     print('A frase digitada não é um palindromo')   
#contando multiplos de 3
#inicia-se criando variaveis para comçar a contagem
soma = 0
cont = 0

for c in range(1, 501 , 4):
    if c % 3 ==0:
        soma = soma + c
        print (c)
    cont + cont + 1    

print (f'a soma dos multiplos de 3 nos 500 primeiro numeros é {soma}')    
#menu de opções, alguma relação entre 2 numeros digitados

import time

prim = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
time.sleep(0.2)
acao = int(input(''' >>>>>> Qual é a sua opção? 
 [ 1 ]  somar
 [ 2 ]  multiplicar
 [ 3 ]  maior
 [ 4 ]  novos números
 [ 5 ]  sair do programa:
       '''))


time.sleep(1)
while acao != 5:
    
    if acao == 1:

        print (f'o resultado de {prim} + {seg} é {prim + seg}')
    
    if acao == 2:

        print (f'O resultado de {prim} x {seg} é {prim * seg}')

    if acao == 3:
        maior = [prim , seg]
        maior.sort()
        print (f'Entre {prim} e {seg} o maior valor é {maior[1]}')
    if acao == 4:

        prim = int(input('Primeiro valor: '))
        seg = int(input('Segundo valor: '))
    print('==========================================================================')
    time.sleep(4)
    acao = int(input(''' >>>>>> Qual é a sua opção? 
 [ 1 ]  somar
 [ 2 ]  multiplicar
 [ 3 ]  maior
 [ 4 ]  novos números
 [ 5 ]  sair do programa:
       '''))

print('Programa encerrado')
exit()


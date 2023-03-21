#identificador de maioridade

from datetime import date



pri = int(input('Em que ano a 1º pessoa nasceu? '))
seg = int(input('Em que ano a 2º pessoa nasceu? '))
ter = int(input('Em que ano a 3º pessoa nasceu? '))
qua = int(input('Em que ano a 4º pessoa nasceu? '))
qui = int(input('Em que ano a 5º pessoa nasceu? '))
sex = int(input('Em que ano a 6º pessoa nasceu? '))
set = int(input('Em que ano a 7º pessoa nasceu? '))



atu = date.today() .year #usando a data atual como refencia

validpri = atu - pri
validseg = atu - seg
validter = atu - ter
validqua = atu - qua
validqui = atu - qui
validsex = atu - sex
validset = atu - set

group = [validpri , validseg , validter , validqua , validqui , validsex , validset]

print (f'o ano atual é {atu}')

countold = 0
countyou  = 0

for c in group:
    if c >= 18:
        countold = countold + 1
    else:
        countyou = countyou  + 1

print (f'{countold} pessoas sao maiores') 

print (f'{countyou} pessoas sao de menores')
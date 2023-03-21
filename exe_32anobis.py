#identificando ano bissesto
#identificando um elemento a cada 4

var_01 = int(input('Que ano quer analisar?'))

if var_01 % 4 == 0:

    var_02 = var_01

    if var_02 <= 2021:
        print('esse ano foi bissesto')

    elif var_02 >= 2022:
        print('esse ano será bissesto')
else:

    var_03 = var_01

    if var_03 <= 2021:
        print('esse ano não foi bissesto')
    elif var_03 >= 2022:
        print('esse ano não será bissesto')
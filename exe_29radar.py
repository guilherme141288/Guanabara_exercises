#input da velocidade, normalmente pego de forma automatica
var_01 = int(input('Qual é a velocidade atual do carro? '))


if var_01 <= 80:
    print ('Tenha um bom dia! Dirija com segurança!')

elif var_01 >= 81:
    print ('Multado! você excedeu o limite peromitido que é de 80km/h')

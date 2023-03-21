#somando valores ate uma ordem de parada ser executada

var_01 = int(input('Digite um número [999 para parar]: '))
var_02 = 0
var_03 = 0

while var_01 != 999:
    
    var_04 = var_01 + var_03
    var_03 += var_01 
    var_02 = var_02 + 1
    #print (var_01 , var_02 , var_03 , var_04)
    var_01 = int(input('Digite um número [999 para parar]: '))

print (f'Você digitou {var_02} números e a soma entre eles foi {var_03}.')
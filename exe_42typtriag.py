#identificando o tipo de triagulo

var_01 = int(input('Primeiro segmento: '))
var_02 = int(input('Segundo segmento: '))
var_03 = int(input('Terceiro segmento: '))


if var_01 > var_02 + var_03 or var_02 > var_01 + var_03 or var_03 > var_02 + var_01:
    print ('Nâo é possivel formar um triangulo com esse segmentos') 
elif var_01 == var_02 and var_02 == var_03 :
    print ('Os segmentos acima formam um triagulo Equilatero')        
elif var_01 == var_02 or var_02 == var_03:
    print ('Os segmentos acima formam um triangulo Isosceles')
elif var_01 != var_02 and var_02 != var_03:
    print ('Os segmentos acima formam um triangulo Escaleno')


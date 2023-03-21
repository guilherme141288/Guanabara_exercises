#identificando se o numero é par ou impar

from ast import Return




try:
    
    var_01 = int(input('Me diga um numero qualquer: ')) 
    
    
    
    if var_01 %2 == 0:
        print('é um numero par')
    else:
        print('é um numer impar')

except:
    print('tem que inserir somente numeros')
           
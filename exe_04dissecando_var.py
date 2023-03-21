#variavel usada para o input
var_01 = input('Digite algo: ')


#ver o valor primitivo
print ('O tipo primitivo desse valor é ' , type(var_01))

#checar se foi inserido somente espacos
print ('so tem espaço?' , var_01.isspace())

#testar se tem somente numeros em um input
print ('é um numero ?' , var_01.isnumeric())

#testar para ver se tem somente letras em um input
print('é alfabetico?' , var_01.isalpha())

#testar se é alphanumerico(numeros e letras)
print ('é alphanumerico? ' , var_01.isalnum())

#testar se esta em letras maiusculas 
print ('esta em maiusculas? ' , var_01.isupper())

#testar se esta em letras minusculas
print ('esta em minuscula? ' , var_01.islower())

#testar se esta capitalizada
print ('esta capitalizada? ' , var_01.istitle())


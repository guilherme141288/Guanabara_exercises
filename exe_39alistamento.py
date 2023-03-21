#identificando se é necessario o alistamento de acordo com a idade



#primeira parte levando em consideração somente o ano


var_01 = int(input('Qual o ano de nascimento? '))


#(1)quantos anos atras deveria ter se alistado, (2)e em que ano deveria ter se alistado
var_02 = 2003 - var_01 + 1

var_03 = 2022 - var_02

#(1)em quantos anos irá se alistar(2)em que ano deverá se alistar 

var_04 = var_01 - 2005 + 1

var_05 = 2022 + var_04

#idade da pessoa
var_06 = 2022 - var_01

print (f'quem nasceu em {var_01} tem {var_06} anos em 2022')

if var_01 <= 2003:
    print(f'''Ja passou da hora de se alistar
    voce deveria ter se alistado a {var_02} anos atras em {var_03}''')

elif var_01 == 2004:
    print('esta na hora de se alistar')    

elif var_01 >= 2005:
    print(f'''voce ainda vai se alistar
    voçe irá se alistar em {var_04} anos em {var_05}''')



#resolução usando calendario, necessario importar date(ex: from datetime import date)


#






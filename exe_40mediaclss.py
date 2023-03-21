#tirando media de 2 numeros

var_01 = float(input('Primeira nota: '))

var_02 = float(input('Segunda nota: '))

var_03 = (var_01 + var_02) / 2

print (f'Tirando {var_01} e {var_02}, a média é {var_03}')

if var_03 <= 70 and var_03 > 0:
    print ('O aluno está \033[4;35;40mREPROVADO\033[m')

elif var_03 >= 70:
    print ('O aluno está \033[4;32;40mAPROVADO\033[m ')    

elif var_03 == 0:
    
    var_04 = input('O aluno ira fazer segunda chamada? (s)para sim, (n)para nâo :') 
    if var_04 == 's':
        print ('A segunda chamada sera daqui 2 dias')
    elif var_04 == 'n':
        print ('Aluno está \033[4;35;40mREPROVADO\033[m ')       
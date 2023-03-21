



val = str(input('Informe seu sexo: [M/F] ')).strip().upper()


while val != 'F' and val != 'M':
    
    
    val = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()
    


if val == 'M':
    print('Sexo masculino registrado com sucesso')
    
elif val == 'F':
    print('Sexo feminino registrado com sucesso')
    
    

   
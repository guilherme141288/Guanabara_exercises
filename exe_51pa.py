print ('='*40)
print ('10 TERMOS DE UMA PA')
print ('='*40)

primeiro_termo = int(input('Primeiro termo: '))           
razao = int(input('razao: '))
decimo = primeiro_termo + (10- 1) * razao     #calculo usado para encontrar os numeros da PA

for c in range(primeiro_termo  , decimo + razao , razao ):    #range muito importante para a coleta de dados aqui. 
                                                              #"primeiro_termo" indica o começo do loop, 
                                                              #"decimo + razao"  indica ate onde vai o loop
    print ((f"{c}") , end= ' > '  )                           #"razao" indica de quantos em quantos ele vai pular


print ('Acabou')

  

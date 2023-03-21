#contando somente pares em uma estrutura de loop
from time import sleep
#for pares in range(1 , 51):
    
    #destacando os pares dos numeros
    #if pares % 2 == 0:
        #print(pares )
        #sleep(0.2)

#outra forma de fazer é adicionando o intervalo dentro do range
for pares in range(0 , 51 , 2): #sendo que o terceiro numero indica o intervalo
    print(pares)
    sleep(0.2)
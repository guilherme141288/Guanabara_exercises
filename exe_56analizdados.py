gnome = []
gidade = []
gsexo = []

per = tuple (gnome , gidade)
fe = 0


for c in range(1 , 5):
    print (f'----- {c}º PESSOA -----')
    
    nome = str(input('Nome: '))
    gnome += [nome]
    
    idade = int(input('Idade: '))
    gidade += [idade]
    
    sexo = str(input('Sexo [M/F]: ').upper())
    
    
    if sexo == 'F' and idade < 20:
        fe += 1 

    elif sexo == 'M':
        sexo = 'Masculino'
    else:
        sexo = 'Feminino' 
    
        

    gsexo += [sexo]


#print (gnome , gidade , gsexo)  

media = float(gidade[0] + gidade[1] + gidade[2] + gidade[3]) / 4
print (f'A média de idade do grupo é de {media} anos')

gidade.sort()



print (f'A pessoa mais velha tem {gidade[3]} anos ')

print(f'Ao todo são {fe} mulheres com menos de 20 anos')




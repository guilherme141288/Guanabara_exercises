#encontrando o maior e menor numero em um grupo


#criando uma list vazia e adicionando elementos pelo 'for loop'
group = []

#inputs using for loop, in this case retrieving 5 positions
for pessoa in range (1 , 6):
    peso = float(input(f'Peso da {pessoa}º pessoa: '))
    group += [peso]



group.sort()

print (f'O maior peso lido foi de {group[4]}')
print (f'O menor peso lifod foi de {group[0]}')
   
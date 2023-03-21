
#parametros de busca
var_palavra = str(input('Qual palavra/frase deseja procurar? ')).strip().upper()

#coletando o nome/texto
var_01 = (input('Qual é o seu nome/texto completo: ')).strip().upper()

#variavel para boleano
var_03 = var_palavra in var_01

#encontrando strings em textos, informação especifica pra levantamento de dados, bem comun para pratica de scraping
print (f'Há esse(a)palavra/frase no texto? {var_03} ')


if var_03 is True:

    #numero de palavras/letras no texto
    print (f'a letra/frase {var_palavra} aparece {var_01.count(var_palavra)} vezes na frase')

    #posição da primeira palavra/letra
    print (f'a primeira letra {var_palavra} aparece na posição {var_01.find(var_palavra)+1}')

    #posição da ultima palavra/letra
    print (f'a ultima letra {var_palavra} aparece na posição {var_01.rfind(var_palavra)+1}')

else:
    print ('Palavra/letra não encontrado')
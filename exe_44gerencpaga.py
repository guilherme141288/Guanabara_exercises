#gerenciador de pagamento com 4 opçoes, e uma subopção

valor_compras = float(input('Preço das compras: R$'))

print ('\033[4;32;40mFORMAS DE PAGAMENTO\033[m')

print ('''[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao_client = int(input('Qual é a opção? '))

valor_a_vista = valor_compras - ((valor_compras / 100) * 10 )
valor_cartao = valor_compras - ((valor_compras / 100) *5 )
valor_prazo = valor_compras + ((valor_compras / 100) *20)

if opcao_client == 1:
    print (f'À vista no pix/dinheiro, sua compra de R${valor_compras} sai por R${valor_a_vista} com desconto de 10%.')

elif opcao_client == 2:
    print (f'À vista no cartão, sua compra de R${valor_compras} sai por R${valor_cartao} com desconto de 5%. ')    

elif opcao_client == 3:
    print (f'Em 2x no cartão, a parcela sai por {valor_compras / 2} com o primeiro pagamento para dia 10')  

elif opcao_client == 4:
    
    
    vezes = int(input('Em quantas vezes deseja parcelar: '))
    if vezes >= 21 : print('O maximo numero de parcelas é 20')
    
    else: print (f'em {vezes} parcelas, O valor total das compras sai por R${valor_prazo:.2f} e a parcela fica R${valor_prazo / vezes:.2f} com um acrescimo de 20%')

else:
    print('Opçao invalida')
   
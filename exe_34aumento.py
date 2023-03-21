#aumento em porcentagem

var_01 = float(input('Qual é o salário do funcionário? R$'))

var_02 = float(input('Qual a porcentagem do aumento? '))


if var_01 <= 5000:
    print(f'quem ganhava R${var_01} com um aumento de {var_02}%, passa a ganhar R${(var_01 / 100 * var_02) + var_01} ')

else:
    print(f'Quem ganhava R${var_01} passa a ganhar {(var_01 / 100 * 10) + var_01}')    
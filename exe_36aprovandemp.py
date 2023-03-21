#determinando condição para aprovação de algo, filtros, determinando tresholds

#analizando credito(guanabara) 

var_01 = int(input('Valor da casa: '))

var_02 = int(input('Qual o salário do comprador: '))

var_03 = int(input('Quantos anos para pagar: '))

#calculando o valor da parcela
var_04 = var_01 / (var_03 * 12) 

#calculando 30% do salario
var_05 = var_02 / 100 * 30

if var_04 >= var_05:
    print (f'Para pagar uma casa de R${var_01} em {var_03} anos, a parcela será de R${var_04:.2f}\n\33[4;28;40mEmpréstimo NEGADO!\033[m') 
else:
    print (f'Para pagar uma casa de R${var_01} em {var_03} anos, a parcela será de R${var_04:.2f}\n\33[4;34;40mEmpréstimo CONCEDIDO!\033[m')    
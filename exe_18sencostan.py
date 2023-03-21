import math

#input do angulo
var_01 = float(input('Digite o ângulo que voce deseja: '))

print (f'O ângulo de {var_01} tem o seno de {math.sin(math.radians(var_01)):.2f} \nO cosseno de {var_01} é {math.cos(math.radians(var_01)):.2f}\nA tangente de {var_01} é {math.tan(math.radians(var_01)):.2f}')
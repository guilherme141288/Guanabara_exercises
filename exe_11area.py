#input do primeiro elemento para area(largura)
var_01 = float(input('Largura da parede: '))

#input do segundo elemento da area(altura)
var_02 = float(input('Altura da parede: '))

print (f'Sua parede tem a dimensão de {var_01}x{var_02} e sua área é de {var_01 * var_02:.2f}m2')
print (f'Para pintar essa parede é necessario {(var_01 * var_02) / 2:.2f}l de tinta')


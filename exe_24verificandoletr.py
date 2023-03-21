
var_01 = str(input('em que cidade voce nasceu? ')).strip()



print (var_01[:5].upper()  == 'SANTO')

var_02 = bool(var_01)


if var_02 == True:
    print ('deu boa')

if var_02 == False:
    print ('continue procurando')

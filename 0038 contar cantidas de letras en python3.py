# Pedir al usuario la frase que desea ingresar
# preguntar al usuario la letra que quiere validar las repeticiones

'''
Usando for
'''
frase = str(input('Introduce la frase que deseas validar: ')).lower()
letra =  str(input('Introduce la letra que quieres contavilizar: ')).lower()
contador = 0
for i in range (len(frase)):
    if letra == frase[i]:
        contador = contador + 1
    else:
        print('la letra \'{}\' no es igual a \'{}\' '.format(letra,frase[i]))
print('la letra \'{}\' se conto \'{} veces\' '.format(letra,contador))

# usando la funcion count

frase2 = str(input('Introduce la frase que deseas validar: ')).lower()
letra2 =  str(input('Introduce la letra que quieres contavilizar: ')).lower()

letter_couting = frase2.count(letra2)
print('El mensaje original es  || {} ||'.format(frase2))
print('La letra que quiere ver cuantas veces se repite es \'{}\' la cual se repitio \'{}\' veces'.format(letra2,str(letter_couting)))
            

# crear un codigo que cuente el numero de vocales en una frase
# Pedir la frase al usuario

'''
Metodo simple
'''

frase = str(input('Introduce la frase para contar sus vocales: ')).lower()
vocales = 'aeiou'
count = 0
for i in range (len(frase)):
    for j in range(len(vocales)):
        if frase[i] == vocales[j]:
            count = count + 1
print('Cantidad de vocales en la frase || {} || es \'{}\' '.format(frase,count))


# Metodo 2 con def

frase2 = str(input('Introduce la frase que quieres validar su cantidades de vocales: '))
def contadorVocales(frase2):
    vocales2 = 'aeiou'
    count2 = 0

    for k in range (len(frase2)):
        letra_i = frase2[k]
        #print(letra_i)

        if letra_i in vocales2:
            count2 += 1
    return f'La cantidad de Vocales en la Frase es  {count2}'

print(contadorVocales(frase2))

    

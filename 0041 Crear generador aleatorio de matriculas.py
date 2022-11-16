# crear Generador de Matriculas Aleatorias
# se importa la libreria random

import random

matriculas_totales = int(input('Introduce la cantidad de matriculas a realizar: '))

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
numeros = '0123456789'

for i in range(matriculas_totales):
    #genera los numeros
    num1= random.choice(numeros)
    num2= random.choice(numeros)
    num3= random.choice(numeros)
    num4= random.choice(numeros)
    # Genera las letras
    letra1 = random.choice(alfabeto)
    letra2 = random.choice(alfabeto)
    letra3 = random.choice(alfabeto)

    print('{}{}{}{}  -  {}{}{}'. format(num1,num2,num3,num4,letra1,letra2,letra3))




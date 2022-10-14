'''
Strings y listas
List slicing
'''

'''string son inmutables'''

str= 'para cada uno, uno diferente, del todo'
print(str[6])

'''los index negativa de izquierda a derecha y positivo de derecha a izquierda '''

'''
     incluido : no incluido : opcional
str[start: end: step]
'''

print(str[0:3])
''' string de 0 hasta antes del 6'''
print(str[0:6])
'''
de inicio al final start
'''
print(str[5:])

'''
Ir de donde inica hasta el end
'''

print(str[3:])
''' usar negativos o positivos'''
print(str[3:-4])

'''
invertir string
'''
print(str[::-1])

'''
saltos con negativos
'''
print(str[-10::-1])

print("parametro step se usa para hacer saltos en la impresion de la cadena")
print(str[2::3])
print(str[-16::-2])

print("""
Escribir la siguiente frase y descomponer
DontForgetToSubscribite
1.-Forget
2.-Forget
3.-Forget
4.-tegroF
5.-tegoto
6.-DontForgetToSub
""")
xstr = "DontForgetToSubscribite"
print(xstr[4:10])
""" inicia del espacio cuatro al 10 sin contar el 10 """
print(xstr[-19:-13])
'''inicia de derecha a izquierda del menos 19 a la derecha menos 13 '''
print(xstr[4:-13])
'''Corta de ambos lados la cadena'''
print(xstr[9:3:-1])
'''invertirlista'''
print(xstr[-14::-2])
print("imprimir final de 2 en dos")
print(xstr[:-8])




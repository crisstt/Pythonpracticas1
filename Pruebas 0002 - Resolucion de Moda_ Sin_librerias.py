#       0 1 2 3 4 5 6  7  8  9 10 11 12 13
lista = [1,3,5,4,3,2,9,10,10,1,8,7,6,10]
lista2 =[]
lista_repeticiones = []
numero = 0
for i in range (len(lista)):
    cont = 0
    if lista[i] != '*':
        for k in range (i,len(lista)):
            if lista[k] != '*':
                numero = lista[i]
                if numero == lista[k]:
                    cont += 1
        lista_repeticiones.append([numero,cont])
        lista2.append(lista[i])
        for s in range(i,len(lista)):
            if numero == lista[s]:
                lista[s] = '*'

modar = 0
modan = [] 
for x in range(len(lista_repeticiones)):
    if lista_repeticiones[x][1] > modar:
        modar = lista_repeticiones[x][1]
        modan = lista_repeticiones[x]
    elif lista_repeticiones[x][1] < modar:
        modar = modar
   
print('''
La calificacion que mas se repite es : {} | {} veces
'''.format(modan[0], modan[1]))                  

print(lista2)          
print(lista_repeticiones)


cantidad_numeros = int(input('Introduce la cantidad de numeros a validar : '))
lista_numeros = [int(input('Introduce los numeros a la lista \"Numero {}\" '.format(i+1))) for i in range(cantidad_numeros)]
new_list = []

for i in lista_numeros:
    if i%2 == 0:
        new_list.append(i // 10)
    elif i%2 != 0: 
        new_list.append(i)

print(lista_numeros)
print(new_list)

# metodo una linea elegante forlist

lista_restada = [i//10 for i in lista_numeros if i%2 == 0]
print(lista_restada)
        
        

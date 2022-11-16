# cuantas veces aparecen las palabras en una frase

frase = str(input('Introduce la frase para contar sus frases repetidas: '))
# se usa split para recortar las frases en palabras y agregarlos a una lista solit('que usar de separador')
frase_separada = frase.split(' ')
dic_palabras = {}
count = 0

for i in range(0, len(frase_separada)):
#captura la primera palabra del primer valor de la lista
    pri_palabra = frase_separada[i]
    
    for k in range(0, len(frase_separada)):
#introduce la segunda y se agrega en el espacio de k
        seg_palabra = frase_separada[k]
#comparar la primera y la segunda si son iguales suma
        if pri_palabra == seg_palabra:
            count += 1
            #                Key llave           Valor value
    dic_palabras[pri_palabra] = count
    count = 0

print(dic_palabras)
        

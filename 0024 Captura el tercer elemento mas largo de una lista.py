# usando sort, sorted, reverse, def
# pedir la lista que se agregara de cadenas texto
# vizualizar la 3ra frase o palabra mas larga

n_texts = int(input("Cuantas frases piensa agregar: "))

list_texts = [input("Introduce la Frase a Agregar : ") for i in range(n_texts)]

list_texts.sort(key = len, reverse = True )
print(list_texts)
print("La 3er Frase mas Larga es : ", list_texts[2])

new_list_sort = sorted(list_texts, key = len, reverse = True)
print(new_list_sort)
print("La 3er Frase mas Larga es : ", new_list_sort[2])

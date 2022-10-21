print("""
limita la cantidad de letras de la siguiente frase
La vida es Grandiosa Aun Sin Tì \n
""")
str = "La vida es Grandiosa Aun Sin Tì"

print("\nExpresa las Primeras 2 Palabras\n")
print("clasica : %.7s"% str)
print("\nExpresa las 3 palabras\n")
print("Usando Format : {0:.10s}".format(str))
print("\nQue se visibilise 3 caracteres\n")
print(format(str, '.3s'))

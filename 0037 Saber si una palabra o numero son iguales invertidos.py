print('Introduce la palabra o numero para saber si se lee igual arreves: ')
word = input('Introduce el Dato a Verificar su Lectura Arreves: ')
word_lower = word.casefold() # Ignora si es mayuscula o minuscula
word_split = word_lower.split(' ') # split para dividir la palabra por lo que se marca en este caso espacio
word_join = ''.join(word_split) # unir lo que hay en word_split

revword = word_join[::-1] # invertir la palabra
print(revword)

if (word_join == revword):
    print('La palabra {} se lee Igual'.format(word))
else:
    print('La palabra {} no se lee Igual'.format(word))

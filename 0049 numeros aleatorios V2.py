import random

n_oculto = random.randint(1,10)
numero = int(input("Introduce el numero para comparar: "))

while True:
    if numero == n_oculto:
        print("Felicitaciones encontraste el numero: {}".format (n_oculto))
        break
    elif numero < n_oculto:
        print("El numero que buscas es mayor a {} ".format(numero))
        numero = int(input("Introduce el numero para comparar: "))
    elif numero > n_oculto:
        print("el numero que buscas es menor a {} ".format(numero))
        numero = int(input("Introduce el numero para comparar: "))

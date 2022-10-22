sumaPares = 0
sumaImpares = 0
numeros_pares = []
numeros_impares = []


try:
    num = int(input("Introduce cuantos numeros vas a calcular en total : "))
except ValueError:
    print("No es un numero")
else:
    for i in range (0, num + 1):
        if i%2 == 0:
            numeros_pares.append(i)
            sumaPares += i
        else:
            numeros_impares.append(i)
            sumaImpares += i
    print("Los numeros Pares de 0 a {} son : {} \n".format(num, numeros_pares))
    print("La suma de los numeros Pares es : ", sumaPares)
    print("\nLos numeros Impares de 0 a {} son : {} \n".format(num, numeros_impares))
    print("La suma de los numeros Impares es : ", sumaImpares)
     
    

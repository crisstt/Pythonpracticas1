# Sumar n cantidad de numeros y egregarlos a una lista
list_n_numeros = []
suma = 0

n_numeros = int(input("Introduce la cantidad de digitos a sumar 0 a N : "))

for i in range (n_numeros + 1):
    list_n_numeros.append(i)
    suma += i
print("Lista a sumar :\n", list_n_numeros)
print("Suma de los numeros agregados es : ", suma)

# Codigo dentro de funcion
print("\nSiguiente resultado usando funciones")
def sumaNNumeros (num):
    sumas = 0
    for i in range (num + 1):
        sumas += i
    print("La suma de los numeros agregados es",sumas)
    
sumaNNumeros(int(input("Ingresa numeros a sumar de 0 a N: ")))

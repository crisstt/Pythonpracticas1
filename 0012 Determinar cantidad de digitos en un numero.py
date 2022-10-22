"""
Convertir los valores dados en Absolutos por medio de abs
"""

num = int(input("Introduce un Numero Entero "))
num = abs(num)
print("Tu Numero es : ", num)
print("Tu Numero es : {} ".format (num))
print("Tu numero es : %d " %num) 

count = 0

while num > 0: # mientras que numero sea mayor a cero
    num //= 10 # divide y quita un cero cada vez
    print("num //= 10 resultado : ",num)# ver como se divide
    count += 1  # si cumple la condicion al final suma 1 al contador
    print(count) # ver como se suma
print ("Cantidad de Digitos del numero agregado es : ", count)

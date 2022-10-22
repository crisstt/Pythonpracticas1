#Saber si un numero es par o impar y agregarlo a una lista usando while
numeros_impares=[]
numeros_pares=[]

n_numeros = int(input("Cantidad de Numeros a validar si son pares e impares "))
count = 0

while (count < n_numeros):
    num = int(input("Introduce numero a Validar si es par o impar : "))
    if num%2 == 0:
        numeros_pares.append(num)
        print("El Numero {} es Par ".format (num))
        count += 1
    else:
        numeros_impares.append(num)
        print("El Numero {} es Impar ".format (num))
        count += 1
print("Numeros Pares son : \n", numeros_pares)
print("Numeros Impares son : \n",numeros_impares)

#Encontrar la cantidad de numeros pares o impares que tiene una lista dada por el usuario
list1 = []
list_par =[]
list_impar =[]
n_par = 0
n_impar = 0
n_numeros_lista = int(input("Cantidad de valores en la lista : "))

for n in range (n_numeros_lista):
    n = int(input("Numero a Agregar a la Lista : "))
    list1.append(n)
    
for k in range(n_numeros_lista):
    if list1[k]%2 == 0:
        list_par.append(list1[k])
        n_par += 1 
    else:
        list_impar.append(list1[k])
        n_impar += 1
        
print("\nLista generada por valores de usuario \n",list1)
print("Los Numeros Pares son: \n",list_par)
print("La cantidad de numeros Pares son: \n",n_par)
print("Los Numeros Impares son: \n", list_impar)
print("La cantidad de numeros Impares son: \n", n_impar)

# con funciones

def par_impar (max_list, lista_numeros):
    count_par = 0
    count_impar= 0
    lista_par = []
    lista_impar = []

    for h in range(max_list):
        if (lista_numeros[h]%2 == 0):
            lista_par.append(lista_numeros[h])
            count_par += 1
        else:
            lista_impar.append(lista_numeros[h])
            count_impar += 1
    print("\nLos numeros Pares son : ",lista_par)
    print("Cantidad de numeros pares son : ",count_par)
    print("\nLos numeros Impares son : ",lista_impar)
    print("Cantidad de numeros impares son : ", count_impar)

par_impar (5,[1,2,3,45,8])
# par_impar (max_list,lista_numeros)    

    
       
       
       


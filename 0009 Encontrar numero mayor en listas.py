print("Encontrar el numero mayor de la siguiente listas")
print("\nUsando una lista creada, por ingresos de usuario")
list1 = []
num_list_1 = int(input("Ingrese numero inicial del intervalo "))
num_list_2 = int(input("Ingrese numero final del intervalo "))
"""
Primer Estilo

"""
if num_list_1 < num_list_2:
    for i in range(num_list_1,num_list_2 + 1):
        list1.append(i)
    print("Lista creada : ",list1)
elif num_list_2 < num_list_1:
    for i in range(num_list_2,num_list_1 + 1):
        list1.append(i)
    print("Lista creada : ",list1)
else:
    print("No existe intervalo en los datos dados\n")
print("\nVisualizar la lista de mayor a menor usando sort")
list1.sort()
print("Lista de menor a mayor", list1)
num_mayor = list1[-1]
print("Numero Mayor de la list1 es: {}". format(num_mayor))

"""
Segundo Estilo

"""
list2 = []
num_elementos = int(input("\nIngresa cantidad de elementos a ordenar y saber el mayo "))
for i in range(num_elementos):
    cada_elemento = int(input("\nIngresa Numero a la lista "))
    list2.append(cada_elemento)
print("Lista creada : ",list2)
list2.sort()
print("Lista acomodada de menor a mayor : ",list2)
print("El numero mayor es", list2[-1])

"""
Tercer Estilo

"""

list3 = []
num_elementos = int(input("\nIngresa cantidad de elementos a ordenar y saber el mayo "))
for i in range(num_elementos):
    cada_elemento = int(input("\nIngresa Numero a la lista "))
    list3.append(cada_elemento)
num_mayor2 = list3[0]

for k in list3:
    if k > num_mayor2:
        num_mayor2 = k
print("Lista creada : ",list3)        
print("El numero Mayor es : ", num_mayor2)

"""
Cuarto Estilo   Funciones

"""
def num_mayor_list (nums):
    numMayor = nums[0]
    for i in nums:
        if i > numMayor:
            numMayor = i
    print("\nse obtienen los siguientes valores usando")
    print("Se crea lista A traves de funciones")
    print("Lista Creada : ", nums)
    print("El numero mayor de la lista es : ", numMayor)

num_mayor_list([2,5,8,10,15,20,25,32,-2])
"""
Cuarto Estilo   Funciones           input

"""
def numeroMayorList (list_numeros):
    numeroMayor = list_numeros[0]
    for i in list_numeros:
        if i > numeroMayor:
            numeroMayor = i
    print("Lista Creada : ", list_numeros)
    print("El numero mayor de la lista es : ", numeroMayor)
numero_en_lista = []
rango_lista = int(input("\nIngresa cantidad de numeros de la lista para sacar el mayor "))
for _ in range(rango_lista):
    numero_en_lista.append(int(input("Agrega numero a la lista : ")))
print("lista Creada para validar el mayor : ", numero_en_lista)

numeroMayorList(numero_en_lista)

"""
Quinto funciones  Max() Min()

"""
def numeroMayor_list (lista_numeros):
    numeroMayor_list = max(lista_numeros)
    print("\nSe obtienen los siguientes valores usando max()  min() : ")
    print("Lista Obtenida",lista_numeros)
    print ("\nNumero mayor obtenido de la lista por medio de max() : ",numeroMayor_list)

numeroMayor_list([2,-10,-20,100,20,15,20])


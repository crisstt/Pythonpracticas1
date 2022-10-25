# Calculadora sencilla usando funciones, if, for, while, seleccion de errores

def suma (nums):
    n_lista = []
    suma_n = 0
    suma_n2 = 0
#opcion 1
    for i in range(nums):
        num = float(input('Agregar numero {} de {} : '. format(i+1,nums)))
        n_lista.append(num)
        suma_n += num
    print(suma_n)
#opcion 2
    for n in range(len(n_lista)):
        suma_n2 += n
    print(suma_n2)  
        
def resta (num):
    n_lista = []   
#opcion 1
    resta_n = 0
    for i in range(nums):
        num = float(input('Agregar numero {} de {} : '. format(i+1,nums)))
        n_lista.append(num)
        #n_lista[0] *= -1
        if resta_n == 0:
            resta_n = num
        else:
            resta_n = resta_n - (num)
    print(n_lista)         
    print(resta_n)
#opcion 2
    resta_n2 = 0
    for n in range(nums):
        if resta_n2 == 0:
            resta_n2 = (n_lista[0])
        else:
            resta_n2 = resta_n2 - (n_lista[n])
    print(resta_n2)
def multiplicacion (nums):
    n_lista = []   
#opcion 1
    resultado = 1
    for i in range(nums):
        num = float(input('Agregar numero {} de {} : '. format(i+1,nums)))
        n_lista.append(num)
        resultado = resultado * num
    print(n_lista)         
    print(resultado)
#opcion 2
    for n in range (nums):
        resultado = resultado * n_lista[n]
def division (numerador,denominador):
    res = numerador / denominador
    print(res)

print ('''
Operación a Realizar :
1) Suma
2) Resta
3) Multiplicación
4) División
''')
continuar = "1"

while (continuar == "1" or continuar == "si"):
    
    try:
        operacion = int(input("Introduce seleccion de operación  1  |  2  |  3  |  4  \n"))
    except ValueError:
        print("Selecion no valida Intentar")
        continue
    else:
        if operacion == 1:
            nums = int(input('Cuantos numeros Sumaras '))
            suma(nums)
        elif operacion == 2:
            nums = int(input('Cuantos numeros Restaras '))
            resta(nums)
        elif operacion == 3:
            nums = int(input('Cuantos numeros  Multiplicaras '))
            multiplicacion(nums)
        elif operacion == 4:
            numerador = float(input('Introduce el numerador  '))
            denominador = float(input('Introduce el denominador '))
            division(numerador,denominador)
        else:
            print("Eleccion Equivocada")
    print('''
Desea continuar con las operaciones
1) SI
2) NO
''')
    continuar = input('Ingrese su respuesta : ').lower()
    
        
        

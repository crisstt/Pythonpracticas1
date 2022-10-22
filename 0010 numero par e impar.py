"""
Basica de impar o par

"""
print("Ingresar numero para saber si es par o impar")
number = int(input("Ingresa un numero entero "))

if number%2 == 0:
    print("El numero {} es Par ".format (number))
else:
    print("El numero {} es Impar ".format (number))

"""
Impar o Par validacion de datos

"""
while True:
    try:
        num = int(input("\nIntroduce un Numero para validar si es Par o Impar "))
    except ValueError:
        print("No es un valor entero")
        continue
    else:
        if num%2 == 0:
            print("El numero {} es Par ".format (num))
        else:
            print("El numero {} es Impar ".format (num))
        
    


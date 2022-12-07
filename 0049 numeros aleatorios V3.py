import random
'''
Adivina el numero
0) informacion inicial (reglas del juego e instrucciones).
1)Número secreto se genera de forma automatica.
2) Se informa al usuario del numero de intentos que le quedan.
3) Al final del juego se informa al usuario sobre todos los numeros usados
    (tratando de buscar el numero oculto).
4) Al final del juego, se informara al usuario cuantos intentos se requirieron. 

'''

n_oculto = random.randint(1,20)
intentos_max = 6
n_usados = []
intentos = 0

print("Adivina el numero, usando los numeros del 1 Al 20")

while intentos < intentos_max:
    try:
        numero = int(input("Adivina el numero escoje del 1 al 20 : "))
        if numero < 21 and numero > 0:
            n_usados.append(numero)
            intentos += 1
           
        else:
            numero = int(input("Adivina el numero escoje del 1 al 20 : "))
            if numero < 21 and numero > 0:
                n_usados.append(numero)
                intentos += 1
                
    except   ValueError:
        print("Error intente de nuevo")
      
    else:
        if numero < 21 and numero > 0:
            if numero == n_oculto:
                in_sobrantes = intentos_max - intentos
                print("""Felicidades el numero que {} es el numero oculto:
Numero de intentos Totales: {}
Numero de Intentos Usados: {}
Numero de  Intentos Sobrantes: {}
Numeros Usados: {}
""". format(numero,intentos_max,intentos,in_sobrantes,n_usados))
                break
            elif numero < n_oculto:
                print("El numero que buscas es Mayor : ")
                
            elif numero > n_oculto:
                print("El numero que buscas es Menor : ")
else:
    in_sobrantes = intentos_max - intentos
    print("""El numero Oculto es {}:
Numero de intentos Totales: {}
Numero de Intentos Usados: {}
Numero de  Intentos Sobrantes: {}
Numeros Usados: {}
""". format(n_oculto,intentos_max,intentos,in_sobrantes,n_usados))
    
    
    
            
            
            

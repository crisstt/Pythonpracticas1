# Encuentra al jugador oculto
"""
Para este ejemplo se mostrara la primera letra del jugador y la ultima, el resto
Se sustituira con --- ejemplo Cristiano "C-------O"
Cada vez que se adivine un jugador se contara un punto

"""
import random

def adivinarNumero(score,inten,inten_max):
    n_random =random.randint(0,(len(list_player)-1))
    player_ocult = list_player[n_random]
    print(player_ocult[0] + "-" * (len(player_ocult)-2) + player_ocult[-1])
    print("""
Se introduce la lista de nombres cargados
{}
""".format(list_player))
    while inten < inten_max:
        name_player = input("Introduce el Nombre que crees que es: ").lower()
        if player_ocult == name_player:
            print("Felicidades, el Nombre es  {} ". format(player_ocult))
            score += 1
            inten += 1
            print("""
Tus puntos son : {}
Intentos hasta ahora: {}
Intentos maximos : {}
""". format(score,inten,inten_max))
            print("Se crea otro nombre para adivinar: ")
            print("El nombre a adivinar es: ")
            n_random =random.randint(0,(len(list_player)-1))
            player_ocult = list_player[n_random]
            print("""
La lista de nombres para escojer
""". format(list_player))
            print(player_ocult[0] + "-" * (len(player_ocult)-2) + player_ocult[-1])
            if inten == inten_max:
                print("""
Tus puntos son : {}
Intentos hasta ahora: {}
Intentos maximos : {}
""". format(score,inten,inten_max))
        else:
            inten += 1
            print("""
Tus puntos son : {}
Intentos hasta ahora: {}
Intentos maximos : {}
""". format(score,inten,inten_max))
                
            
star = "1"


while star == "1" or star == "si":
    score = 0
    inten_max = 6
    inten = 0
    print("""
Para el siguiente juego introducir la cantidad de jugadores a escribir y agregarlos

""")
    max_player = int(input("Introduce la cantidad de nombres de jugadores a usar: "))
    list_player = [input("Introduce los nombres de a usar en el juego: ") for i in range(max_player)]
    print("""
Luego de introducir los jugadores se comienza con el juego, adivina quien es acumularas puntos.
y en caso de agotar tus oportunidades el juego terminara
""")
    """
Jugador a Adivinar

"""
    adivinarNumero(score,inten,inten_max)
    star = input("""
Desea Continuar
1) SI
2) NO
""").lower()

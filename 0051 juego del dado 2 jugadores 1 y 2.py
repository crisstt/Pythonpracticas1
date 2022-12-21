import random
import time

def addList(listplayer1,listplayer2):
    if sum(listplayer1) >  sum(listplayer2):
        print("El Ganador es el Jugador 1 con un Acomulado de {} puntos". format(sum(listplayer1)))
    elif sum(listplayer1) < sum(listplayer2):
        print("El Ganador es el Jugador 2 con un Acomulado de {} puntos". format(sum(listplayer12)))
    else:
        print("Los dos Jugadores Tienen los Mismos Puntos \t|| JUGADOR 1 : {} ||\t || JUGADOR 2 : {} || ". format(sum(listplayer1),sum(listplayer2)))
  
    

    
other = "1"

while other == "1" or other == "si":
    listplayer1 = []
    listplayer2 = []
    lanzamiento = 0
    print("""
Usando el siguiente codigo podemos simular el lanzamiento de un dado.
Tomando en cuenta que existen dos jugadores.
Luego se compara los resultados y se muestra el ganador del tiro.
""")
    lanzamientos = int(input("Cantidad de lanzamientos a validar: "))
    while lanzamiento != lanzamientos:
        print("PREPARANDO EL LANZAMIENTO #{} DEL JUGADOR 1.......". format(lanzamiento+1))
        time.sleep(2.5)
        player1 = random.randrange(1,7)
        print("Lanzamiento del jugador 1 es: {}". format( player1))
        time.sleep(1)
        print("ESPERANDO EL LANZAMIENTO #{} DEL JUGADOR 2.......... ". format(lanzamiento+1))
        time.sleep(2.5)
        player2 = random.randrange(1,7)
        print("Lanzamiento del jugador 2 es {}". format(player2))
        time.sleep(1)
        print("DETERMINANDO EL GANADOR DEL LANZAMIENTO #{} : ". format(lanzamiento+1))
        time.sleep(2.5)
        if player1 > player2:
            print("Lanzamiento {0} \tJugador 1 = {1} \tJugador 2 = {2} \tentonces el ganador es:  Jugador 1 con el numero {1} \n". format(lanzamiento+1,player1,player2))
            listplayer1.append(player1)
            time.sleep(2.5)
        elif player1 < player2:
            print("Lanzamiento {0} \tJugador 1 = {1} \tJugador 2 = {2} \tentonces el ganador es: Jugador 2 con el numero {2}\n". format(lanzamiento+1,player1,player2))
            listplayer2.append(player2)
            time.sleep(2.5)
        else:
            print("Lanzamiento {} \tJugador 1 = {} \Jugador 2 = {} \t los numeros son iguales: \n". format(lanzamiento+1,player1,player2))
            time.sleep(2.5)
        if lanzamiento == lanzamientos-1:
            addList(listplayer1,listplayer2)
        lanzamiento += 1
    other = input("""
Desea Continuar con el Juego
1) SI
2) NO

""").lower()
    time.sleep(2.5)
    
        
        

print("Adivina el numero : Solo hay 4 oportunidades")

top_secret = 7
lanzamiento = 0
max_lanzamiento = 4

while lanzamiento < max_lanzamiento:
    lanzamientos = int (input("Numero de oportunidades:  "))
    lanzamiento += 1
    if lanzamientos == top_secret:
        print("Has encontrado el numero: {}".format(top_secret))
        break
    else:
        print("Intente de Nuevo ")
else:
    print("Game Over")

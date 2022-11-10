# Convertir RGB a Hexadecimal
# Un color RGB tiene este formato
# RGB (red_color, green_color, blue_color)
# RGB (     245     ,       78         ,        100     )
# los valores RGB se obtienen de  0 a 255

#Un colo Hexadecimal se forman apartir de los valores decimales que generan los RGB, sistema HEXADECIMAL
#(  0   ,   1   ,   2   ,   3   ,   4   ,   5   ,   6   ,   7   ,   8   ,   9   ,   A   ,   B   ,   C   ,   D   ,   E   ,   F   )

# Version Automatica por funciones de Hexadecimal
print("Introduce el color RGB a Convertir a Hexadecimal ")
print("Los valores comprendidos en los colores es de 0 a 255")
print('1ro Rojo | 2do Verde | 3er Azul')

red = int(input("Introduce el Color Rojo : "))
green =int(input("Introduce el Color Verde : "))
blue = int(input("Introduce el Color Azul "))

hex_color = 'H{:02x}{:02x}{:02x}'.format(red,green,blue)

print('''
El color en RGB : ( {} , {} , {} )
Es en Hexadecimal : {}
'''.format(red,green,blue,hex_color))

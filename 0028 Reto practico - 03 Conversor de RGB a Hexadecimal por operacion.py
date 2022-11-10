# Convertir RGB a Hexadecimal
# Un color RGB tiene este formato
# RGB (red_color, green_color, blue_color)
# RGB (     245     ,       78         ,        100     ) Ejemplo

#1ro  |||   245 / 16      =   15.3125
#            Entero             Operar Resto             Resto              Los valores en cada par se lee de abajo a arriva
#2do |||     15                     .3125*16                     5                     |||    Se busca la equivalencia en Hexadecimal
#3ro  |||    15/16 = 0.9375                                                              ||      Primer Par de Hexadecimal
#4to  |||       0                       .9375*16                   15                    |       F5

#1ro     |||    78 / 16 = 4.875
#               Entero              operar Resto            Resto               
#do      |||    4                       .875*16                     14                  ||| Se busca equivalencia en Hexadecimal
#3ro     |||    4 / 16 = 0.25                                                            ||  Segundo Par de Hexadeximal
#4to     |||    0                       .25*16                      4                    |   4E

#1ro     |||    100 / 16 = 6.25
#               Entero              operar Resto            Resto               
#do      |||    6                       .25*16                          4                  ||| Se busca equivalencia en Hexadecimal
#3ro     |||    6 / 16 = .375                                                              ||  Tercer  Par de Hexadeximal
#4to     |||    0                       .375*16                        6                  |   64

# Numero Hexadecimal #55ee44


# los valores RGB se obtienen de  0 a 255
#Un colo Hexadecimal se forman apartir de los valores decimales que generan los RGB, sistema HEXADECIMAL
#Hexadecimal (  0   ,   1   ,   2   ,   3   ,   4   ,   5   ,   6   ,   7   ,   8   ,   9   ,   A   ,   B   ,   C   ,   D   ,   E   ,   F   )
# Decimal        (  0   ,   1   ,   2   ,   3   ,   4   ,   5   ,   6   ,   7   ,   8   ,   9   ,   10  ,  11  ,   12  ,  13  ,  14  ,  15  )

# conversion de segundos, minutos, horas, segun sea la peticion del usuario
# 1 - los datos a convertir dependen del usuario
def segMin (segundos):
    minutos = segundos/60
    print('{} segundos = {} minutos '.format(segundos,minutos))
def minHor (minutos):
    horas = minutos/60
    print('{} minutos = {} horas '.format(minutos, horas))
def segHor(segundos):
    horas = (segundos/60)/60
    print('{} segundos = {} horas '.format(segundos,horas))
    
def minSeg (minutos):
    segundos = minutos*60
    print('{} minutos = {} segundos '.format(minutos, segundos))
def horMin(horas):
    minutos = horas*60
    print('{} horas = {} minutos '.format(horas,minutos))
def horSeg(horas):
    segundos = (horas*60)*60
    print('{} horas = {} segundos '.format(horas,segundos))

accion = '1'

while accion == 'si' or accion == '1':
    
    print('''
¿Qué operación desea realizar?
1) Convertir a Horas
2) Convertir a Minutos
3) Convertir a Segundos
''')
    try:
        menu_uno = int(input('Coloque su elección : '))
    except:
        print('Eleccion Equivocada Intentar de Nuevo : ')
        continue
    else:
        if menu_uno == 1:
            print ('''
¿Qué acción realizara?
1) Segundos a Horas
2) Minutos a Horas
''')
            menu_dos = int(input('Introduce la elección '))
            if menu_dos == 1:
                segundos = int(input('Introduce los segundos a convertir '))
                segHor(segundos)
            elif menu_dos == 2:
                minutos = int(input('Introduce los minutos a convertir '))
                minHor(minutos)
        elif menu_uno == 2:
            print ('''
¿Qué acción realizara?
1) Segundos a Minutos
2) Horas a Minutos
''')
            menu_tres = int(input('Introduce la elección '))
            if menu_tres == 1:
                segundos = int(input('Introduce los segundos a convertir '))
                segMin(segundos)

            if menu_tres == 2:
                horas = int(input('Introduce las horas a convertir '))
                horMin(horas)
            
        elif menu_uno == 3:
             print ('''
¿Qué acción realizara?
1) Minutos a Segundos
2) Horas a Segundos
''')
             menu_cuatro = int(input('Introduce la elección '))
             if menu_cuatro == 1:
                 minutos = int(input('Introduce los minutos a convertir '))
                 minSeg(minutos)
             if menu_cuatro == 2:
                 horas = int(input('Introduce las horas a convertir '))
                 horSeg(horas)
        else:
            print('Elección equivocada')
    print('Alguna otra elección 1 Si |||| 2 No')
    accion = input('Introdusca su elección ').lower()


            

# conversion de segundos, minutos, horas, segun sea la peticion del usuario
# 1 - los datos a convertir dependen del usuario
# agregar igual sus sobrantes
def segMin (num):
    segundos = num % 60
    minutos = (num - segundos)/60
    print('{} segundos = {} minutos y {} segundos '.format(num,minutos,segundos))
def minHor (num):
    minutos = num % 60
    horas = (num - minutos)/60
    print('{} minutos = {} horas y {} minutos'.format(num,horas,minutos))
def segHor(num):
    segundos = num % 60
    minutos = (num - segundos)/60
    minutos2 = minutos % 60
    horas = (minutos - minutos2)/60
    print('{} segundos = {} horas con {} minutos y {} segundos '.format(num, horas, minutos2, segundos))
    
def minSeg (num):
    segundos = num*60    
    print('{} minutos = {} segundos '.format(num, segundos))
def horMin(num):
    minutos = num*60
    print('{} horas = {} minutos '.format(num, minutos))
def horSeg(num):
    segundos = (num*60)*60
    print('{} horas = {} segundos '.format(num, segundos))

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
                num = int(input('Introduce los segundos a convertir '))
                segHor(num)
            elif menu_dos == 2:
                num = int(input('Introduce los minutos a convertir '))
                minHor(num)
        elif menu_uno == 2:
            print ('''
¿Qué acción realizara?
1) Segundos a Minutos
2) Horas a Minutos
''')
            menu_tres = int(input('Introduce la elección '))
            if menu_tres == 1:
                num = int(input('Introduce los segundos a convertir '))
                segMin(num)

            if menu_tres == 2:
                num = int(input('Introduce las horas a convertir '))
                horMin(num)
            
        elif menu_uno == 3:
             print ('''
¿Qué acción realizara?
1) Minutos a Segundos
2) Horas a Segundos
''')
             menu_cuatro = int(input('Introduce la elección '))
             if menu_cuatro == 1:
                 num = int(input('Introduce los minutos a convertir '))
                 minSeg(num)
             if menu_cuatro == 2:
                 num = int(input('Introduce las horas a convertir '))
                 horSeg(num)
        else:
            print('Elección equivocada')
    print('Alguna otra elección 1 Si |||| 2 No')
    accion = input('Introdusca su elección ').lower()


            

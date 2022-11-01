# Mostrar menú con las opciones de conversión disponibles
# Capturar la elección del usuario
# Solicitar la cantidad a convertir
# Mostrarle al usuario el resultado de la conversión
# Permtir que el usuario decida continuar o terminar la aplicación
# 1 milla = 1.60934 KM

def millasKilometros(dato):
    kilometros = dato/1.60934
    print('{} Millas es igual a {} kilometros'.format(dato,kilometros))
def kilometrosMillas(dato):
    millas = dato * 1.60934
    print('{} Kilometros es igual a {} Millas'.format(dato, millas ))

eleccion = '1'

while eleccion == '1' or eleccion == 'si':
    print('''
Conversión de Longitudes imperial - Metrica
1) Millas a Kilometros
2) Kilometros a Millas
''')
    try:
        menu_uno = int(input('Tipo de conversión deseada : '))
        if menu_uno == 1:
            dato = float(input('Introduce las Millas a convertir : '))
        elif menu_uno == 2:
            dato = float(input('Introduce los Kilometros a convertir : '))
        
    except ValueError:
        print('Elección Erronea ')
        continue
    else:
        if menu_uno == 1:
            millasKilometros(dato)
        elif menu_uno == 2:
            kilometrosMillas(dato)
    eleccion = input('Desea continuar con la conversión || 1| SI  ||  2| NO  || : ')

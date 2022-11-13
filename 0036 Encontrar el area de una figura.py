# metodo uno
print('Buscar el Area de Un Triangulo, para ello se requiere los siguientes datos: ')
base=float(input('Introduce la Base del Triangulo: '))
altura = float(input('Introduce la Altura del Triangulo: '))

area_tri = (base*altura) /2
print('El area del triangulo es: ',area_tri)
# Metodo 2 usando while

eleccion = '1'
while eleccion == '1' or eleccion == 'si':
    print('Buscar el Area de Un Triangulo, para ello se requiere los siguientes datos: ')
    base2=float(input('Introduce la Base del Triangulo: '))
    altura2 = float(input('Introduce la Altura del Triangulo: '))

    area_tri2 = (base2*altura2) /2
    print('El area del triangulo es: ',area_tri2)

    eleccion = input('Desea Continuar || 1) SI | 2) NO || Elija: ').lower()

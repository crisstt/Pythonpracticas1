eleccion = '1'

while eleccion == '1':
    try:
        print('''Elige la figura a Crear:
1) Triangulo
2) Cuadrado
3) Rectangulo ''')
        figura =input('Elige la Figura a Crear con Patrones de * : ').lower()
        
    except ValueError:
        print('Datos incorrectos ingresar de Nuevo')
        continue
    else:
        linea = int((input('Cuantas Lineas Tendra la figura: ')))
        if figura == '1' or figura == 'triangulo':
            triangulo = input('''1)Triangulo Rectángulo
2) Triangulo Acuatángulo :

Que Figura Deseas: ''')
            if triangulo == '1':
                for i in range (linea):
                    for j in range (i):
                        print('* ', end = ' ')
                    print('.')
            if triangulo == '2':
                for a in range (linea):
                    for s in range (a):
                        print('* ', end = ' ')
                    print('+')
                for a in range (linea, 0 , -1):
                    for x in range(a):
                        print('* ', end = ' ')
                    print('-')
        if figura == '2' or figura == 'cuadrado':
            for r in range (linea):
                print('*     ' * linea)
                
        if figura == '3' or figura == 'rectangulo':
            columna = int(input('Introduce la cantidad de columnas del Rectángulo: '))
            for t in range (linea):
                print('*     '*columna)
                

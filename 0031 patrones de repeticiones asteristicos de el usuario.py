num = int(input('Introduce la cantidad de Filas: '))

for i in range(num+1):
    for x in range(i):
        print('* ', end = ' ')
    print('.')

for j in range (num + 1):
    print(j * '*  ', end = '''.
''')


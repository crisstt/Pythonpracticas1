num = int(input('Introduce la cantidad de Filas: '))

for i in range(num):
    for x in range(i):
        print('* ', end = ' ')
    print('+')
for i in range (num, 0 , -1):
    for x in range(i):
        print('* ', end = ' ')
    print('-')



    

for j in range (num):
    print(j * '*  ', end = '''+
''')
for j in range (num, 0, -1):
    print(j * '*  ', end = '''-
''')


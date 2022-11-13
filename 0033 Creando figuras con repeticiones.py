num = int(input('Ingresa canidad de lineas a crear de la figura: '))
for i in range (num):
    print('  ' * (num - i - 1) + '*' * (2 * i + 1))
for j in range(num, 0, -1):
    print('  ' * (num - j ) + '*' * (2 * j -1))

num = int(input('Introduce la cantidad de linas para crear el arbol: '))
for i in range (num):
    print('  ' * (num -i -1) + '*' * (2 * i + 1))

for n in range (int(num/2)):
    print('  ' * int((num - num/2.9)+1)+ '*'*int(num/2) )

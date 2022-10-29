# temperatura media
# valores por encima de temperatura media
suma = 0
t_s_media = []
cantidad_t = int(input("Ingrese cantidad de temperatura a promediar : "))
temperaturas = [int(input("Introduce la Temperatura : ")) for i  in range (cantidad_t)]
print(temperaturas)

for i in range(len(temperaturas)):
    suma += temperaturas[i]

print("La suma de las Temperas antes de Promediar es : ",suma, "\nCantidad de Temperaturas Tomadas : ", len(temperaturas))
promediar = suma / len(temperaturas)
print("Temperatura promedio de las muestras es : ",promediar)

for i in range(len(temperaturas)):
    if promediar < temperaturas[i]:
        t_s_media.append(temperaturas[i])

for i in range(len(t_s_media)):
    if i == 0:
        print('''
Las Temperaturas Superiores a {} grados son :
'''.format(promediar))
        print("La temperatura {} grados".format(t_s_media[i]))
    else:
        print("La temperatura {} grados".format(t_s_media[i]))
        
        

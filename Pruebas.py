alumnos_calificacion = [[['Jose', 'Perez', 'Sanchez'], [10.0, 8.0, 7.5, 9.0]],
                                        [['Maria', 'Herrera', 'Gutierrez'], [8.5, 9.0, 7.5, 6.3]]]
suma = 0
for i in range(len(alumnos_calificacion)):
    suma = 0
    for k in range(len(alumnos_calificacion[i][1])):
        suma = suma + alumnos_calificacion[i][1][k]
    print(alumnos_calificacion[i][1])
    print(suma)
    promedio = suma/len(alumnos_calificacion[i][1])
    print('''
Nombre Completo : {} {} {}
Calificacion por Parcial : {} | {} | {} | {}
Promedio Final : {}
'''. format (alumnos_calificacion[i][0][0],alumnos_calificacion[i][0][1],alumnos_calificacion[i][0][2], alumnos_calificacion[i][1][0], alumnos_calificacion[i][1][1],
            alumnos_calificacion[i][1][2],alumnos_calificacion[i][1][3], promedio))




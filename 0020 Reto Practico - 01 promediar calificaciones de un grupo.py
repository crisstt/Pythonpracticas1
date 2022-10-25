# Crear un codigo que permita validar calificaciones y alumnos, promediar y mostrar calificacion media y agrupar en una lista
# Si el Alumno aprobar o reprobo la materia
# if, for, while, try, def  , .lower()
# Nombre | Calificion #1 | Calificacion #2 | Calificacion #3 | Calificacion #4 | Promedio | Status
# promedio del salon |  media o calificacion mas repetida  | calificacion mas baja | calificacion mas alta
# menu sencillo que nos permita continuar pidiendo nombres y calificiones|
alumnos_clase = []
calificacion_clase = []
calificacionAlumnos = []
x = 0

def alumnos (nombre, a_paterno, a_materno):
    alumno = [nombre, a_paterno , a_materno]
    alumnos_clase.append(alumno)
    print('Lista de alumnos : ',alumnos_clase)
    parcial_uno = float(input('Introduce calificacion parcial 1 : '))
    parcial_dos = float(input('Introduce calificacion parcial 2 : '))
    parcial_tres = float(input('Introduce calificacion parcial 3 : '))
    parcial_cuatro = float(input('Introduce calificacion parcial 4 : '))
    calificaciones(parcial_uno, parcial_dos, parcial_tres, parcial_cuatro)

def calificaciones (parcial_uno, parcial_dos, parcial_tres, parcial_cuatro):
    calificacion = [parcial_uno, parcial_dos, parcial_tres, parcial_cuatro]
    calificacion_clase.append(calificacion)
    calificacionAlumnos.append([alumnos_clase[x],calificacion_clase[x]])
    i = 0
    k = 0
    for i in range(len(calificacionAlumnos)):
        suma = 0
        for k in range(len(calificacionAlumnos[i][1])):
            suma = suma + calificacionAlumnos[i][1][k]
        promedio = suma/len(calificacionAlumnos[i][1])
        if promedio > 6 :
            print('Aprovado')
            status = 'Aprobado'
        else:
            print('Reprobado')
            status = 'Reprobado'
        imprimirAlumnos(i,promedio,status)
        
    

def modificar ():
    print('modificar')
    

def imprimirAlumnos (i, promedio, status):
    print('''
ID {}11  
Nombre Completo  {} {} {}
Calificaciones Parcial 1er {} |2do {} |3er {} |4to {}
Promedio :  {}
Status :  {} 
'''. format(i,calificacionAlumnos[i][0][0],calificacionAlumnos[i][0][1],calificacionAlumnos[i][0][2],
            calificacionAlumnos[i][1][0],calificacionAlumnos[i][1][1],calificacionAlumnos[i][1][2],calificacionAlumnos[i][1][3],promedio, status))
        
        
      



print('''
Bienvenido
Introducir accion a realizar
1) Agregar Alumno
2) Agregar Calificacion
3) Cambiar Informacion
    a) Nombre de Alumnos
    b) Calificaciones
''')
continuar = '1'


while(continuar == '1' or continuar == 'si'):
    try:
        accion = int(input('Introduce la accion a realizar : \n'))
    except ValueError:
        print("Selecion No Valida")
        continue
    else:
        if accion == 1:
            nombre = input('Introduce nombre del alumno : ')
            a_paterno = input('Introduce apellido paterno del alumno : ')
            a_materno = input('Introduce apellido materno del alumno : ')
            alumnos(nombre, a_paterno , a_materno)
        elif accion == 2:
            calificaciones(parcial_uno, parcial_dos, parcial_tres, parcial_cuatro)
        elif accion == 3:
            modificar ()
        else:
            print('Elección Equivocada')
    x += 1
    print('''
Agregar algun dato mas :
1) SI
2) NO
''')
    continuar = input('Ingresa tu  respuesta   |1|SI|   |2|NO : ').lower()

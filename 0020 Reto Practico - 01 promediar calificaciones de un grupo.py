# Crear un codigo que permita validar calificaciones y alumnos, promediar y mostrar calificacion media y agrupar en una lista
# Si el Alumno aprobar o reprobo la materia
# if, for, while, try, def  , .lower()
# Nombre | Calificion #1 | Calificacion #2 | Calificacion #3 | Calificacion #4 | Promedio | Status
# promedio del salon |  media o calificacion mas repetida  | calificacion mas baja | calificacion mas alta
# menu sencillo que nos permita continuar pidiendo nombres y calificiones|
alumnos_clase = []
calificacion_clase = []
calificacionAlumnos = []
lista_alumnos = []
x = 0
# Funcion que pide alumonos y las calificaciones
def alumnos (nombre, a_paterno, a_materno):
    alumno = [nombre, a_paterno , a_materno]
    alumnos_clase.append(alumno)
    print('Lista de alumnos : ',alumnos_clase)
    parcial_uno = float(input('Introduce calificacion parcial 1 : '))
    parcial_dos = float(input('Introduce calificacion parcial 2 : '))
    parcial_tres = float(input('Introduce calificacion parcial 3 : '))
    parcial_cuatro = float(input('Introduce calificacion parcial 4 : '))
    calificaciones(parcial_uno, parcial_dos, parcial_tres, parcial_cuatro)
# Funcion que toma las calificaciones y las acomoda junto a los nombres de alumnos antes tomados
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
            print('Aprobado')
            status = 'Aprobado'
        else:
            print('Reprobado')
            status = 'Reprobado'
    imprimirAlumnos(i,promedio,status)
    guardarAlumnos(i,promedio,status)    
# Funcio que permite ver los datos ingresados si hay algun problema desde ahi detectarlo
def imprimirAlumnos (i, promedio, status):
    print('''
ID {}11  
Nombre Completo  {} {} {}
Calificaciones Parcial 1er {} |2do {} |3er {} |4to {}
Promedio :  {}
Status :  {} 
'''. format(i,calificacionAlumnos[i][0][0],calificacionAlumnos[i][0][1],calificacionAlumnos[i][0][2],
            calificacionAlumnos[i][1][0],calificacionAlumnos[i][1][1],calificacionAlumnos[i][1][2],calificacionAlumnos[i][1][3],promedio, status))
# Funcion que Guarda la Informacion en un orden establecido
def guardarAlumnos (i,promedio,status):
    datos_alumno =[i,calificacionAlumnos[i][0][0],calificacionAlumnos[i][0][1],calificacionAlumnos[i][0][2],
            calificacionAlumnos[i][1][0],calificacionAlumnos[i][1][1],calificacionAlumnos[i][1][2],calificacionAlumnos[i][1][3],promedio, status]
    lista_alumnos.append(datos_alumno)
# Funcion que muestra en lista los alumnos, calificacion y promedios
def mostrarListaAlumnos (lista_alumnos):
    for i in range(len(lista_alumnos)):
        print('''
{}           {} {} {}                {}  {}  {}  {}            {}           {}
'''. format (lista_alumnos[i][0],lista_alumnos[i][1],lista_alumnos[i][2],lista_alumnos[i][3],lista_alumnos[i][4],lista_alumnos[i][5],lista_alumnos[i][6],lista_alumnos[i][7],lista_alumnos[i][8],lista_alumnos[i][9]))

# Funciones Utilizadas para Modificar el Nombre de los Alumnos
def modificarNombre(ID):
    lista_alumnos[ID][1] = input('Introduce el Nuevo Nombre : ') 
def modificarApellidoP(ID):
    lista_alumnos[ID][2] = input('Intruduce el Nuevo Apellido Paterno : ')
def modificarApellidoM(ID):
    lista_alumnos[ID][3] = input('Intruduce el Nuevo Apellido Materno : ')
def modificarLastName(ID):
    lista_alumnos[ID][1] = input("Introduce Nuevo Nombre : ")
    lista_alumnos[ID][2] = input("Introduce Nuevo Apellido Paterno : ")
    lista_alumnos[ID][3] = input("Introduce Nuevo Apellido Materni : ")
# Funciones para Modificar las Calificaciones de los Alumnos
def parcialUno(ID):
    lista_alumnos[ID][4] = float(input("Ingresa Nueva Calificacion del 1er Parcial : "))
    lista_alumnos[ID][8] = (lista_alumnos[ID][4] + lista_alumnos[ID][5] + lista_alumnos[ID][6] + lista_alumnos[ID][7])/4
def parcialDos(ID):
    lista_alumnos[ID][5] = float(input("Ingresa Nueva Calificacion del 2do Parcial : "))
    lista_alumnos[ID][8] = (lista_alumnos[ID][4] + lista_alumnos[ID][5] + lista_alumnos[ID][6] + lista_alumnos[ID][7])/4
def parcialTres(ID):
    lista_alumnos[ID][6] = float(input("Ingresa Nueva Calificacion del 3er Parcial : "))
    lista_alumnos[ID][8] = (lista_alumnos[ID][4] + lista_alumnos[ID][5] + lista_alumnos[ID][6] + lista_alumnos[ID][7])/4
def parcialCuatro (ID):
    lista_alumnos[ID][7] = float(input("Ingresa Nueva Calificacion del 4to Parcial : "))
    lista_alumnos[ID][8] = (lista_alumnos[ID][4] + lista_alumnos[ID][5] + lista_alumnos[ID][6] + lista_alumnos[ID][7])/4

def nAlumnosPromedioGeneral(lista_alumnos):
    for i in range(len(lista_alumnos)):
        sum_genral = sum_general + lista_alumnos[i][8]
    prom_general = sum_genral/len(lista_alumnos)
    print('''
Cantidad de Alumnos en el Salon : {}
Promedio General del Salon : {}
''').format(len(lista_alumnos),prom_general)
        
def calificacionMinMaxModa(lista_alumnos):
    calif_max = 0
    for m in range(len(lista_alumnos)):
        if calif_max > lista_alumnos[m][8]:
            calif_max = calif_max
        elif calif_max < lista_alumnos[m][8]:
            calif_max = lista_alumnos[m][8]
        else:
            print("Son Iguales :")
            calif_max = calif_max
    calif_min = 10
    for c in range(len(lista_alumnos)):
        if calif_min > lista_alumnos[c][8]:
            calif_min = lista_alumnos[c][8]
        elif calif_min < lista_alumnos[c][8]:
            calif_min = calif_min
        else:
            print('Son Iguales :')
            calif_min = calif_min
    
    

continuar = '1'


while(continuar == '1' or continuar == 'si'):
    try:
        print('''
Bienvenido
Introducir accion a realizar
1) Agregar Alumno
2) Informacion de la Clase
    a) Cantidad de Alumnos y Promedio General 
    b) Calificacion Max , Calificion Min y Moda
3) Cambiar Informacion
    a) Nombre de Alumno
    b) Calificaciones
4) Mostrar Lista de Alumnos
''')
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
            print('''
¿Que información desea de la clase?
a) Numero de Alumnos y Promedio de la Clase
b) Calificaciones Min, Max y Moda
''')
            try:
                tipo_informacion = input("Informacion a Vizualizar de la Clase: ").lower()
            except ValueError:
                print('Dato no valido')
                continue
            else:
                if tipo_informacion == 'a':
                    nAlumnosPromedioGeneral(lista_alumnos)
                elif tipo_informacion == 'b':
                    calificacionMinMaxModa(lista_alumnos)
                else:
                    print('Error Intente de nuevo')
            
        elif accion == 3:
            mostrarListaAlumnos(lista_alumnos)
            print('''
¿Que desea Editar?
a) Nombre de Alumno
b) Calificaciones
''')
            ID = int(input('Introduce el ID del Alumno : '))
            option = input("Introdusca su eleccion : ").lower()
            if option == 'a':
                print('''
¿Que desea Modificar?
1) Nombre
2) Apellido Paterno
3) Apellido Materno
4) Todos los anteriores''')
                try:
                    edit_nombre = input("Que Modificacion desea realizar 1 | 2 | 3 | 4 : ")
                except ValueError:
                    print("Eleccion no valida ")
                    continue
                else:
                    if edit_nombre == '1':
                        modificarNombre(ID)
                    elif edit_nombre == '2':
                        modificarApellidoP(ID)
                    elif edit_nombre =='3':
                        modificarApellidoM(ID)
                    elif edit_nombre == '4':
                        modificarLastName(ID)
                    else:
                        print('Dato no Valido ')
            elif option == 'b':
                print('''
¿Que Calificacion desea Editar?
1) 1er Parcial
2) 2do Parcial
3) 3er Parcial
4) 4to Parcial
''')
                try:
                    edit_parcial = input("Que Modificacion desea realizar 1 | 2 | 3 | 4 : ")
                except ValueError:
                    print("Eleccion no valida ")
                    continue
                else:
                    if edit_parcial == '1':
                        parcialUno(ID)
                    elif edit_parcial == '2':
                        parcialDos(ID)
                    elif edit_parcial =='3':
                        parcialTres(ID)
                    elif edit_parcial == '4':
                        parcialCuatro(ID)
                    else:
                        print('Dato no Valido ')
                    
                        
        elif accion == 4:
            print ('ID         |           Nombre Completo        |      Calificacion Parcial      |  Promedio  |     Status   |     ')
            print('                                                               |   1er   |  2do  |   3er  |   4to | ')
            mostrarListaAlumnos(lista_alumnos)
        else:
            print('Elección Equivocada')
    x += 1
    print('''
Agregar algun dato mas :
1) SI
2) NO
''')
    continuar = input('Ingresa tu  respuesta   |1|SI|   |2|NO : ').lower()

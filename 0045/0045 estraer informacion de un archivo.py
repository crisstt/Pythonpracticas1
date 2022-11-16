# capturar usuario + contraseña de un archivo de texto
# Leer datos originales
# Generar .txt para los nombres de usuarios capturados
# Generar .txt con los pasword capturados
'''
0             1                  2                 3                  4                          5
ID : STATUS : COUNTRY : USER : PASSWORD : TIMESTAMP
'''
dic_datos = {}
#Abrir archivo original en modo lectura
#name archivo = abrir('nombre del archivo con extencion', 'r'  ||lectura||)
file = open('usuarios_paswords.txt', 'r')
#variable = Crear archivo ('nombre del archivo con extencion', 'w' ||escribir||)
username = open('user.txt', 'w')
passwords = open ('password.txt', 'w')
dicc_datos = open('diccionario_datos.txt', 'w')
dicc_datos_acomodados = open ('diccionario_agrupado.txt','w')

for line in file:
    parts = line.split(':')
    dic_datos [parts[0]] = parts[1], parts[2], parts[3], parts[4], parts[5]
    name = parts[3]
    password = parts[4]
#   usar donde se guardan los archivos y escribir lo que se necesita ()
    username.write(name)
    username.write('\n')
    passwords.write(password)
    passwords.write('\n')

#Guarda los valores con un separador : listo para usar y crear un diccionario
for u in dic_datos:
    dicc_datos.write('{0}:{1},{2},{3},{4},{5}'. format(u,str(dic_datos[u][0]),str(dic_datos[u][1]),str(dic_datos[u][2]),str(dic_datos[u][3]),str(dic_datos[u][4])))
    dicc_datos.write('\n')


# Creamos un txt Con los Datos Ordenados, Para su Guardado
for o in dic_datos:
    i_d = o
    status = dic_datos[o][0]
    country = dic_datos[o][1]
    user = dic_datos[o][2]
    pass_single = dic_datos[o][3]
    timestamp = dic_datos[o][4]
    dicc_datos_acomodados.write('''
ID : {}
STATUS : {}
COUNTRY : {}
USER : {}
PASSWORD : {}
TIMESTAMP : {}
'''. format(i_d,status,country,user,pass_single,timestamp))
    dicc_datos.write('\n')

# Mostrar datos Agrupados en ejecucion
for x in dic_datos:
    print('''
ID :\t {}
STATUS : {}
COUNTRY : {}
USER :\t {}
PASSWORD: {}
TIMESTAMP {}
'''. format(x,dic_datos[x][0],dic_datos[x][1],dic_datos[x][2],dic_datos[x][3],dic_datos[x][4]))

#cerrar los documentos usados
file.close()
username.close()
passwords.close()
dicc_datos.close()
dicc_datos_acomodados.close()
    
    

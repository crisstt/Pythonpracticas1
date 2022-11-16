# como capturar el user name y el nombre de usuario de un dominio de mail
# 3 formas de capturarlos

'''
FORMA 1
Usando for y diccionarios de forma sensilla
'''
n_email = int(input('Cantidad de correos a pedir para la captura de datos: '))
                                                                            #strip no toma en cuenta los espacios en blanco
user_input = [str(input('Introducir los correos electronicos a validar: ')).strip() for i in range(n_email)]
print(user_input)
dic_namedomain = {}

for i in range (len(user_input)):
    # capturamos los nombres de los correos
    print('El Correo a validar es ||  {}  || '.format(user_input[i]))
    user_name = user_input[i]
    user_name = user_name[ :user_name.index('@')]
    # capturamos los dominios de los correos
    domain_name = user_input[i]
    domain_name = domain_name[domain_name.index('@') + 1: ]
    dic_namedomain [user_name] = domain_name

for x, y in dic_namedomain.items():
    print('Nombre de Usuario del Correo es : ',x,'\nEl dominio del Correo es: ',  y, '\n\n')
print(dic_namedomain)


    
    


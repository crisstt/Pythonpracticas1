'''
Usando partition
Forma 2 de realizarlo

'''
n_email = int(input('Cantidad de correos a pedir para la captura de datos: '))
                                                                            #strip no toma en cuenta los espacios en blanco
user_input = [str(input('Introducir los correos electronicos a validar: ')).strip() for i in range(n_email)]
dic_email_domain = {}

for i in range(len(user_input)):
    email = user_input[i]
    parts = email.partition('@')
    dic_email_domain[parts[0]] = parts[2]
    print('Validar el correo ingresado : ',email)

for x in dic_email_domain:
    print('User : ',x,'----',' Domain:  ',dic_email_domain[x])

    
    

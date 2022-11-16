'''
Usando split()
Forma 3 de realizarlo

'''
n_email = int(input('Cantidad de correos a pedir para la captura de datos: '))
                                                                            #strip no toma en cuenta los espacios en blanco
user_input = [str(input('Introducir los correos electronicos a validar: ')).strip() for i in range(n_email)]
dic_email_domain = {}
for i in range(len(user_input)):
    email_split = user_input[i].split('@')
    dic_email_domain [email_split[0]] = email_split[1]
    print('Email #{} es : {}'.format(i+1,user_input[i]))
n=0
for x in  dic_email_domain:
    print('#',n+1,'User : ',x,'---', ' Domain : ',dic_email_domain[x])
    n+=1

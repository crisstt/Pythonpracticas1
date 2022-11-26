import pandas as pd

'''contenedor = panda.leerexcel('nombre del archivo excel con extencion')'''
data = pd.read_excel('d_user_email.xlsx')

# print(data)

get_email = data.get('EMAIL')
list_emails = list (get_email)

print(list_emails)

# mientras abrir ('archivo_crear', 'seescribe') 
with open ('get_emails.txt', 'w') as f1:
    for item in list_emails:
        f1.write(item + '\n')

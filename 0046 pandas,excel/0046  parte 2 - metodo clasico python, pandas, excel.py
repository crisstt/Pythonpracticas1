import pandas as pd

'''contenedor = panda.leerexcel('nombre del archivo excel con extencion')'''
data = pd.read_excel('d_user_email.xlsx')

# print(data)

get_email = data.get('EMAIL')
list_emails = list (get_email)

print(list_emails)

f = open ('my_emails.txt','w')
for item in list_emails:
    f.write(item +'\n')

f.close()

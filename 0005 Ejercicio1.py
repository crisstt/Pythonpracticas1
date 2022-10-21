print("""
Usando la Siguiente Información, extrae los datos requeridos
User_data = 'root:32-AD-65-92-C4-D2:08242019:SaoPaulo'
""")
user_data = 'root:32-AD-65-92-C4-D2:08242019:SaoPaulo'

print("Extrae el Direccion MAC")
print(user_data[5:22])
print(user_data[-35:-18])
print(user_data[5:-18])

print("\n Extrae la Fecha")
print(user_data[23:31])
print(user_data[-17:-9])
print(user_data[23:-9])

print("\n Extrae el Nombre de Usuario")
print(user_data[23:31])
print(user_data[-17:-9])
print(user_data[23:-9])

print("\n Extrae La Ciudad")
print(user_data[32:40])
print(user_data[-8:])
print(user_data[32:])



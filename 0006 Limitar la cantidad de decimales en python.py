print("limitar las decimales a dos de los siguientes valores")

print("48.94245 : 25.2354 : 16.8864 : 2.1514544")
num1= 48.94245
num2= 25.2354
num3= 16.8864
num4= 2.1514544

print("\n Metodo A la vieja escuela")
print("Clasic Way : %.2f \n" %num1)

"""Usando Format"""
print("\n Metodo format")

print(float("{0:.2f}".format(num2)))
print(float("{:.2f}".format(num2)))

""" Metodo Round"""
print("\n Metodo Round")

print(round(num3, 2))

"""Usando directamente el metodo Format """
print("\nFormat Directo")
print(format(num4,".2f"))

""" Modern way"""
print("\n Metodo Moderno")
print(f"Modern way : {num1:2f}")
print(f"Modern way : {num2:2f}")
print(f"Modern way : {num3:2f}")
print(f"Modern way : {num4:2f}")






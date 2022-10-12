print(50 * "+")
print(17* " " + "Helo App")
print(50* "+")

user_input = input ("¡Hola! ¿Comó te llamas?  \n")
say_hello = "Hola! un Gusto Saludarte " + user_input
say_hello2 = "¡Hola! un Gusto Saludarte %s "  %user_input
say_hello3 = "¡Hola! un Gusto Saludarte {} ". format  (user_input)
say_hello4 = f"¡Hola! un Gusto Saludarte {user_input}"
print(say_hello)
print (say_hello2)
print (say_hello3)
print (say_hello4)

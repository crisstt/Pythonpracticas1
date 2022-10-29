# 4 formas de crear lista de numero secuenciales

# lista for
n_secuenciales = [i for i in range(1,51)]
print(n_secuenciales)

# generator expression similar a lista for
# se convierte a lista
n_sec = list(i for i in range(1,51))
print(n_sec)

# Clasico for
numero_sec = []
for n in range(1,51):
    numero_sec.append(n)
print(numero_sec)

# usando while

contador = 1
list_secuencial = []
while contador < 51:
    list_secuencial.append(contador)
    contador += 1
print(list_secuencial)
        



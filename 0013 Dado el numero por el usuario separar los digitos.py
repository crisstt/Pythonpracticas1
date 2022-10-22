""" Separar los digitos y agregar a una lista """
# Metodo uno
lista = []
# crear funcion
def str_int(numero):
    for i in numero:
        lista.append(int(i))
    print(lista)

numero = input("introduce numero a separar digitos ")

str_int(numero)

# Metodo dos List compreheshion forma elegante de hac er listas

def string_int (txt):
    list_num = [int(i) for i in txt]
    print(list_num)

num_input = input("Introduce el numero a separar sus digitos : ")

string_int(num_input)

    


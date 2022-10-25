# Crea una tabla de multipliación con menú de selección
# Funcion y selector de errores , ciclo for y deciciones if else

"""
Crear un menu donde se seleccione latabla de multiplicar y el limite a tomar de la tabla
"""
import sys

select = '1'

def tablaDeMultiplicar (tabla,n_maximo):
    for i in range(1,n_maximo+1):
        tabla_de_multiplicar = tabla*i
        print("{} X {} = {} ".format(tabla, i , tabla_de_multiplicar))
print("""
Introduce eleccion a realizar :
    1) Generar Tabla de Multiplicar
    2) Salir
    """)

while (select == '1' or select == 'si'):
    try:
        select = (input("Ingrese la seleccion ")).lower()
    except ValueError:
        print("La Seleccion no es valida")
        continue
    else:
         if select == '1' or select == 'si':
             print("Introduce que tabla decea realizar :  ")
             tabla = int(input(" "))
             print("Hasta que numero desea realizar la multiplicacion : ")
             n_maximo = int(input(" "))
             tablaDeMultiplicar(tabla,n_maximo)
         else:
            print("Finalizar")
            sys.exit(1)
    print("""
Continuar Creando tablas :
    1) Si
    2) No
    """)
             
        




    
    

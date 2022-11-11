#Tipo de Unidad	Cantidad   	        Tipo de unidad            |         Tipo de Unidad	        Cantidad                    Tipo de unidad    				
#Pulgada(in)            25.4	                            Milimetro	           |	    Milímetro (mm)	        0.0393701	               Pulgada (in)
#Pulgada(in)            2.54	                            Centimetro              |	    Milímetro (mm)	        0.00328084	               Pie (ft)
#Pulgada(in)           0.0254	                            Metro	           |	    Milímetro (mm)	        0.00109361	               Yarda (yd)
#Pulgada(in)           0.0000254	                            Kilometros              |	    Milímetro (mm)	        0.0062137	               Milla (mi)
#Pulgada(in)           0.0833333333333333         Pie	                            |	    Milímetro (mm)	        0.1	                                Centímetro (cm)
#Pulgada(in)           0.0277777777777777         Yarda	           |         Milímetro (mm)	        0.001	               Metro (m)
#Pulgada(in)           0.0000157828282828283   Milla	           |	    Milímetro (mm)	        0.000001	               Kilómetro (km)
#				                                              |         Centímetro (cm)        0.393701	               Pulgada (in)
#Pie (ft)	                12	                            Pulgada (in)              |         Centímetro (cm)	        0.0328084	               Pie (ft)
#Pie (ft)	                0.333333	                            Yarda (yd)	           |         Centímetro (cm)	        0.0109361	               Yarda (yd)
#Pie (ft)	                0.000189394	            Milla (mi)	           |	    Centímetro (cm)         0.062137	               Milla (mi)
#Pie (ft)	                304.8	                            Milímetro (mm)      |	    Centímetro (cm)         10	                                 Milímetro (mm)
#Pie (ft)	                30.48	                            Centímetro (cm)    |	    Centímetro (cm)         0.01	                                 Metro (m)
#Pie (ft)	                0.3048	                            Metro (m)	           |	    Centímetro (cm)         0.00001	                Kilómetro (km)
#Pie (ft)	                0.0003048	                            Kilómetro (km)      |	    Metro (m)	         393701	                Pulgada (in)
#				                                               |       Metro (m)	         328084	                Pie (ft)
#Yarda (yd)	    36	                            Pulgada (in)               |	    Metro (m)	         109361	                Yarda (yd)
#Yarda (yd)	    3	                            Pie (ft)	            |	    Metro (m)	         0.000621371	                Milla (mi)
#Yarda (yd)	    0.000568182                   Milla (mi)	            |	    Metro (m)	         1	                                 Milímetro (mm)
#Yarda (yd)	    914.4	                            Milímetro (mm)      |	    Metro (m)	         100	                                 Centímetro (cm)
#Yarda (yd)	    91.44	                            Centímetro (cm)     |	    Metro (m)	         0.001	                Kilómetro (km)
#Yarda (yd)	    0.9144	                            Metro (m)	            |	    Kilómetro (km)	        39,370.10	                Pulgada (in)
#Yarda (yd)	    0.0009144	            Kilómetro (km)      |	    Kilómetro (km)	        3,280.84	                Pie (ft)
#				                                                |       Kilómetro (km)  	        1,093.61	                Yarda (yd)
#Milla (mi)	    63,360	                            Pulgada (in)                |	    Kilómetro (km)	        0.621371	                Milla (mi)
#Milla (mi)	    5,280	                            Pie (ft)	            |	    Kilómetro (km)	        1000000	                Milímetro (mm)
#Milla (mi)	    1,760	                            Yarda (yd)	           |	    Kilómetro (km)	        100	                                 Centímetro (cm)
#Milla (mi)	    1,610,000	            Milímetro (mm)    |	    Kilómetro (km)	        1	                                 Metro (m)
#Milla (mi)	    160,934	            Centímetro (cm)  |				
#Milla (mi)	    1,609.34	            Metro (m)	             |			
#Milla (mi)	    1.60934	            Kilómetro (km)    |

# mostrar menú con las opciones de conversión disponibles
# capturar la elección del usuario
# Solicitar la cantidad a convertir
#mostrarle al usuario el resultado de la conversión
#permtir que el usuario decida continuar o terminar la aplicación

def menuEleccion(unidadentrada,menu_uno):
    print('''
Convertir a :
1)Pulgadas(in)                  5)Milimetros(mm)
2)Pies(ft)                          6)Centimetros(cm)
3)Yardas(yd)                    7)Metros(m)
4)Millas(mi)                      8)Kilometros(km)
''')
    menu_dos = int(input('Introduce a que Unidad Convertir: '))
    operacionesIn(unidadentrada,menu_dos,menu_uno)
    
def operacionesIn(unidadentrada,menu_dos,menu_uno):
    if menu_uno == 1:
        if menu_dos == 1:
            print('{0} Pulgadas es igual a {0} Pulgadas'.format(unidadentrada))
        elif menu_dos == 2:
            pies = unidadentrada*0.0833333333333333
            print('{} Pulgadas es igual a {} Pies'.format(unidadentrada,pies))
        elif menu_dos == 3:
            yarda = unidadentrada * 0.0277777777777777
            print('{} Pulgadas es igual a {} Yardas'.format(unidadentrada,yarda))
        elif menu_dos == 4:
            milla = unidadentrada * 0.0000157828282828283
            print('{} Pulgadas es igual a {} Millas'.format(unidadentrada,milla))          
   


eleccion = '1'
while eleccion == '1' or eleccion == 'si':
    print('''
Unidades a Convertir:
1)Pulgadas(in)                  5)Milimetros(mm)
2)Pies(ft)                          6)Centimetros(cm)
3)Yardas(yd)                    7)Metros(m)
4)Millas(mi)                      8)Kilometros(km)
''')
     
    try:
        menu_uno = int(input('Introduce que Unidad desea Convertir : '))
        unidadentrada = float(input('Introduce la cantidad de unidades a convertir : '))
    except ValueError:
        print('Los datos ingresados son incorrectos, Intentar de nuevo : ')
        continue
    else:
        if menu_uno == 1:
            menuEleccion(unidadentrada,menu_uno)
            
        elif menu_uno == 2:
            menuEleccion(unidadentrada,menu_uno)
            
        elif menu_uno == 3:
            menuEleccion(unidadentrada,menu_uno)
           
        elif menu_uno == 4:
            menuEleccion(unidadentrada,menu_uno)
           
        elif menu_uno == 5:
            menuEleccion(unidadentrada,menu_uno)
            
        elif menu_uno == 6:
            menuEleccion(unidadentrada,menu_uno)
            
        elif menu_uno == 7:
            menuEleccion(unidadentrada,eleccion)
            
        elif menu_uno == 8:
            menuEleccion(unidadentrada,menu_uno)
            
        else:
            print('Intenetar de Nuevo')
    eleccion = input('Desea Continuar  (||1||) SI    (||2||)  NO: ').lower()
            


                                                                    

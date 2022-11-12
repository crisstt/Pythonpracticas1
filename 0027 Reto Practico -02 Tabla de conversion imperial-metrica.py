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
    menu_dos = int(input('Introduce a que Unidad Convertir:  || 1) | 2) | 3) | 4) | 5) | 6) | 7) | 8) || '))
    if menu_uno == 1:
        operacionesIn(unidadentrada,menu_dos)
    elif menu_uno == 2:
        operacionesFt(unidadentrada,menu_dos)
    elif menu_uno == 3:
        operacionesYd(unidadentrada,menu_dos)
    elif menu_uno == 4:
        operacionesMi(unidadentrada,menu_dos)
    elif menu_uno == 5:
        operacionesMil(unidadentrada,menu_dos)
    elif menu_uno == 6:
        operacionesCm(unidadentrada,menu_dos)
    elif menu_uno == 7:
        operacionesMe(unidadentrada,menu_dos)
    elif menu_uno == 8:
        operacionesKi(unidadentrada,menu_dos)
   
'''
Menu Pulgadas
'''
#---------------------------------------------------------Pulgada-------------------------------------------------------------------------------
def operacionesIn(unidadentrada,menu_dos):
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
    elif menu_dos == 5:
        milimetro = unidadentrada * 25.4
        print('{} Pulgadas es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centrimetro = unidadentrada * 2.54
        print('{} Pulgadas es igual a {} Centimetros'.format(unidadentrada,centrimetro))
    elif menu_dos == 7:
        metro = unidadentrada * .0254
        print('{} Pulgadas es igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.0000254
        print('{} Pulgadas es igual a {} Kilometros'.format(unidadentrada,kilometro))
'''
Menu pies
'''
#---------------------------------------------------------Pies------------------------------------------------------------------------------

def operacionesFt(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 12
        print('{0} Pies es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        print('{} Pies es igual a {} Pies'.format(unidadentrada))
    elif menu_dos == 3:
        yarda = unidadentrada * 0.333333
        print('{} Pies es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        milla = unidadentrada * 0.000189394
        print('{} Pies es igual a {} Millas'.format(unidadentrada,milla))
    elif menu_dos == 5:
        milimetro = unidadentrada * 304.8
        print('{} Pies es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centrimetro = unidadentrada * 30.48
        print('{} Pies es igual a {} Centimetros'.format(unidadentrada,centrimetro))
    elif menu_dos == 7:
        metro = unidadentrada * .3048
        print('{} Pies es igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.0003048	   
        print('{} Pies es igual a {} Kilometros'.format(unidadentrada,kilometro))
'''
Menu Yarda
'''
#---------------------------------------------------------Yarda-------------------------------------------------------------------------------

def operacionesYd(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 36
        print('{0} Yardas es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 3
        print('{} Yardas es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        print('{} Yardas es igual a {} Yardas'.format(unidadentrada))
    elif menu_dos == 4:
        milla = unidadentrada * 0.000568182
        print('{} Yardas es igual a {} Millas'.format(unidadentrada,milla))
    elif menu_dos == 5:
        milimetro = unidadentrada * 914.4
        print('{} Yardas es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centrimetro = unidadentrada * 91.44
        print('{} Yardas es igual a {} Centimetros'.format(unidadentrada,centrimetro))
    elif menu_dos == 7:
        metro = unidadentrada * 0.9144
        print('{} Yardas es igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.0009144
        print('{} Yardas es igual a {} Kilometros'.format(unidadentrada,kilometro))

'''
Menu Milla
'''
#---------------------------------------------------------Milla-------------------------------------------------------------------------------

def operacionesMi(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 63360
        print('{0} Millas es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 5280
        print('{} Millas es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        yarda = unidadentrada * 1760
        print('{} Millas es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        print('{} Millas igual a {} Millas'.format(unidadentrada))
    elif menu_dos == 5:
        milimetro = unidadentrada * 1610000
        print('{} Millas es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centrimetro = unidadentrada * 160934
        print('{} Millas es igual a {} Centimetros'.format(unidadentrada,centrimetro))
    elif menu_dos == 7:
        metro = unidadentrada * 1609.34
        print('{} Millases igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 1.60934
        print('{} Millas es igual a {} Kilometros'.format(unidadentrada,kilometro))
        
'''
Menu Milimetros
'''
#---------------------------------------------------------Milimetros-------------------------------------------------------------------------------
def operacionesMil(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 0.0393701
        print('{0} Milimetros es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 0.00328084
        print('{} Milimetros es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        yarda = unidadentrada * 0.00109361
        print('{} Milimetros es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        milla = unidadentrada * 0.0062137
        print('{} Milimetros igual a {} Millas'.format(unidadentrada))
    elif menu_dos == 5:
        print('{} Milimetros es igual a {} Milimetros'.format(unidadentrada))
    elif menu_dos == 6:
        centrimetro = unidadentrada * 0.1
        print('{} Milimetros es igual a {} Centimetros'.format(unidadentrada,centrimetro))
    elif menu_dos == 7:
        metro = unidadentrada * 0.001
        print('{} Milimetros igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.000001
        print('{} Milimetros es igual a {} Kilometros'.format(unidadentrada,kilometro))


'''
Menu Centimetros
'''
#-----------------------------------------------------------Centimetros-------------------------------------------------------------------------------
def operacionesCm(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 0.393701
        print('{0} Centimetros es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 0.0328084
        print('{} Centimetros es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        yarda = unidadentrada * 0.0109361
        print('{} Centimetros es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        milla = unidadentrada * 0.062137
        print('{} Centimetros igual a {} Millas'.format(unidadentrada))
    elif menu_dos == 5:
        milimetro = unidadentrada * 10
        print('{} Centimetros es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        print('{} Centimetros es igual a {} Centimetros'.format(unidadentrada))
    elif menu_dos == 7:
        metro = unidadentrada * 0.01
        print('{} Centimetros igual a {} Metros'.format(unidadentrada,metro))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.00001
        print('{} Centimetros es igual a {} Kilometros'.format(unidadentrada,kilometro))

'''
Menu Metros
'''
#---------------------------------------------------------Metros-------------------------------------------------------------------------------
def operacionesMe(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 39.3701
        print('{0} Metros es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 3.28084
        print('{} Metros  es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        yarda = unidadentrada * 1.09361
        print('{} Metros  es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        milla = unidadentrada * 0.000621371
        print('{} Metros  igual a {} Millas'.format(unidadentrada))
    elif menu_dos == 5:
        milimetro = unidadentrada * 1000
        print('{} Metros  es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centimetro = unidadentrada* 100
        print('{} Metros  es igual a {} Centimetros'.format(unidadentrada,centimetro))
    elif menu_dos == 7:
        print('{} Metros  igual a {} Metros'.format(unidadentrada))
    elif menu_dos == 8:
        kilometro = unidadentrada * 0.001
        print('{} Metros  es igual a {} Kilometros'.format(unidadentrada,kilometro))

'''
Menu Kilometros
'''
#---------------------------------------------------------Kilometros-------------------------------------------------------------------------------
def operacionesKi(unidadentrada,menu_dos):
    if menu_dos == 1:
        pulgadas = unidadentrada * 39370.1
        print('{0} Kilometros es igual a {0} Pulgadas'.format(unidadentrada,pulgadas))
    elif menu_dos == 2:
        pie = unidadentrada * 3280.84
        print('{} Kilometros  es igual a {} Pies'.format(unidadentrada,pie))
    elif menu_dos == 3:
        yarda = unidadentrada * 1093.61
        print('{} Kilometros  es igual a {} Yardas'.format(unidadentrada,yarda))
    elif menu_dos == 4:
        milla = unidadentrada * 0.621371
        print('{} Kilometros igual a {} Millas'.format(unidadentrada))
    elif menu_dos == 5:
        milimetro = unidadentrada * 1000000
        print('{} Kilometros es igual a {} Milimetros'.format(unidadentrada,milimetro))
    elif menu_dos == 6:
        centimetro = unidadentrada* 100000
        print('{} Kilometros  es igual a {} Centimetros'.format(unidadentrada,centimetro))
    elif menu_dos == 7:
        metro = unidadentrada * 1000
        print('{} Kilometros  igual a {} Metros'.format(unidadentrada, metro))
    elif menu_dos == 8:
        print('{} Kilometros  es igual a {} Kilometros'.format(unidadentrada,))


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
    eleccion = input('Desea Continuar  |1| \'SI\'    |2|  \'NO\': ').lower()
            


                                                                    

import tkinter as tk
import random
# Crear una instancia - class Tk()
# Create a new instance - class Tk()
# Nueva instancia de la clase Tk

my_window = tk.Tk()
# funcion para hacer los cambios de colores del fondo
num_hex = []

def changeBG():
    # create List for adding number random
    #crear lista para guardar numeros random
    random_num_hex_list= []
    #number HEx
    #numeros hexadecimales
    num_hex =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','F']
    #loop for, create list number random
    #ciclo for, para crear la lista de numeros random
    for i in range (6):
        random_num_hex = random.choice(num_hex)
        random_num_hex_list.append(random_num_hex)
    # print para validar la lista
    #print to validate the list
    print(random_num_hex_list)
    # crear codigo de color Hexadecimal
    #create color code from hexadecimals
    bg_color='#{0}{1}{2}{3}{4}{5}'. format(random_num_hex_list[0],random_num_hex_list[1],random_num_hex_list[2],
                                           random_num_hex_list[3],random_num_hex_list[4],random_num_hex_list[5])
    #print para validar el codigo de color Hexadecimal
    # print to validate color code from hexadecimal
    print(bg_color)
    # lo que hara la funcion cada vez que se oprima el boton
    # what the function will do each time the button is pressed
    my_window.config(background = bg_color)

#Creas un Titulo a la ventana
# Let's create a title and some text
my_window.title("Changes BG COLOR")
# Range of window aplication
my_window.geometry("520x200")
# Block size
my_window.resizable(False,False)
#Configurando el Color de Fondo
#config background COLOR
my_window.config(background = '#2798FA')
#Agregar un Texto Estilo Titulo Configurando Texto, Color, Fondo, Tamaño y Letra
# add a text style , Title, Tex Color, Backlground, size, style text.
main_title = tk.Label(text= "Tkinter - ejercice 2",font=('Tahoma',16),bg= '#ff7763', fg= 'black', width= '60', height= '4')
# Lugar donde colocar el Texto por cordenadas
# Place where the text will be placed
main_title.place(x=0, y=10)
# adding a button
# Agregar el boton
main_btn = tk.Button(my_window, text= 'Change Background Color', command= changeBG)
main_btn.place(x=190, y= 150)







#lanzamos la aplicacion - para evitar que se cierre se usara mainloop method
# Let's lauch the application - preveting closing using mainloop method
my_window.mainloop()

import tkinter as tk

# Crear una instancia - class Tk()
# Create a new instance - class Tk()
# Nueva instancia de la clase Tk

my_window = tk.Tk()

#Creas un Titulo a la ventana
# Let's create a title and some text
my_window.title("Python + Tkinter GUI")
# Range of window aplication
my_window.geometry("600x400")
# Block size
''' my_window.resizable(False,False) '''
#Configurando el Color de Fondo
#config background COLOR
my_window.config(background = '#2798FA')
#Agregar un Texto Estilo Titulo Configurando Texto, Color, Fondo, Tamaño y Letra
# add a text style , Title, Tex Color, Backlground, size, style text.
main_title = tk.Label(text= "Tkinter - ejercice 1",font=('Tahoma',16),bg= '#ff7763', fg= 'black', width= '60', height= '4')
# Lugar donde colocar el Texto por cordenadas
# Place where the text will be placed
main_title.place(x=0, y=50)


#lanzamos la aplicacion - para evitar que se cierre se usara mainloop method
# Let's lauch the application - preveting closing using mainloop method
my_window.mainloop()



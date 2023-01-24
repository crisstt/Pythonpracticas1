from tkinter import *
from tkinter import ttk

class Ventana(Frame):
    def __init__(self, master = None):
        super().__init__(master,width=1560, height=1000)
        self.master = master
        self.pack()
        self.create_widgets()
    
    
    def create_widgets(self):
        ventana1 = Frame(self, bg="#8f4900",pady= 2, padx = 2)
        ventana1.place(width = 778, height = 498)
        ventana2 = Frame(self, bg="#8f4900",pady= 2, padx = 2)
        ventana2.place(x = 780, y = 0,width = 778, height = 498)
        self.btnNuevo=Button(ventana2,text="Nuevo", command=None, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(ventana2,text="Modificar", command=None, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)
        
        ventana3 = Frame(self, bg="#8f4900",pady= 2, padx = 2)
        ventana3.place(x = 0, y = 500, width = 778, height = 498)
        ventana4 = Frame(self, bg="#8f4900",pady= 2, padx = 2)
        ventana4.place(x = 780, y = 500,width = 778, height = 498)
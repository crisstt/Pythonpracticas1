# CREATE A DIGITAL CLOCK USING PYTHON AND TKINTER ------ CLASS-----------
import time
import tkinter as tk
import datetime
from datetime import date

class Digital_clock():
    #costructor de la clase, cada vez que se pide una nueva instancia se ejecuta primero
    def __init__(self):
        #redefinir el TK la ventana
        self.myWindow = tk.Tk()
        # Las medidas de la ventana
        # Size Window
        self.myWindow.geometry('600x380')
        # Bloquear el cambio de tamaño
        #Block Resizable
        self.myWindow.resizable(0,0)
        #Titulo de la ventana
        # Title of the window
        self.myWindow.title('Creating a Digital Clock | Python and Tkinter | Example 4')
        # configura el fondo de la ventana
        #config the background of the window
        self.myWindow.configure(background = '#1f2f3f')
        #Crea el texto que quieres mopstrar en la ventana y se configura
        # Create text to config
        self.current_time_label = tk.Label(text = '', font = ('Tahoma',44), fg= '#ffffff', bg= '#72a922', pady= 10, padx= 10)
        #Crea el texto que quieres mopstrar en la ventana y se configura
        # Create text to config
        self.week_day_label = tk.Label(text = '', font = ('Tahoma',12), fg= '#ffffff', bg= '#72a922', pady= 10, padx= 10)
        #Crea el texto que quieres mopstrar en la ventana y se configura
        # Create text to config
        self.name_creator_label = tk.Label(text = 'EVERPLAY', font = ('Tahoma',12), fg= '#ffffff', bg= '#72a922', pady= 10, padx= 10)
        #metodo place para posicionar
        #method place
        self.current_time_label.place(x=175 , y=50)
        #metodo place para posicionar
        #method place
        self.week_day_label.place(x=220 , y=160)
         #metodo place para posicionar
        #method place
        self.name_creator_label.place(x=245, y=220)
        self.update_clock()
        self.week_date()
        self.myWindow.mainloop()

    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.current_time_label.configure(text = now)
        self.myWindow.after(1000,self.update_clock)

    def week_date(self):
        #get week day
        #buscar el dia
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime('%A')
        #Get current date
        #Mostrar las fechas segun formato siguiente
        today= date.today()
        d1 = today.strftime('%d/%m/%y')
        self.week_day_label.configure(text = d1 + ' | ' + week_day)
    
        

main = Digital_clock()

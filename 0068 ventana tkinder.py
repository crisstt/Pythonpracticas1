import tkinter as tk
# importar de tkinter messagebox
from tkinter import messagebox

myWindow = tk.Tk()
myWindow.title('Boton de Mensaje')

def myMenssage():
    messagebox.showinfo('information!', 'A simple info message! ')

btn1 = tk.Button(myWindow, text= '1er Boton', command = myMenssage)
#btn1.pack()
btn1.place (x=75, y=50)

myWindow.mainloop()


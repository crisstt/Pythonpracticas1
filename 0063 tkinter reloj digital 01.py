import tkinter
from time import strftime

# conviertes el TK en una variable mas sencilla Root la ventana
#you convert the TK into a simpler variable Root the window
root = tkinter.Tk()
# Agregas titulo a la ventana
# adding title a window
root.title=('DIGITAL CLOCK :::::: Example 3')
#Creas un espacio para colocar el elemento
#create Label to place element
myClock = tkinter.Label()
# Crea el textop que contendra
# Create the text that will contain the label
myClock['text'] = ' 21:18:00 '
# metodo pack usado para ajusta los elementos y luego la ventana tome el tamaño necesario
# pack method used to fit the elements and then the window takes the necessary size
myClock.pack()
# Modifica el tamaño de Texto y su stilo
# Modify the size and style the text
myClock['font'] = 'Tahoma 150 bold'
# Metodo strftime() devuelve la fecha segun  %H, %M ,%S
# strftime() Method returns a string representing data and time using date,time or datetime object
strftime('%H:%M:%S')

def tic():
    myClock['text'] = strftime('%H:%M:%S')

tic()

def tac():
    tic()
    myClock.after(1000,tac)

tac()

myClock['fg'] = 'black'
myClock['bg'] = '#2ffbf0'

# CREATE A DIGITAL CLOCK USING PYTHON AND TKINTER
import time
import tkinter as tk
import datetime
from datetime import date

myWindow = tk.Tk()
myWindow.geometry('400x180')
myWindow.resizable(0,0)
myWindow.title('Creating a Digital Clock | Python and Tkinter | Example')
myWindow.configure(background = '#1f2f3f')
current_time_label = tk.Label(text = time.strftime(' %H:%M:%S '), font = ('Tahoma',44), fg= '#ffffff', bg= '#443355', pady= 10, padx= 10)
current_time_label.place(x=70 , y=40)
print(current_time_label['text'])

def update_clock():
    time_now = time.strftime(' %H:%M:%S ')
    if current_time_label['text'] != time_now:
        current_time_label['text'] = time_now
        print(current_time_label['text'])
    myWindow.after(1000, update_clock)

update_clock()
myWindow.mainloop()

main = Digital_clock()

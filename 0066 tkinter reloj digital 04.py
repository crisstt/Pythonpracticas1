import tkinter as tk
from time import strftime

def time():
    get_hour = strftime('%I:%M:%S %p')
    my_day = strftime('%a')
    label.config(text = get_hour)
    label.after(1000,time)
    label2.config(text= my_day)
    


my_window = tk.Tk()
my_window.title("My Digital Clock - Easy Version")
my_window.geometry("400x180")
my_window.resizable(False,False)
my_window.config(background = '#1f2f85')

label = tk.Label(my_window, font = ("Open Sans", 50), background = "black", foreground = "lime")
label.place(x = 5, y = 30)
label2 = tk.Label(my_window, font = ('Raleway', 20), background = '#554455', foreground = 'white')
label2.place(x = 170, y = 130)

time()
my_window.mainloop()

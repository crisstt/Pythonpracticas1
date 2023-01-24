import tkinter as tk

mywindow = tk.Tk()
mywindow.geometry("650x550")
mywindow.title("Formulario de Registro || Python y Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = tk.Label(text = "Ventana Transparente", font=("Cambria",16), bg= "#56CD63", fg = "Black",width = "500", height = "2")
main_title.pack()
# para agregar los valores de transparencia de la ventana es de  0 y 1
mywindow.wm_attributes("-alpha", 0.4)

mywindow.mainloop()

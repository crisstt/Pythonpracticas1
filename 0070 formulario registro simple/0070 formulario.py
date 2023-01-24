from tkinter import *

#Funcion que guarda la informacion del formulario

def send_data():
    # se recupera la informacion de las variables por medio de get()
    username_data = username.get()
    password_data = str(password.get())
    fullname_data = fullname.get()
    age_data = str(age.get())
    # Imprimir informacion optenida
    print(username_data, "\t" , password_data, "\t" , fullname_data, "\t", age_data)

    # se crea un documento con la informacion optenida y se guarda
    newfile = open("form_registration.txt", "a")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write(password_data)
    newfile.write("\t")
    newfile.write(fullname_data)
    newfile.write("\t")
    newfile.write(age_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo Usuario Registrado. UserName: {} | FullName{}   ".format(username_data,fullname_data))
    

    # metodo delete para borrar los espacios de texto capturados
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)


mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Formulario de Registro || Python y Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
mywindow.iconbitmap('C:\\Users\\zxxma\\Documents\\Respaldo pc Cristian, programacion\\Python\\0070 formulario registro simple\\continuar.ico')
main_title = Label(text = "Formulario de Registro Python", font=("Cambria",16), bg= "#56CD63", fg = "Black",width = "500", height = "2")
main_title.pack()

# Se ingresan las Cabeceras de cada una de los datos a pedir
username_label = Label (text = "Username", bg= "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label (text = "Password", bg= "#FFEEDD")
password_label.place(x = 22, y = 130)
Fullname_label = Label (text = "Fullname", bg= "#FFEEDD")
Fullname_label.place(x = 22, y = 190)
age_label = Label (text = "Age", bg= "#FFEEDD")
age_label.place(x = 22, y = 250)

# se le asigna un StringVar a una variable
username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

# se asocialas variables anteriores a los espacios donde se les asignara la informacion atravez de textvariable

username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40", show ="*")
fullname_entry = Entry(textvariable = fullname, width = "40")
age_entry = Entry(textvariable = age, width = "40")

# usar la sentencia place para posicionar las entradas de texto

username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
fullname_entry.place(x = 22, y = 220)
age_entry.place(x = 22, y = 280)

# se generan los botones para guardar la información

submit_btn = Button(mywindow, text = "Submit info", command = send_data, width = "30", height = "2", background = "#00CD63")
submit_btn.place(x = 22, y = 320)

mywindow.mainloop()








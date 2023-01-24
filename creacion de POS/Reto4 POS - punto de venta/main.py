
from tkinter import *
from ventana import *
from v_principal import *


def main():
    root = Tk()
    root.wm_title("Sistema de Puntos de Venta")
    app = Ventana(root) 
    app.mainloop()



if __name__ == "__main__":
    main()
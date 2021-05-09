from tkinter import *
import random

ventana = Tk()

ventana.title('Ejercicio 4.0')
ventana.resizable(0,0)
ventana.geometry("600x400")

#funciones

def opcionUno():
    numero = random.randrange(0,11)
    return etiqueta.configure(text=numero)

def opcionDos():
    numero = random.randrange(0, 51)
    return etiqueta.configure(text=numero)

def opcionTres():
    numero = random.randrange(0, 101)
    return etiqueta.configure(text=numero)


#Botones

botonUNo = Button(ventana, text= 'Num entre 0 y 10', bg='blue', fg='#ffffff', command=opcionUno)
botonUNo.grid(column=1,row=0)
botonDos = Button(ventana, text = 'Num entre 0 y 50', bg='green', fg='#ffffff', command=opcionDos)
botonDos.grid(column=2,row=0)
botonTres = Button(ventana, text='Num entre 0 y 100', bg='red', fg='#ffffff', command=opcionTres)
botonTres.grid(column=3, row=0)

#Etiqueta

etiqueta = Label(ventana, text='...', bg='orange')
etiqueta.grid(column=2, row=2)
ventana.mainloop()
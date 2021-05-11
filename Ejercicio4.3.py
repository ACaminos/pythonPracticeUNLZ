from tkinter import *
from tkinter import messagebox as MessageBox

contador=''
click = 0
ventana = Tk()
ventana.title('Ejercicio 4.3')
ventana.resizable(0,0)
ventana.geometry('600x400')

#Funciones

def ingreso():
    num = texto.get()
    lista.append(int(num))
    texto.delete(0,30)

def modificar():
    MessageBox.showinfo("Usted ingreso los numeros: ",lista)
    duplicados()
    lista.sort()
    MessageBox.showinfo('Numeros ordenados: ',lista)
    duplicados()
    MessageBox.showinfo('Numeros sin repetir: ',lista)
    impares()
    MessageBox.showinfo('Numeros sin impares: ',lista)
    suma(lista)
    MessageBox.showinfo('Suma de los numeros ingresados sin repetir: ',lista)

def duplicados():
    for listado in lista:
        if texto not in list:
            lista.append(int(texto.get()))

def impares():
    if num%2 == 0:
        lista.remove(int(num))

def suma(lista):
    resultadoFinal = 0
    for i in lista:
        resultadoFinal = resultadoFinal+i
        return resultadoFinal
        lista.insert(0, resultadoFinal)
#lista

lista = []


#Etiquetas
etiqueta = Label(ventana, text='Ingrese 5 numero')
etiqueta.grid(column=0, row=0)

texto = Entry(ventana, width=30)
texto.grid(column=1, row=0)

ingresoNum=Button(ventana, text='ingresar', command=ingreso)
ingresoNum.grid(column=2, row=0)

stop = Button(ventana, text='Stop!', command=modificar)
stop.grid(column=3, row=0)

etiqueta2= Label((ventana))
etiqueta.grid(column=0, row=0)


ventana.mainloop()
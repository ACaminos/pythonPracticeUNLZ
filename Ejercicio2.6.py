palabra = ''
lista = []
i = 0
cantPalabras = int(input('ingrese cant de palabras a ingresar: '))
while i < cantPalabras :
    palabra = input('ingrese la palabra: ')
    lista.append(palabra)
    i = i+1

print(lista)
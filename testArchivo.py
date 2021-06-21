respuesta = 's'

opcion = input("Que opcion quiere realizar?\n1 - Crear un archivo nuevo\n2 - Abrir y leer un archivo creado\n\n")

if opcion == '1':

    fileName = input(str("ingrese el nombre del archivo:\t"))

    file = open(fileName+'.txt','w')
    while respuesta == 's':
        nombre = input('ingrese nombre:\t')
        apellido = input('ingrese apellido:\t')
        dni = input('ingrese DNI:\t')
        file.write(nombre+','+apellido+','+dni+'\n')
        print('\n')

        respuesta=input("Desea agregar un usuario mas?\ts/n\t")
        if respuesta != 's':
            break
    file.close()
elif opcion == '2':
    archivo = input(str("\nIngrese el nombre del archivo txt, sin su extension:\t"))
    openFile = open(archivo+'.txt','r')
    contenido = openFile.read()
    print('\n\n')
    print(contenido)
    openFile.close()
else:
    print('Error')

## Primero crear archivo para poder hacer uso de la opcion 2 - Leer archivo ##

respuesta = 's'
opcion = input("Que opcion quiere realizar?\n1 - Crear un archivo nuevo\n2 - Abrir y leer un archivo creado\n\n")

if opcion == '1':

    fileName = input(str("ingrese el nombre del archivo:\t"))

    file = open(fileName+'.txt','w')
    while respuesta == 's':
        nombre = input('ingrese nombre:\t')
        apellido = input('ingrese apellido:\t')
        dni = input('ingrese DNI:\t')
        file.write(dni+','+nombre+','+apellido,'\n')
        print('\n')

        respuesta=input("Desea agregar un usuario mas?\ts/n\t")
        if respuesta != 's':
            break
    file.close()
elif opcion == '2':
    archivo = input(str("\nIngrese el nombre del archivo txt, sin su extension:\t"))
    openFile = open(archivo+'.txt','r')
    contenido = openFile.readlines()
    print('\n\n')
    busqueda = input(str('Ingrese los 8 numeros del dni a buscar:\t'))

    for x in contenido:
        if busqueda == x[:len(busqueda)]:
            lista_datos = x
            break

    lista_datos = lista_datos.split(sep=',')
    print('DNI: ',lista_datos[0])
    print('Nombre: ',lista_datos[1])
    print('Apellido: ',lista_datos[2])
    openFile.close()
else:
    print('Error')

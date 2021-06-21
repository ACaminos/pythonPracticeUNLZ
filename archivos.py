respuesta = 's'

datos1 = open('datos.txt','w')

while respuesta == 's':
    nombre = input('Ingrese el nombre:\t')
    apellido = input('ingrese el apellido:\t')
    dni = input('ingrese el DNI:\t')
    datos1.write(nombre + '-' + apellido + '-' + dni + '\n\n')
    print('\n\n')

    respuesta = input('Desea ingresar mas datos?\t s = Si\t n = No :\t')
    if respuesta != 's':
        break
    else:
        respuesta = 's'

datos1.close()

print ('archivo generado exitosamente!')

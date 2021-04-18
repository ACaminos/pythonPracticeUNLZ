import os
opcionA = ''
opcionB = ''
opcionC = ''
opcionD = ''

print('\nA = Usuario \t \t B = Configuracion \t \tC = Idioma \t \tD = Ayuda ')

opcion = input('\n\nIngrese opcion A, B, C o D : \t')

if opcion == 'a' or 'A' or 1 :
    os.system("clear")
    print('Bienvenido a la seccion Usuario')
elif opcion == 'b' or 'B' or 2 :
    os.system("clear")
    print('Menu de configuracion del usuario')
elif opcion == 'c' or 'C' or 3 :
    os.system("clear")
    print('Seccion idiomas')
elif opcion == 'd' or 'D' or '4' :
    os.system("clear")
    print('Menu de ayuda al usuario')
else :
    os.system("clear")
    print('Error - opcion no encontrada -')

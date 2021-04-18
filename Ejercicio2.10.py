import os

eleccion=''
while eleccion != 2 : 
    print('Ingrese dos numeros:')
    primerN = int(input('Primer numero:\t'))
    segundoN = int(input('Segundo numero:\t'))

    os.system("clear")

    print('\nA = Suma \t \t B = Resta \t \tC = Multiplicacion \t \tD = Division ')

    opcion = input('\n\nEliga una de las opciones : \t')

    if opcion == 'a' or opcion == 'A' or opcion == 1 :
        os.system("clear")
        resultado = primerN + segundoN
        print('Resultado de la suma: ',resultado)
        eleccion = int(input('\n\nContinuar = 1\nSalir = 2 : \t'))
        os.system("clear")
    else :
        if opcion == 'b' or opcion == 'B' or opcion == 2 :
            os.system("clear")
            resultado = primerN - segundoN
            print('Resultado de la resta: ',resultado)
            eleccion = int(input('\n\nContinuar = 1\nSalir = 2 :\t'))
            os.system("clear")
        else :
            if opcion == 'c' or opcion == 'C' or opcion == 3 :
                os.system("clear")
                resultado = primerN * segundoN
                print('Resultado de la multiplicacion: ',resultado)
                eleccion = int(input('\n\nContinuar = 1\nSalir = 2 :\t'))
                os.system("clear")
            else :
                if opcion == 'd' or opcion == 'D' or opcion == '4' :
                    os.system("clear")
                    if opcion == 0 :
                        print('No se puede dividir por 0')
                        eleccion = int(input('\n\nContinuar = 1\nSalir = 2 :\t'))
                        os.system("clear")
                    else :
                        resultado = primerN / segundoN
                        print('Resultado de la division: ',resultado)
                        eleccion = int(input('\n\nContinuar = 1\nSalir = 2 :\t'))
                        os.system("clear")
                else :
                    os.system("clear")
                    print('Error - opcion no encontrada -')
                    eleccion = int(input('\n\nContinuar = 1\nSalir = 2 :\t'))
                    os.system("clear")

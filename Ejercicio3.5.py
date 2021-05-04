consulta = ''
while consulta != False :
    numero = int(input("Ingrese un numero: \t "))

    resultado = numero**3

    print("El numero ", numero, "elevado al cubo, tiene como resultado : ",resultado, "\n")
    
    consulta = int(input("Para salir del programa, oprima el cero ( 0 ), caso contrario, cualquier tecla: \t"))

    if consulta == 0 :
        consulta = False
primerNumero = int(input('Ingrese el primer numero Real: '))
segundoNumero = int(input('Ingrese el segundo numero Real: '))
if segundoNumero <= 0 :
    suma = primerNumero + segundoNumero
    resta = primerNumero - segundoNumero
    multiplicacion = primerNumero * segundoNumero

    print('---------------- Resultados -------------------')
    print('')
    print('Suma: ',suma)
    print('Resta: ',resta)
    print('Multiplicacion: ', multiplicacion)
    print('La division no se puede realizar')
else :
    suma = primerNumero + segundoNumero
    resta = primerNumero - segundoNumero
    multiplicacion = primerNumero * segundoNumero
    division = primerNumero / segundoNumero

    print('---------------- Resultados -------------------')
    print('')
    print('Suma: ',suma)
    print('Resta: ',resta)
    print('Multiplicacion: ', multiplicacion)
    print('division: ', division)
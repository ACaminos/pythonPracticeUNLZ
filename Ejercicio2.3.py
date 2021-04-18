lista = []
pares = 0
primerNumero = int(input('ingrese primer numero: '))
segundoNumero = int(input('ingrese numero final: '))

if primerNumero < segundoNumero :
    while primerNumero <= segundoNumero :
        if primerNumero%2 == 0 :
            lista.append(primerNumero)
            pares = pares + 1
            primerNumero = primerNumero + 1
        else :
            primerNumero = primerNumero + 1
else :
    print('El primer numero es mayor que el segundo numero ingresado ... Error 404 (? ')

print('los numeros pares encontrados entre los numeros ingresados son : ',lista)
print('cantidad de numeros pares: ',pares)
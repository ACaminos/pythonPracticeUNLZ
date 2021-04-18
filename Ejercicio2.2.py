divisor = 1
lista = []
numero = int(input('ingrese un numero mayor que cero: '))
if numero > 0 :
    while divisor <= 9 :
        if numero%divisor == 0:
            lista.append(divisor)
            divisor = divisor + 1

        else :
            divisor = divisor + 1
else :
    print('No se encontraron divisores exactos')

print('Los divisores del numero ingresado son: ',lista)


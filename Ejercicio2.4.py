numero = ''
lista = []
numMin = 999999999999999
numMax = 0
while numero != 0 :
    numero = int(input('ingrese un numero: '))
    lista.append(numero)
    if numero > numMax :
        numMax = numero
    if numero == 0 :
        break
    if numero < numMin :
        numMin = numero

print('El numero min es : ', numMin)
print('El numero max es : ', numMax)

    
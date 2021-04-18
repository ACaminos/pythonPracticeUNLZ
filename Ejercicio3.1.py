
resultado = ''
numero = int(input('ingrese un numero positivo :\t'))
contador = numero -1
if numero > 0 :
    while numero != 0 :
        resultado = numero * numero
        numero-=1

else :
    print('Error')

lista = []
contador = 0
palabra = ''

print('Ingrese 10 palabras de a una por vez \n')

while contador < 10 :
    palabra = input('ingrese palabra : ')
    lista.append(palabra)
    contador = contador + 1

Ultimapalabra = input('ingrese una ultima palabra: ')

if lista.count(Ultimapalabra) == 0 :
    print('La palabra ' + Ultimapalabra +' no se encuentra repetida en la lista que ingreso')
    print(lista)
else :
    print('La palabra ' + Ultimapalabra + ' se encuentra repetida')
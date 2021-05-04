vocales = 'aeiouAEIOU'

def getVocales(frase):
    return set([letra for letra in frase if letra in vocales])

def getConsonantes(frase):
    return set([letra for letra in frase if letra not in vocales])

fraseIngresada = input("Ingrese una Frase: ")

print("Las Vocales de la Frase Ingresa son: ", getVocales(fraseIngresada),"\n")
print("Las Consonantes de la Frase Ingresa son: ", getConsonantes(fraseIngresada), "\n")
print("Frase Ingresada:", fraseIngresada)
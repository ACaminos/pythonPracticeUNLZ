def m2(v):
    if v%2 == 0:
        print("Es multiplo de 2")
    else:
        print("No es multiplo de 2")

def m3(v):
    if v%3 == 0:
        print("Es multiplo de 3")
    else:
        print("No es multiplo de 3")

#Funcion Orden superior

def multiplo(v, fn):
    return fn(v)

#Cuerpo del programa

multiplo(12, m2)
multiplo(39,m3)
multiplo(4, m3)
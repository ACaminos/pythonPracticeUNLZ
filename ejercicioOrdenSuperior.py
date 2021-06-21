#Ejercicio propuesto: Hacer una función de orden superior llamada Operador
# que reciba dos valores y otra función como parámetros.
# Las funciones que pasemos por parámetro deberán ser Sum, Resta,Multiplicación y División.
# Probar con al menos un valor cada una de ellas.


#funcion suma
def suma(n1,n2):
    resultado = n1+n2
    print('El resultado es:\t',resultado)

#funcion resta
def resta(n1,n2):
    resultado = n1-n2
    print('El resultado es:\t',resultado)

#funcion multiplicacion
def multiplicacion(n1,n2):
    resultado = n1*n2
    print('El resultado es:\t',resultado)

#funcion division
def division(n1,n2):
    if n2==0:
        print("No se puede dividir por cero")
    else:
        resultado = n1/n2
        print('El resultado es:\t',resultado)

#Funcion orden superior
def operador(n1,n2,fn):
    return fn(n1,n2)


operador(2,2,suma)

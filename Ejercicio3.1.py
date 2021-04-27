a = ''

a = int(input("ingrese un numero entero :\t"))

def calculaFactorial(n):
  if n>0:
    n = n * calculaFactorial(n - 1)
  else:
    n = 1
  return n

factorial_a = calculaFactorial(a)
print ("El factorial de ", a ,"es ",factorial_a)
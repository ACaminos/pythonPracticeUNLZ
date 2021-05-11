class calculadora:
    resultado = ''
    firstNum = ''
    secondNum = ''
    operador = ''

    def numeros (self, num1, num2, operador):
        self.firstNum = num1
        self.secondNum = num2
        self.operador = operador

        if operador == 1:
            resultado = num1 + num2
            print('El resultado de la suma es:\t',resultado)
        
        if operador == 2:
            resultado = num1 - num2
            print('El resultado de la resta es:\t',resultado)
        
        if operador == 3:
            resultado == num1 * num2
            print('El resultado de la multiplicacion es:\t',resultado)
        
        if operador == 4:
            if num2 > 0:
                resultado = num1 / num2
                print('El resultado de la division es:\t',resultado)
            else:
                print('error')

        
    
primerNumero = int(input('Ingrese un numero:\t'))
segundoNumero = int(input('Ingrese segundo numero:\t'))
operando = int(input('Ingrese el operador:\n Suma = 1 \n Resta = 2 \n Multiplicacion = 3 \n Division = 4 \n\n\nOpcion:\t'))

Calculadora = calculadora()

Calculadora.numeros(primerNumero,segundoNumero,operando)
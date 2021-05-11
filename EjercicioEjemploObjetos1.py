class calculadora:
    resultado = ''

    def suma(self, num1, num2):
        self.resultado = num1 + num2
        print('El resultado de la suma es : ', self.resultado)
    
numero1 = int(input('Ingrese un numero:\t'))
numero2 = int(input('Ingrese segundo numero:\t'))

calculadora = calculadora()

calculadora.suma(numero1,numero2)
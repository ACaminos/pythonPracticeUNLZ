#Objetos explicacion de la guia

class auto:
    color = 'sin color'
    modelo = 'sin modelo'
    puertas = 'sin datos'

    def pintar(self,pintura):
        self.color = pintura
    
    def marca(self, Marca):
        self.modelo = Marca
    
    def puerta(self, Puertas):
        self.puertas = Puertas

#objeto
vw = auto()
fiat = auto()

#Ver atributos

vw.pintar('azul electrico')
print('VW color: ',vw.color)
vw.marca('Peugeot')
print('VW modelo: ',vw.modelo)
vw.puerta(3)
print('VW puertas: ',vw.puertas)
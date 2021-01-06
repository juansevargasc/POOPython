
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): #Esto significa que el cuadrado extiende del Rectangulo
    def __init__(self, lado):
        super().__init__(lado, lado) #Inicializamos la super clase. Requiere base, altura.
    
if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
    
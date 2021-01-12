class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona1 = Persona('David')
    persona1.avanza()

    ciclista1 = Ciclista('Daniel')
    ciclista1.avanza()

if __name__ == '__main__':
    main()
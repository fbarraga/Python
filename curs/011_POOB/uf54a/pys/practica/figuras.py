import math

class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.base + 2*self.altura

    def __str__(self):
        return f'{self.nombre}[base:{self.base} altura:{self.altura}]'

class Circulo(Figura):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f'{self.nombre}[radio:{self.radio}]'


def probar_figura(figura):
    print(figura)
    print('Area: ', figura.area())
    print('Perimetro: ', figura.perimetro())

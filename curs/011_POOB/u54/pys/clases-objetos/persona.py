
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostra_datos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)

    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
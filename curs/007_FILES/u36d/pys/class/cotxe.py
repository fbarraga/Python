class Cotxe:
    # constructor de la classe
    def __init__(self,mat,mar,mod,col,mot,ann):
        self.matricula = mat
        self.marca = mar
        self.model = mod
        self.color = col
        self.motor = mot
        self.ann = ann
    
    def obtenir_matricula(self):
        return self.matricula.upper()
    
    def obtenir_marca(self):
        return self.marca.title()
    
    def obtenir_model(self):
        return self.model.title()
    
    def obtenir_color(self):
        return self.color
    
    def obtenir_motor(self):
        return self.motor.title()
    
    def obtenir_ann(self):
        return self.ann
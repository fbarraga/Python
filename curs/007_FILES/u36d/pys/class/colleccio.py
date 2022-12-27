import cotxe
import pickle

class Colleccio:
    def __init__(self):
        self.dades_cotxes = []
    
    def afegir(self,c):
        self.dades_cotxes.append(c)

    def mostrar(self):
        for o in self.dades_cotxes:
            print(f"{o.obtenir_matricula()} {o.obtenir_marca()} {o.obtenir_model()} ({o.obtenir_ann()})")

    def carregar(self,f):
        try:
            with open(f,'rb') as fitxer:
                self.dades_cotxes = pickle.load(fitxer)
                return len(self.dades_cotxes)
        except:
            return 0
    
    def emmagatzemar(self,f):
        fitxer = open(f,'wb')
        pickle.dump(self.dades_cotxes,fitxer)
        fitxer.close()
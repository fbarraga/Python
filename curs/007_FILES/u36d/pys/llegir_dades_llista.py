import pickle
fitxer = open('dades.pckl','rb')
llista = pickle.load(fitxer)
print(llista)
fitxer.close
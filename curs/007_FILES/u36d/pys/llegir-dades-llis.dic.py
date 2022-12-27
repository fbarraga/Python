import pickle
fitxer = open('dades.pckl','rb')
ll = pickle.load(fitxer)
for e in ll:
nom = e['nom']
cognom = e['cognom']
print(f"{cognom}, {nom}")
fitxer.close
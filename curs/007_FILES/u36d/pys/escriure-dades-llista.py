import pickle
llista = ['anna','lluis','pere','laura','maria','joan','manel','joan']
fitxer = open('dades.pckl','wb')
pickle.dump(llista,fitxer)
fitxer.close
import pickle
p1 = {'nom': 'eva', 'cognom': 'garcia'}
p2 = {'nom': 'anna', 'cognom': 'felip'}
p3 = {'nom': 'joan', 'cognom': 'garcia'}
p4 = {'nom': 'manel', 'cognom': 'lopez'}
ll = [p1,p2,p3,p4]
fitxer = open('dades.pckl','wb')
pickle.dump(ll,fitxer)
fitxer.close
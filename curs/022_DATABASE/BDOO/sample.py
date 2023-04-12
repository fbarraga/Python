# persones.py
from tinydb import TinyDB, Query

bdd_persones = TinyDB('bddp.json')
bdd_persones.insert({'nom': 'laura', 'cognoms': 'garcia sanchez', 'edat': 17})
bdd_persones.insert({'nom': 'pere', 'cognoms': 'sanchez velez', 'edat': 19})
bdd_persones.insert({'nom': 'marta', 'cognoms': 'garcia vidal', 'edat': 21})
bdd_persones.insert({'nom': 'joan', 'cognoms': 'moreno garcia', 'edat': 13})
bdd_persones.insert({'nom': 'anna', 'cognoms': 'garcia mendez', 'edat': 23})
print(f"bdd_persones es del tipus {type(bdd_persones)}")
print()
print("Les dades de totes les persones")
for p in bdd_persones:
    print(p)
print()
print("Les dades d'en Joan")
consulta = bdd_persones.search(Query().nom == 'joan')
print(consulta)
print()
print("Les dades de les persones menors d'edat")
consulta = bdd_persones.search(Query().edat < 18)
for p in consulta:
    print(p)
bdd_persones.close()
import sys
from tinydb import TinyDB, Query

planeta = sys.argv[1]
dades_planetes = TinyDB('bddpla.json')
for p in dades_planetes:
 if (p['nom'] == planeta): 
    print(f"{p['unitat_astronomica']}")
dades_planetes.close()

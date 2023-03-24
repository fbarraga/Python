from tinydb import TinyDB, Query

dades_planetes = TinyDB('bddpla.json')
dades_planetes.insert_multiple([
 {'nom': 'terra', 'sistema_estel·lar': 'sistema solar', 'estrella': 'sol', 'unitat_astronomica': 1.00},
 {'nom': 'mart', 'sistema_estel·lar': 'sistema solar', 'estrella': 'sol', 'unitat_astronomica': 1.524},
 {'nom': 'pluto', 'sistema_estel·lar': 'sistema solar', 'estrella': 'sol', 'unitat_astronomica': 39.3},
 {'nom': 'jupiter', 'sistema_estel·lar': 'sistema solar', 'estrella': 'sol', 'unitat_astronomica': 5.203},
 {'nom': 'proxima b', 'sistema_estel·lar': 'alfa centauri', 'estrella': 'proxima centauri', 'unitat_astronomica': 0}])
print()
for p in dades_planetes:
 print(f"{p.doc_id} {p['nom']} ({p['sistema_estel·lar']}, {p['unitat_astronomica']})")
print()
consulta = dades_planetes.search((Query().sistema_estel·lar == 'sistema solar') & (Query().unitat_astronomica < 10))
for c in consulta:
 print(f"{c.doc_id} {c['nom']} ({c['sistema_estel·lar']}, {c['unitat_astronomica']})")
print()
dades_planetes.remove(Query().nom == 'pluto')
for p in dades_planetes:
 print(f"{p.doc_id} {p['nom']} ({p['unitat_astronomica']})")
print()
dades_planetes.update({'unitat_astronomica': 267112.92}, Query().nom == 'proxima b')
for p in dades_planetes:
 print(f"{p.doc_id} {p['nom']} ({p['unitat_astronomica']})")
print()
dades_planetes.close()

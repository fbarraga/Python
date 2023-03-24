from tinydb import TinyDB, Query

dades_cotxes = TinyDB('cbdd.json')
llista_cotxes = []
for c in dades_cotxes:
    llista_cotxes.append(f"{c['any']} {c['marca']} {c['model']}")
for e in sorted(llista_cotxes):
 print(e)
dades_cotxes.close()
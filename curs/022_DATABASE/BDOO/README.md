# Bases de dades Orientades a Objectes

## Introducció

En una **base de dades orientada a objectes** (Object Database Management System, ODBMS), la informació es representa mitjançant objectes com els presents en la programació orientada a objectes.
NoSQL és una àmplia classe de sistemes de gestió de bases de dades que difereixen de el model clàssic de SGBDR (Sistema de Gestió de Bases de Dades Relacionals) en aspectes importants, sent el més destacat que no fan servir SQL com a llenguatge principal de consultes.

[TinyDB](https://tinydb.readthedocs.io/en/latest/index.html) és una base de dades lleugera orientada a documents, tipus NoSQL, dissenyada per a ser simple, fàcil d'usar i amb una API senzilla. Amb una alta capacitat per estendre les seves  funcionalitats i no necessita un servidor extern.

Pots consultar tota la informació de TinyDB en els següents links:
* [pypi](https://pypi.org/project/tinydb/)
* [github](https://github.com/msiemens/tinydb)
* [readthedocs](https://tinydb.readthedocs.io/en/latest/)

## Instal·lació de TinyDB

Per treball amb TinyDB haurem d'instal·lar el mòdul a través del pip

```python
pip install tinydb
```

## Exemple de funcionament de TinyDB

``` python
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
bdd_persones.close(
```

## Mostrar les dades
```python
from tinydb import TinyDB, Query
bdd_persones = TinyDB('bddp.json')
for p in bdd_persones:
 print(f"{p['cognoms']}, {p['nom']}")
bdd_persones.close()
```


***
[Index](../../../README.md)

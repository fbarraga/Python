# Tipus de dades conjunts: set, frozenset

## set

 Els conjunts (`set`): em permeten guardar conjunts (desordenats) de dades (als que es pot calcular una funció de hash), en el que no existeixen repeticions. Es un tipus de dades mutable.

 Normalment s'utilitzen per comprovar si existeix un element en el conjunt, eliminar duplicats i càlculs matemàtics, com la intersecció, unió, diferència,...

### Definició de set. Constructor set

Podem definir un tipus `set` de diferentes formes:

	>>> set1 = set()
	>>> set1
	set()
	>>> set2=set([1,1,2,2,3,3])
	>>> set2
	{1, 2, 3}
	>>> set3={1,2,3}
	>>> set3
	{1, 2, 3}

## Frozenset

El tipus `frozenset` es un tipus inmutable de conjunts.

### Definició de frozenset. Constructor frozenset

	>>> fs1=frozenset()
	>>> fs1
	frozenset()
	>>> fs2=frozenset([1,1,2,2,3,3])
	>>> fs2
	frozenset({1, 2, 3})


## Operacions bàsiques amb set i frozenset

De les operacions que vam estudiar en l'apartat "Tipo de dades seqüència" els conjuns només accepten les següents:

* Recorregut
* Operadores de pertanyença: `in` i `not in`.

Entre les funcions definides podem utilitzar: `len`, `max`, `min`, `sorted`.

## Els set son mutables, los frozenset son inmutables

	>>> set1={1,2,3}
	>>> set1.add(4)
	>>> set1
	{1, 2, 3, 4}
	>>> set1.remove(2)
	>>> set1
	{1, 3, 4}

El tipus `frozenset` es inmutable per lo tanto no poseeix els mètodos `add` i `remove`.

## Mètodes de set i frozenset

	set1.add                          set1.issubset
	set1.clear                        set1.issuperset
	set1.copy                         set1.pop
	set1.difference                   set1.remove
	set1.difference_update            set1.symmetric_difference
	set1.discard                      set1.symmetric_difference_update
	set1.intersection                 set1.union
	set1.intersection_update          set1.update
	set1.isdisjoint     
	
Veiem alguns mètodes, partint sempre d'aquests dos conjunts:

	>>> set1={1,2,3}
	>>> set2={2,3,4}
	
	>>> set1.difference(set2)
	{1}
	>>> set1.difference_update(set2)
	>>> set1
	{1}

	>>> set1.symmetric_difference(set2)
	{1, 4}
	>>> set1.symmetric_difference_update(set2)
	>>> set1
	{1, 4}

	>>> set1.intersection(set2)
	{2, 3}
	>>> set1.intersection_update(set2)
	>>> set1
	{2, 3}

	>>> set1.union(set2)
	{1, 2, 3, 4}
	>>> set1.update(set2)
	>>> set1
	{1, 2, 3, 4}

Veiem els mètodes d'afegir i eliminar elements:

	>>> set1 = set()
	>>> set1.add(1)
	>>> set1.add(2)
	>>> set1
	{1, 2}
	>>> set1.discard(3)
	>>> set1.remove(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 3
	>>> set1.pop()
	1
	>>> set1
	{2}

i els mètodes de comprovació:

	>>> set1 = {1,2,3}
	>>> set2 = {1,2,3,4}
	>>> set1.isdisjoint(set2)	
	False
	>>> set1.issubset(set2)
	True
	>>> set1.issuperset(set2)
	False
	>>> set2.issuperset(set1)
	True


Per últim els mètodes de `frozenset`:


	fset1.copy                  fset1.isdisjoint            fset1.symmetric_difference
	fset1.difference            fset1.issubset              fset1.union
	fset1.intersection          fset1.issuperset            


***
[Index](../../../README.md)










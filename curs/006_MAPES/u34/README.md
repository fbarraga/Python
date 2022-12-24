# Mètodes principals de diccionaris

	dict1.clear       dict1.get         dict1.pop         dict1.update      
	dict1.copy        dict1.items       dict1.popitem     dict1.values      
	dict1.fromkeys    dict1.keys        dict1.setdefault  

## Mètodes d'eliminació: clear

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict1.clear()
	>>> dict1
	{}

## Mètodes d'agregat i creació: copy, dict.fromkeys, update, setdefault

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict2 = dict1.copy()

	>>> dict.fromkeys(["one","two","three"])
	{'one': None, 'two': None, 'three': None}
	>>> dict.fromkeys(["one","two","three"],100)
	{'one': 100, 'two': 100, 'three': 100}

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict2 = {'four':4,'five':5}
	>>> dict1.update(dict2)
	>>> dict1
	{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict1.setdefault("four",4)
	4
	>>> dict1
	{'one': 1, 'two': 2, 'three': 3, 'four': 4}
	>>> dict1.setdefault("one",-1)
	1
	>>> dict1
	{'one': 1, 'two': 2, 'three': 3, 'four': 4}

## Mètodes de retorn: get, pop, popitem, items, keys, values	

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict1.get("one")
	1
	>>> dict1.get("four")
	>>> dict1.get("four","no existe")
	'no existe'

	>>> dict1.pop("one")
	1
	>>> dict1
	{'two': 2, 'three': 3}
	>>> dict1.pop("four")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'four'
	>>> dict1.pop("four","no existe")
	'no existe'

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict1.popitem()
	('one', 1)
	>>> dict1
	{'two': 2, 'three': 3}

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> dict1.items()
	dict_items([('one', 1), ('two', 2), ('three', 3)])

	>>> dict1.keys()
	dict_keys(['one', 'two', 'three'])

	
## El tipus de dades dictviews

Els tres darrers mètodes retornen un objecte de tipus `dictviews`.

Això retorna una vista dinàmica del diccionari, per exemple:

	>>> dict1 = dict(one=1, two=2, three=3)
	>>> i = dict1.items()
	>>> i
	dict_items([('one', 1), ('two', 2), ('three', 3)])
	>>> dict1["four"]=4
	>>> i
	dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

Sobre aquest tipus de dades podem utilitzar les següents funcions:

* `len()`: Retorna número d'elements de la vista.
* `iter()`: Ens retorna un iterador de les claus, valors o ambdos.
* `x in dictview`: Retorna True si x està en les claus o valors.

## Recorregut de diccionaris

Podem recorrer les claus:

	>>> for clave in dict1.keys():
	...    print(clave)
	one
	two
	three

Podem recorrer els valors:

	>>> for valor in dict1.values():
	...    print(valor) 
	1
	2
	3

O podem recorrer ambdos:

	>>> for clave,valor in dict1.items():
	...   print(clave,"->",valor)
	one -> 1
	two -> 2
	three -> 3

***
[Index](../../../README.md)

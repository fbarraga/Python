# Tipus de dades: iterador i generador

## Iterador

Un objecte iterable es aquell que pot retornar un iterador. Normalment ls coleccions que hem vist son iterables. Un iterador em permet recorrer els elementos de l'objecte iterable.

### Definició d'iterador. Constructor iter

	>>> iter1 = iter([1,2,3])
	>>> type(iter1)
	<class 'list_iterator'>
	>>> iter2 = iter("hola")
	>>> type(iter2)
	<class 'str_iterator'>

## Función next(), reversed()

Per recérrer el iterador, utilitzem la funció `next()`:

	>>> next(iter1)
	1
	>>> next(iter1)
	2
	>>> next(iter1)
	3
	>>> next(iter1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration

La funció `reversed()` retorna un iterador amb els elements invertits, des de l'últim al primer.

	>>> iter2 = reversed([1,2,3])
	>>> next(iter2)
	3
	>>> next(iter2)
	2
	>>> next(iter2)
	1
	>>> next(iter2)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration	

## El módul itertools

El módul [itertools](https://docs.python.org/3.11/library/itertools.html) conté diferents funcions que ens retornen iteradors.

Exemples:

`count()`: Retorna un iterador infinit.

	>>> from itertools import count
	>>> counter = count(start=13)
	>>> next(counter)
	13
	>>> next(counter)
	14

`cycle()`: Retorna una seqüència infinita.

	>>> from itertools import cycle
	>>> colors = cycle(['red', 'white', 'blue'])
	>>> next(colors)
	'red'
	>>> next(colors)
	'white'
	>>> next(colors)
	'blue'
	>>> next(colors)
	'red'

`islice()`: Retorna un iterador finit.

	>>> from itertools import islice
	>>> limited = islice(colors, 0, 4) 
	>>> for x in limited: 
	...   print(x) 
	white
	blue
	red
	white

## Generadors

Un generador es un tipus concret de iterador. Es una funció que permet obtenir els seus resultats pas a pas. Per exemple, fer una función que cada vegada que la cridem ens doni el próxim número par. Tenim dos maneras de crear generadores:

1. Realizar una funció que retorni els valores amb la paraula reservada `yield`. 
2. Utilitzant la sintaxis de les "list comprehension". Per exemple:

		>>> iter1 = (x for x in range(10) if x % 2==0)
		>>> next(iter1)
		0
		>>> next(iter1)
		2
		>>> next(iter1)
		4

***
[Index](../../../README.md)

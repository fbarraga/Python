# Mètodes principals de llistes

Quan creem una llista estem creant un objecte de la classe `list`, que té definit un conjunt de mètodes:

	llista.append   llista.copy     llista.extend   llista.insert   llista.remove   llista.sort
	llista.clear    llista.count    llista.index    llista.pop      llista.reverse

## Mètodes d'inserció: append, extend, insert

	>>> llista = [1,2,3]
	>>> llista.append(4)
	>>> llista
	[1, 2, 3, 4]

	>>> llista2 = [5,6]
	>>> llista.extend(lista2)
	>>> llista
	[1, 2, 3, 4, 5, 6]	

	>>> llista.insert(1,100)
	>>> llista
	[1, 100, 2, 3, 4, 5, 6]

## Mètodes d'eliminació: pop, remove

	>>> llista.pop()
	6
	>>> llista
	[1, 100, 2, 3, 4, 5]

	>>> llista.pop(1)
	100
	>>> llista
	[1, 2, 3, 4, 5]

	>>> llista.remove(3)
	>>> llista
	[1, 2, 4, 5]

## Mètodes d'ordenació: reverse, sort, 

	>>> llista.reverse()
	>>> llista
	[5, 4, 2, 1]

	>>> llista.sort()
	>>> llista
	[1, 2, 4, 5]

	>>> llista.sort(reverse=True)
	>>> llista
	[5, 4, 2, 1]

	>>> llista=["hola","que","tal","Hola","Que","Tal"]
	>>> llista.sort()
	>>> llista
	['Hola', 'Que', 'Tal', 'hola', 'que', 'tal']
	
	>>> llista=["hola","que","tal","Hola","Que","Tal"]
	>>> llista.sort(key=str.lower)
	>>> llista
	['hola', 'Hola', 'que', 'Que', 'tal', 'Tal']


## Mètodes de cerca: count, index

	>>> llista.count(5)
	1

	>>> llista.append(5)
	>>> llista
	[5, 4, 2, 1, 5]
	>>> llista.index(5)
	0
	>>> llista.index(5,1)
	4
	>>> llista.index(5,1,4)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: 5 is not in list

## Mètode de copia: copy

	>>> llista2 = llista1.copy()
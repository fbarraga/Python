# Mètodes principals de llistes

Quan creem una llista estem creant un objecte de la classe `list`, que té definit un conjunt de mètodes:

	llista.append   llista.copy     llista.extend   llista.insert   llista.remove   llista.sort
	llista.clear    llista.count    llista.index    llista.pop      llista.reverse

## Mètodes d'inserció: append, extend, insert

*Append*: Afegeix al final de la llista:

	>>> llista = [1,2,3]
	>>> llista.append(4)
	>>> llista
	[1, 2, 3, 4]

*Extend*: Esten la llista amb una nova llista

	>>> llista2 = [5,6]
	>>> llista.extend(lista2)
	>>> llista
	[1, 2, 3, 4, 5, 6]	

*Insert*: Inserta en una posició un valor

	>>> llista.insert(1,100)
	>>> llista
	[1, 100, 2, 3, 4, 5, 6]

## Mètodes d'eliminació: pop, remove

*Pop*: Elimina l'últim valor de la llista
	
	>>> llista.pop()
	6
	>>> llista
	[1, 100, 2, 3, 4, 5]

*Pop(n)*: Elimina el valor de la posició n

	>>> llista.pop(1)
	100
	>>> llista
	[1, 2, 3, 4, 5]

*Remove*: Elimina el valor de la llista

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

*index(n)*: retorna la primera posició on es troba el valor n
	>>> llista.index(5)
	0
*index(n,i): retorna la següent posició on es troba el valor n	
	>>> llista.index(5,1)
	4


## Mètode de copia: copy

	>>> llista2 = llista1.copy()


***
[Index](../../../README.md)

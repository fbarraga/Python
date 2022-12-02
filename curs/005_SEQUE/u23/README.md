# Operacions avançades amb seqüències

Les funcions que anem a estudiar en aquesta unitat ens apropen al paradigna de la programació funcional que tambén ens ofereix python. La programació funcional es un paradigma de programació declarativa basat en el ús de funcions matemàtiques, en contrast amb la programació imperativa, que enfatitza els canvis d'estat mitjançant la mutació de variables.

## Funció map

`map(funció,seqüència)`: Executa la funció enviada per paràmetre sobre cadascun dels elements de la seqüència.

*Exemple*

	>>> items = [1, 2, 3, 4, 5]
	>>> def sqr(x): return x ** 2
	>>> list(map(sqr, items))
	[1, 4, 9, 16, 25]

## Funció filter

`filter(funció,seqüència)`: Retorna una seqüència amb els elements de la seqüència envíada per paràmetre que retornen `True` al aplicar-li la funció envíada també como paràmetre.

*Exemple*

	>>> llista = [1,2,3,4,5]
	>>> def par(x): return x % 2==0 
	>>> list(filter(par,llista))

	[2,4]

## Funció reduce

`reduce(funció,seqüència)`: Retorna un únic valor que és el resultat d'aplicar la funció als elements de la seqüència.
	
*Exemple*

	>>> from functools import reduce
	>>> llista = [1,2,3,4,5]
	>>> def add(x,y): return x + y
	>>> reduce(add,llista)

	15

# list comprehension

`list comprehension` ens propociona una alternativa per la creació de llistes. Es semblant a la funció `map`, pero mentres `map` executa una funció per cada element de la seqüència, amb aquesta tècnica s'aplica una expressió.

*Exemple*

	>>> [x ** 3 for x in [1,2,3,4,5]]
	[1, 8, 27, 64, 125]

	>>> [x for x in range(10) if x % 2 == 0]
	[0, 2, 4, 6, 8] 

	>>> [x + y for x in [1,2,3] for y in [4,5,6]]
	[5, 6, 7, 6, 7, 8, 7, 8, 9]

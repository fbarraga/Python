# Tipus de dades seqüència: llistes

Les llistes (`list`) em permeen guadar un conjunt de dades que es poden repetir i que poden ser de distints tipus. Es un tipus mutable.

## Construcció d'una llista 

Per crear una llista puc utilitzar diferents mètodes:

* Amb els caràcters `[` y `]`:

		>>> llista1 = []
		>>> llista2 = ["a",1,True]

* Utilizant el constructor `list`, que pren com a parámetre una dada d'algún tipus de seqüència.

		>>> llista3 = list()
		>>> llista4 = list("hola")
		>>> llista4
		['h', 'o', 'l', 'a']

## Operacions bàsiques amb llistes

Com veiem en el apartado "Tipo de datos secuencia" podemos realizar las siguientes operaciones:

* Les seqüències es poden recórrer.
* Operadors de pertanyença: `in` i `not in`.
* Concatenació: `+` 
* Repetició: `*`
* Indexació: Cada element té un índex, comencem a comptar pel element en el índex 0. Si intentem accedir a un índex que correspogui a un element que no existeix obtenim una excepció `IndexError`.

		>>> llista1[6]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module
		IndexError: list index out of range	

	Es poden utilitzar índexs negatius:

		>>> lista[-1]
		6

* Slice: S'utilitza de la següent manera

	* `llista[start:end]` 	  # Elements des de la posició start fins end-1
	* `llista[start:]`    	  # Elements desde la posició start fins el final
	* `llista[:end]`      	  # Elements des de el principio fins la posició end-1
	* `llista[:]` 		 	  # Tots els elements
	* `llista[start:end:step]` # Igual que l'anterior pero donant step salts.
 		
 	Es poden utilitzar també indexs negatius, per exemple: `llista[::-1]`

## Funcions predefinides que treballin amb llistes

	>>> llista1 = [20,40,10,40,50]
	>>> len(llista1)
	5
	>>> max(llista1)
	50
	>>> min(llista1)
	10
	>>> sum(llista1)
	150
	>>> sorted(llista1)
	[10, 20, 30, 40, 50]
	>>> sorted(llista1,reverse=True)
	[50, 40, 30, 20, 10]

Veiem  la funció `enumerate` amb més detall: rep una seqüència i retorna un objecte enumerat amb tuples:

	>>> seasons = ['Primavera', 'Estiu', 'Tardor', 'Hivern']
	>>> list(enumerate(seasons))
	[(0, 'Primavera'), (1, 'Estiu'), (2, 'Tardor'), (3, 'Hivern')]
	>>> list(enumerate(seasons, start=1))
	[(1, 'Primavera'), (2, 'Estiu'), (3, 'Tardor'), (4, 'Hivern')]


## Les llistes son mutables

Com hem indicat anteriorment les llistes es un tipus de dades mutable. Això té per nosaltres varies conseqüències, per exemple podem obtenir resultats com els que es mostren a continuació:

	>>> llista1 = [1,2,3]
	>>> llista1[2]=4
	>>> llista1
	[1, 2, 4]
	>>> del llista1[2]
	>>> llista1
	[1, 2]


	>>> llista1 = [1,2,3]
	>>> llista2 = lista1
	>>> llista1[1] = 10
	>>> llista2
	[1, 10, 3]

### ¿Com es copien les llistes?

Si volem copiar una llista en una altra podem fer-ho de moltes maneres:

	>>> llista1 = [1,2,3]
	>>> llista2=llista1[:]
	>>> llista1[1] = 10
	>>> llista2
	[1, 2, 3]

	>>> llista2 = llist(llista1)	

	>>> llista2 = llista1.copy()

## Llistes multidimensionals

A la hora de definir les llistes hem indicat que podem guardar en elles dades de qualsevol tipus, i evidentement podem guardar llistes dintre de llistes. 

	>>> taula = [[1,2,3],[4,5,6],[7,8,9]]
	>>> taula[1][1]
	5

	>>> for fila in taula:
	...   for elem in fila:
	...      print(elem,end="")
	...   print()
	 
	123
	456
	789

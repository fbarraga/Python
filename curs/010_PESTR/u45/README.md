# Introducció a las funcions

## Introducció a la programació estructurada i modular

La programació és un paradigma de programació orientat a millorar la claredat, qualitat i temps de desenvolupament d'un programa d'ordinador, utilitzant únicament subrutines (funcions o procediments) i tres estructures: seqüència, alternatives i repetitives. 

La programació modular és un paradigma de programació que consisteix a dividir un programa en mòduls o subprogrames per tal de fer-lo més llegible i manejable.

En aplicar la programació modular, un problema complex ha de ser dividit en diversos subproblemes més simples, i aquests al seu torn en altres subproblemes més simples. Això s'ha de fer fins a obtenir subproblemes prou simples com per poder ser resolts fàcilment amb algun llenguatge de programació (divideix i venceràs).

La programació estructural i modular es duu a terme en python3 amb la definició de funcions.


## Definició de funcions

Veiem un exemple de definició de funció:

	>>> def factorial(n):
	...   """Calcula el factorial de un número"""
	...   resultado = 1
	...   for i in range(1,n+1):
	...     resultado*=i
	...   return resultado

Podem obtenir informació de la funció:

	>>> help(factorial)
	Help on function factorial in module __main__:
	factorial(n)
    	Calcula el factorial de un número

i per utilitzar la funció:

	>>> factorial(5)
	120

## Àmbit de variables. Sentència global

Una variable local es declara en el seu àmbit d'ús (en el programa principal i dins d'una funció) i una global fora del seu àmbit perquè es pugui utilitzar en qualsevol funció que la declari com a global.

	>>> def operar(a,b):
	...    global suma
	...    suma = a + b
	...    resta = a - b
	...    print(suma,resta)
	... 
	>>> operar(4,5)
	9 -1
	>>> resta
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'resta' is not defined
	>>> suma
	9

Podem definir variables globals, que serán visibles en tot el mòdul. Es recomana declarar-les en majúscules:

	>>> PI = 3.1415
	>>> def area(radio):
	...    return PI*radio**2
	... 
	>>> area(2)
	12.566


## Paràmetros formals i realss

* Paràmetres formals: Són les variables que rep la funció, es creen en definir la funció. El seu contingut el rep en realitzar la crida a la funció dels paràmetre reals. Els paràmetres formals són variables locals dins de la funció.

* Paràmetres reals: Són les expressions que s' utilitzen en la trucada de la funció, els seus valors es copiaran en els paràmetres formals.


## Pas de paràmetre per valor o per referència

A Python el pas de paràmetres és sempre per referència. El llenguatge no treballa amb el concepte de variables sinó objectes i referències. En realitzar l'assignació a = 1 no es diu que "a conté el valor 1" sinó que "a referència a 1". Així, en comparació amb altres llenguatges, es podria dir que a Python els paràmetres sempre es passen per referència.

Evidentment si es passa un valor d' un objecte immutable, el seu valor no es podrà canviar dins la funció:


	>>> def f(a):
	...     a=5
	>>> a=1
	>>> f(a)
	>>> a
	1

No obstant si passem un objecte d'un tipus mutable, si podrem canviar el seu valor:

	>>> def f(lista):
	...   lista.append(5)
	... 
	>>> l = [1,2]
	>>> f(l)
	>>> l
	[1, 2, 5]

Tot i que podem canviar el paràmetre real quan els objectes passats són de tipus mutables, no és recomanable fer-ho a Python. En altres llenguatges és necessari perquè no tenim opció de retornar múltiples valors, però com veurem a Python podem tornar tuplas o llista amb la instrucció 'return'.

## Crides a una funció

Quan es crida a una funció s' han d' indicar els paràmetres reals que s' han de passar. La crida a una funció es pot considerar una expressió el valor i el tipus de la qual és el retornat per la funció. Si la funció no té una instrucció 'return' el tipus de l'anomenada sera 'None'.


	>>> def cuadrado(n):
	...   return n*n
	
	>>> a=cuadrado(2)
	>>> cuadrado(3)+1
	10
	>>> cuadrado(cuadrado(4))
	256
	>>> type(cuadrado(2))
	<class 'int'>

Quan estem definint una funció estem creant un objecte de tipus `function`.

	>>> type(cuadrado)
	<class 'function'>

I per lo tant pot guardar el objecte funció en una alra variable:

	>>> c=cuadrado
	>>> c(4)
	16

***
[Index](../../../README.md)

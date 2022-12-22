# Treballant amb variables

Com hem indicat anteriorment les variables en Python no es declaren, es determina el seu tipus en temps d'execució empleant una tècnica que s'anomena **tipat dinàmic**.

## ¿Qué es el tipat dinàmic?

A python quan assignem una variable, es crea una referencia (punter) al objecte creat, en aquest moment es determina el tipus de la variable. Per lo tant cada vegada que assignem de nou la variable pot canviar el tipus en temps d'execució.

	>>> var = 3
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>


## Objectes inmutables i mutables

### Objectes inmutables

Python procura no consumir més memoria de la necesaria. Certs objectes son **inmutables**, es a dir, no poden modificar el seu valor. El número 2 es sempre el número 2. És un objecte inmutable. Python procura emmagatzemar en memoria una sola vegada cada valor inmutable. Si dos o més variables contenen aquest valor, les seves referències apunten a la mateixa zona de memòria.

**Exemple**

Per comprovar això, anem a utilitzar la funció `id`, que ens retorna l'identificador de la variable o el objecte en memòria.

Veiem el següent codi:

	>>> a = 5

Podem comprovar que `a` fa referencia al objecte `5`.
	
	>>> id(5)
	10771648
	>>> id(a)
	10771648

Això és molt diferent a altres llenguatges de programació, on una variable ocupa un espai de memoria on es guarda un valor. Des d'aquest punt quan assignem un altre número a la variable esic canviant la referència.

	>>> a = 6
	>>> id(6)
	10771680
	>>> id(a)
	10771680

Les cadenes també son un objecte **inmutable**, que ho siguin té efectes sobre les operacions que podem fer sobre elles. L'assignació a un element d'una cadena, per exemple està prohibida.

	>>> a = "Hola"
	>>> a[0]="h"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

Dels tipus de dades principals, s'ha de recordar que son inmutables els números, les cadenes o les tuples.

### Objectes mutables

El cas contrari el tenim per exemple en els objectes tipus llistes, en aquest cas les llistes son mutables. Es pot modificar un element de la llista:

**Exemple**

	>>> a = [1,2]
	>>> b = a
	>>> id(a)
	140052934508488
	>>> id(b)
	140052934508488

Com anteriorment veiem que dos variables fan referencia a la misma llista i memòria. Pero aquí ve la diferència, al poder ser modificada podem trobar situacions com la següent:

	>>> a[0] = 5
	>>> b
	[5, 2]

Quan estudiem les llistes abordarem aquest tema de manera completa.
Dels tipus de dades principals, s'ha de recordar que son mutables les llistes i els diccionaris.

## Operadors de identitat

Per provar això de una altra manera podem utilitzar els operadors d'identitat:

* `is`: Retorna True si dos variables o objectes están referenciant la darrera posició de memòria. En caso contrari retorna False.
* `is not`: Retorna True si dos variables u objectes **no** están referenciant la mateixa posició de memoria. En cas contrari retorna False.

**Exemple**

	>>> a = 5
	>>> b = a
	>>> a is b
	True
	>>> b = b +1
	>>> a is b
	False
	>>> b is 6
	True

	
## Operadors d'assignació

Em permet assignar una valor a una variable, o dit d'una altra manera em permet canviar la referència a un nou objecte.

L'operador principal és `=`:

	>>> a = 7
	>>> a
	7

Podem fer diferents operacions amb la variable i després assignar, per exemple sumar i després assignar.

	>>> a+=2
	>>> a
	9

Altres operadors d'assignació: `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

## Assignació múltiple

En python es permeten assignacions múltiples d'aquesta:

	>>> a, b, c = 1, 2, "hola"

***
[Index](../../../README.md)

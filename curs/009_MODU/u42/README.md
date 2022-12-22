# Mòduls estàndards: mòduls matemàtics

## Mòdul math

El mòdul [math](https://docs.python.org/3.11/library/math.html) ens proporciona varies funcions i operacions matemàtiques.

	>>> import math
	>>> math.factorial(5)
	120
	>>> math.pow(2,3)
	8.0
	>>> math.sqrt(7)
	2.6457513110645907
	>>> math.cos(1)
	0.5403023058681398
	>>> math.pi
	3.141592653589793
	>>> math.log(10)
	2.302585092994046

## Mòdul fraccions

El mòdul [fractions](https://docs.python.org/3.11/library/fractions.html) ens permet treballar amb fraccions.

	>>> from fractions import Fraction
	>>> a=Fraction(2,3)
	>>> b=Fraction(1.5)
	>>> b
	Fraction(3, 2)
	>>> c=a+b
	>>> c
	Fraction(13, 6)

## Mòdul statistics

El mòdul [statistics](https://docs.python.org/3.11/library/statistics.html) ens proporciona funcions per fer operacions estadístiques.

	>>> import statistics
	>>> statistics.mean([1,4,5,2,6])
	3.6

	>>> statistics.median([1,4,5,2,6])
	4

## Módulo random

El mòdul [random](https://docs.python.org/3.11/library/random.html) ens permet generar dades pseudo-aleatoris.

	>>> import random
	>>> random.randint(10,100)
	34
	
	>>> random.choice(["hola","que","tal"])
	'que'
	
	>>> frutas=["manzanas","platanos","naranjas"]
	>>> random.shuffle(frutas)
	>>> frutas
	['naranjas', 'manzanas', 'platanos']

	>>> lista = [1,3,5,2,7,4,9]
	>>> numeros=random.sample(lista,3)
	>>> numeros
	[1, 2, 4]

	
***
[Index](../../../README.md)




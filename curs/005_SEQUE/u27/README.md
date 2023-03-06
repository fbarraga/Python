# Tipus de dades cadenes de caràcters

* Les cadenes de caràcters (`str`): permeten guardar seqüències de caràcters. És un tipus inmutable. Com hem comentat les cadenes de caràcters en Python3 està codificada amb Unicode.

## Definició de cadenes. Constructor str

Podem definir una cadena de caràcters de diferents maneres:

	>>> cad1 = "Hola"
	>>> cad2 = '¿Qué tal?'
	>>> cad3 = '''Hola,
		que tal?'''

També podem crear cadenes amb el constructor `str` a partir de altres tipus de dades.

	>>> cad1=str(1)
	>>> cad2=str(2.45)
	>>> cad3=str([1,2,3])

## Operacions bàsiques amb cadenes de caràcters

Com veiem en l'apartat "Tipus de dades seqüència" podemos realitzar les següents operacions:

* Les cadenes s poden recórrer.
* Operadors de pertanyença: `in` i `not in`.
* Concatenació: `+` 
* Repetició: `*`
* Indexació
* Slice

Entre les funcions definides podem utilitzar: `len`, `max`, `min`, `sorted`.

## Les cadenes son inmutables

	>>> cad = "Hola que tal?"
	>>> cad[4]="."
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

## Comparació de cadenes

Les cadenes es comparen caràcter a caràcter, en el moment en que dos caràcters no són iguals es compara alfabèticament (és a dir, es converteix a codi unicode i es comparen). 

*Exemples*

	>>> "a">"A"
	True
	>>> ord("a")
	97
	>>> ord("A")
	65

	>>> "informatica">"informacio"
	True

	>>> "abcde">"abcdef"
	False

## Funcions repr, ascii, bin

* `repr(objecte)`: Retorna una cadena de caràcters que representa la informació d'un objecte.

		>>> repr(range(10))
		'range(0, 10)'
		>>> repr("piña")
		"'piña'"

	La cadena retornada per `repr()` hauria de ser aquella que, passada a `eval()`, retorna el mateix objecte.

		>>> type(eval(repr(range(10))))
		<class 'range'>

* `ascii(objecte)`: Retorna també la representació en cadena d'un objecte però en aquest cas mostra els caràcters amb un codi d'escape \. Per exemple en ascii (Latin1) la `á` es representa con `\xe1`.

		>>> ascii("á")
		"'\\xe1'"
		>>> ascii("piña")
		"'pi\\xf1a'"

* `bin(numero)`: retorna una cadena de caràcters que correspon a la representació binaria del número rebut.

		>>> bin(213)
		'0b11010101'	
		
***
[Index](../../../README.md)

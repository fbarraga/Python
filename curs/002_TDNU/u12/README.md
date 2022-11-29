# Tipus de dades numèriques

Python3 treballa amb tres tipus numèrics:

* Enters (int): Representen tots els números enters( positius, negatius i zero), sense part decimal. A Python3 aquest tipus no te limitació d'espai. 
* Reals (float): Serveix per representar els números reals, tenen una parte decimal i una altra decimal. Normalment s'utilitza per la seva implementació un tipus `double` de C. 
* Complexes (complex): serveixen per representar números complexes, amb una parte real i altra imaginaria.

Els tipus de dades numèrics  son tipus de dades inmutables.

*Exemples*

	>>> entero = 7
	>>> type(entero)
	<class 'int'>
	>>> real = 7.2
	>>> type (real)
	<class 'float'
	>>> complejo = 1+2j
	>>> type(complejo)
	<class 'complex'>

## Operadors aritmètics

* `+`: Suma dos números
* `-`: Resta dos números
* `*`: Multiplica dos números
* `/`: Divideix dos números, el resultat és `float`.
* `//`: Divisió entera
* `%`: Mòdul o reste de la divisió
* `**`: Potència
* `+`, `-`: Operadors unaris positiu i negatiu

## Funcions predefinides que treballen amb números:

* `abs(x)`: Retorna al valor absolut d'un número.
* `divmod(x,y)`: Pren como paràmetre dos números, i retorna una tupla amb dos valors, la divisió entera, i el mòdul o reste de la divisió.
* `hex(x)`: Retorna una cadena amb la representació hexadecimal del número que rep com a paràmetre.
* `oct(x)`: Retorna una cadena amb la representació octal del número que rep com a paràmetre.
* `bin(x)`: Retorna una cadena amb la representació binaria del número que rep com a paràmetre.
* `pow(x,y)`: Retorna la potència de la base x elevat al exponent y. Es similar a l'operador `**`.
* `round(x,[y])`: Retorna un número real (float) que es el redondeig del número rebut com paràmetre, podems indicar un paràmetro opcional que indica el número de decimals en el redondeig.

*Exemples*

	>>> abs(-7)
	7
	>>> divmod(7,2)
	(3, 1)
	>>> hex(255)
	'0xff'
	>>> oct(255)
	'0o377'
	>>> pow(2,3)
	8
	>>> round(7.567,1)
	7.6


## Operadors a nivell de bit

* `x | y`: x OR y	
* `x ^ y`: x XOR y 	 
* `x & y`: a AND y 	 
* `x << n`: Desplaçament a l'esquerra **n** bits.
* `x >> n`: Desplaçament a la dreta **n** bits.
* `~x`: Retorna els bits invertits.

## Conversió de tipus

* `int(x)`: Converteix el valor a enter.
* `float(x)`: Converteix el valor a float.
* `complex(x)`: Converteix el valor a un complex sense part imaginaria.
* `complex(x,y)`: Converteix el valor a un complex, la parte real de la qual es x i la part imaginaria y.

Els valors que es reben també poden ser cadenes de caràcters (str).

*Exemples*

	>>> a=int(7.2)
	>>> a
	7
	>>> type(a)
	<class 'int'>
	>>> a=int("345")
	>>> a
	345
	>>> type(a)
	<class 'int'>
	>>> b=float(1)
	>>> b
	1.0
	>>> type(b)
	<class 'float'>
	>>> b=float("1.234")
	>>> b
	1.234
	>>> type(b)
	<class 'float'>

Si volem convertir una cadena a enter, la cadena ha d'estar formada per caràcters numèrics, sino ens retornarà un error:

*Exemples*

	a=int("123.3")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '123.3'

***
[Index](../../../README.md)

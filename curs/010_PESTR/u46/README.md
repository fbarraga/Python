# Conceptes avançats sobre funcions

## Tipus d'arguments: posicionals o keyword

Tenim dos tipus de paràmetres: **els posicionals** on el paràmetre real ha de  coincidir en posició amb el paràmetre formal:

	>>> def sumar(n1,n2):
	...   return n1+n2
	... 
	>>> sumar(5,7)
	12
	>>> sumar(4)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: sumar() missing 1 required positional argument: 'n2'

A més podem tenir paràmetres amb valors per defecte:

	>>> def operar(n1,n2,operador='+',respuesta='El resultado es '):
	...   if operador=="+":
	...     return respuesta+str(n1+n2)
	...   elif operador=="-":
	...     return respuesta+str(n1-n2)
	...   else:
	...     return "Error"
	... 
	>>> operar(5,7)
	'El resultado es 12'
	>>> operar(5,7,"-")
	'El resultado es -2'
	>>> operar(5,7,"-","La resta es ")
	'La resta es -2'


Els paràmetres **keyword** son aquells on s'indican el nom del paràmetre formal i el seu valor, per lo tant no es necesari que tinguin la mateixa posició. Al definir una funció o al cridar-la, s'ha d'indicar primer els arguments posicionals i a continuació els arguments amb valor per defecte (keyword). 

	>>> operar(5,7)	# dos parámetros posicionales
	>>> operar(n1=4,n2=6)	# dos parámetros keyword
	>>> operar(4,6,respuesta="La suma es")	# dos parámetros posicionales y uno keyword
	>>> operar(4,6,respuesta="La resta es",operador="-")	# dos parámetros posicionales y dos keyword

## Paràmetre *

Un paràmetre `*` entre els paràmetres formals d'una funció, ens obliga a indicar els paràmetres reals posteriors amb **keyword**:

	>>> def sumar(n1,n2,*,op="+"):
	...   if op=="+":
	...     return n1+n2
	...   elif op=="-":
	...     return n1-n2
	...   else:
	...     return "error"
	... 
	>>> sumar(2,3)
	5
	>>> sumar(2,3,"-")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: sumar() takes 2 positional arguments but 3 were given
	>>> sumar(2,3,op="-")
	-1


## Arguments arbitraris (\*args y \*\*kwargs)

Per indicar un número indefinit d'arguments posicionals al definir una funció, utilitzem el símbol `*`:

	>>> def sumar(n,*args):
	...   resultado=n
	...   for i in args:
	...     resultado+=i
	...   return resultado
	... 
	>>> sumar(2)
	2
	>>> sumar(2,3,4)
	9

Per indicar un número indefinit d'arguments keyword al definir una funció,  utilitzem el símbol `**`:

	>>> def saludar(nombre="pepe",**kwargs):
	...   cadena=nombre
	...   for valor in kwargs.values():
	...    cadena=cadena+" "+valor
	...   return "Hola "+cadena
	... 
	>>> saludar()
	'Hola pepe'
	>>> saludar("juan")
	'Hola juan'
	>>> saludar(nombre="juan",nombre2="pepe")
	'Hola juan pepe'
	>>> saludar(nombre="juan",nombre2="pepe",nombre3="maria")
	'Hola juan maria pepe'

Per lo tant podríem tenir definicions de funcions del tipus:

	>>> def f()
	>>> def f(a,b=1)
	>>> def f(a,*args,b=1)
	>>> def f(*args,b=1)
	>>> def f(*args,b=1,*kwargs)
	>>> def f(*args,*kwargs)
	>>> def f(*args)
	>>> def f(*kwargs)

## Desempaquetar arguments: passar llistes i diccionaris

En caso contrari es quan hem de passar paràmetres que ho tenim guardat en una llista o en diccionari.

Per passar llistes utilitzem el símbol `*`:

	>>> lista=[1,2,3]
	>>> sumar(*lista)
	6
	>>> sumar(2,*lista)
	8
	>>> sumar(2,3,*lista)
	11

Podem tenir paràmetres keyword guardats en un diccionari, per enviar un diccionari utilitzem el símbol `**`:

	>>> datos={"nombre":"jose","nombre2":"pepe","nombre3":"maria"}
	>>> saludar(**datos)
	'Hola jose maria pepe'

## Retornar múltiples resultats

La instrucció `return` pot retornar qualsevol tipus de resultats, per lo tant es fàcil retornar múltiples dades guardades en una llista o en un diccionari. Veiem un exemple en que retornem les dades en una tupla:

	>>> def operar(n1,n2):
	...   return (n1+n2,n1-n2,n1*n2)	

	>>> suma,resta,producto = operar(5,2)
	>>> suma
	7
	>>> resta
	3
	>>> producto
	10

***
[Index](../../../README.md)<right>[Tipus Especials de funcions](../u47/README.MD)</right>

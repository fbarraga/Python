# Excepcions

## Errors sintàctics i errors d'execució

Veim com és un exemple d'error sintàctic:

	>>> while True print('Hello world')
	  File "<stdin>", line 1
	    while True print('Hello world')
	                   ^
	SyntaxError: invalid syntax

Una excepció o un error de execució es produeix durant l'execució del programa. Les excepcions es poden gestionar perque no termini el programa. Veiem alguns exemples d'excepcions:

	>>> 4/0
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero	

	>>> a+4
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined	

	>>> "2"+2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: Can't convert 'int' object to str implicitly

Hem obtingut varies excpcions: *ZeroDivisionError*, *NameError* i *TypeError*. Pots consultar la [llista de excepcions](https://docs.python.org/3.4/library/exceptions.html#bltin-exceptions) i el seu significat.

## Gestionant excepcions. try, except, else, finally

Veiem un exemple simple de com podem tractar una excepció:

	>>> while True:
	...   try:
	...     x = int(input("Introdueix un número:"))
	...     break
	...   except ValueError:
	...     print ("Has d'introduir un número")

1. S'executa el bloc d'instruccions de `try`.
2. Si no es produeix l'excepció, el bloc de `except` no s'executa i continúa l'execució seqüència.
3. Si es produeix una excepció, la resta del bloc `try` no s'executa, si l'excepció que s'ha produit correspon amb la indicada en `except` salta a executar el bloc d'instruccions `except`.
4. Si l'excepció produïda no es correspon amb les indicades en `except` es passa a una altra instrucció `try`, si finalment no hi ha un gestionador ens donarà error i el programa acabarà.

Un bloc `except` pot gestionar varis tipus d'excepcions:

	... except (RuntimeError, TypeError, NameError):
	...     pass

Si vull controlar varis tipus d'excepcions puc posar varis blocs  `except`. Tenint en compte que en el darrer, si vull no indico el tipus d'excepció:

	>>> try:
	...   print (10/int(cad))
	... except ValueError:
	...   print("No es pot convertir a enter")
	... except ZeroDivisionError:
	...   print("No es puede dividir per zero")
	... except:
	...   print("Qualsevol altre error")

Es pot utilitzar també la clàusula `else`:

	>>> try:
	...   print (10/int(cad))
	... except ValueError:
	...   print("No es pot convertir a enter")
	... except ZeroDivisionError:
	...   print("No es pot dividirr per zero")
	... else:
	...   print("Qualsevol altre error")

Per últim indicar que podem indicar una clàusula `finally` per indicar un bloc d'instruccions que sempre s'haurà d'executar, independentment de que l'excepció s'hagi produit o no.

	>>> try:
	...     result = x / y
	... except ZeroDivisionError:
	...     print("Divisió per zero!")
	... else:
	...     print("El resultat es", result)
	... finally:
	...     print("Acabem el programa")


## Obtenint informació de les excepcions

	>>> cad = "a"
	>>> try:
	...   i = int(cad)
	... except ValueError as error:
	...   print(type(error))
	...   print(error.args)
	...   print(error)
	... 
	<class 'ValueError'>
	("invalid literal for int() with base 10: 'a'",)
	invalid literal for int() with base 10: 'a'

## Propagant excepcions. raise

Si construim una funció on es gestioni una excepció podem fer que l'excepció s'envii a la funció des d'on l'hem cridat. Per fer-ho utilizarem la instrucció `raise`. Veiem alguns exemples:

	def dividir(x,y):
		try:
			return x/y
		except ZeroDivisionError:
			raise 

Amb `raise` També podem propagar una excepció en concret:

	def nivel(numero):
		if numero<0:
			raise ValueError("El número ha de ser positiu:"+str(numero))
		else:
			return numero

# Conceptes avançats de programació orientada a objectes I

## Atributs de classe (estàtics)

A Python, les variables definides dintre d'una classe, però no dintre d'un mètode, son anomenades variables estàtiques o de classe. Aquestes variables son compartidas per tots els
objectes de la clase.

Per accedir a una variable de classe podem fer-ho escrivint el nom de la classe o mitjançant self.

	>>> class Alumno():
	...    contador=0
	...    def __init__(self,nombre=""):
	...       self.nombre=nombre
	...       Alumno.contador+=1
	... 
	>>> a1=Alumno("jose")
	>>> a1.contador
	1
	>>> Alumno.contador
	1

Utilitzem les variables estàtiques (o de classe) pels atributs que son comuns a tots els atributs de la classe. Els atributs dels objectes es defineixen en el constructor.

## Atributs privados i ocultos

Les variables que comencen per un guió baix `_` son considerades privades. El seu nom indica a altres programadors que no son públiques: son un detall d'implementació del que no es pot dependre — entre altres coses perque podríen desapareixer en qualsevol moment. **Però res ens impideix accedir a aquestes variables.**

	>>> class Alumno():
	...    def __init__(self,nombre=""):
	...       self.nombre=nombre
	...       self._secreto="asdasd"
	... 
	>>> a1=Alumno("jose")
	>>> a1.nombre
	'jose'
	>>> a1._secreto
	'asdasd'

Dos guions baixo al començament del nom `__` porten l'ocultament un pas enllà, "enmaranyant" (name-mangling ) la variable de manera que sigui més difícil veure-la des de fora.

	>>> class Alumno():
	...    def __init__(self,nombre=""):
	...       self.nombre=nombre
	...       self.__secreto="asdasd"
	... 
	>>> a1=Alumno("jose")
	>>> a1.__secreto
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Alumno' object has no attribute '__secreto'

Pero en realidad sigue siendo posible acceder a la variable.

	>>> a1._Alumno__secreto
	'asdasd'

Es solen utilitzar quan d'una subclasse defineix un atribut amb el mateix nom que la classe mare, per que no coincideixin els noms.


## Mètodes de classe (estàtics)

Els mètodes estàtics (static methods) son aquells que no necesiten accès a cap atribut de cap objecte en concret de la classe.

	>>> class Calculadora():
	...   def __init__(self,nombre):
	...     self.nombre=nombre
	...   def modelo(self):
	...     return self.nombre
	...   @staticmethod
	...   def sumar(x,y):
	...     return x+y
	... 
	>>> a=Calculadora("basica")
	>>> a.modelo()
	'basica'
	>>> a.sumar(3,4)
	7
	>>> Calculadora.sumar(3,4)
	7

Res ens impedeix moure aquest mètode a una funció fora de la classe, ja que no fa ús de cap atribut de cap objeto, però la deixem dintre perque la seva lògica (fer sumes) pertany conceptualment a Calculadora.

Ho podem cridar des de l'objecte o des de la classe.

## Funcions getattr,setattr,delattr,hasattr

	>>> a1=Alumno("jose")
	>>> getattr(a1,"nombre")
	'jose'
	>>> getattr(a1,"edad","no tiene")
	'no tiene'

	>>> setattr(a1,"nombre","pepe")
	>>> a1.nombre
	'pepe'

	>>> hasattr(a1,"nombre")
	True

	>>> delattr(a1,"nombre")

# Conceptes avançats de programació orientada a objectes II


## Propietats: getters, setters, deleter

Per implementar l'encapsulació i no permetre l'accés directe als atributs, podem posar els atributs ocults i declarar mètodes específics per accedir i modificar els atributs (mutadors). Aquests mètodes es denominen getters i setters.

	class circulo():
		def __init__(self,radio):
			self.set_radio(radio)
		def set_radio(self,radio):
			if radio>=0:
				self._radio = radio
			else:
				raise ValueError("Radio positivo")
				self._radio=0
		def get_radio(self):
			print("Estoy dando el radio")
			return self._radio

	>>> c1=circulo(3)
	>>> c1.get_radio()
	Estoy dando el radio
	3
	>>> c1.set_radio(-1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_python3/curso/u51/circulo.py", line 8, in set_radio
	    raise ValueError("Radio positivo")
	ValueError: Radio positivo

A Python, les propietats ens permeten implementar la funcionalitat exposant aquests mètodes amb atributs.

	class circulo():
		def __init__(self,radio):
			self.radio=radio
		
		@property
		def radio(self):
			print("Estoy dando el radio")
			return self._radio	

		@radio.setter
		def radio(self,radio):
			if radio>=0:
				self._radio = radio
			else:
				raise ValueError("Radio positivo")
				self._radio=0


	>>> c1=circulo(3)
	>>> c1.radio
	Estoy dando el radio
	3
	>>> c1.radio=4
	>>> c1.radio=-1
	Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_python3/curso/u52/circulo2.py", line 15, in radio
	    raise ValueError("Radio positivo")
	ValueError: Radio positivo

Hi ha un tercera property que podem crear: **el deleter**

	...
	@radio.deleter
	def radio(self):
		del self._radio


	>>> c1=circulo(3)
	>>> c1.radio
	Estoy dando el radio
	3
	>>> del c1.radio
	>>> c1.radio
	Estoy dando el radio
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_python3/curso/u52/circulo2.py", line 8, in radio
	    return self._radio
	AttributeError: 'circulo' object has no attribute '_radio'
	>>> c1.radio=3

## Representació d'objectes \_\_str\_\_ y \_\_repr\_\_

La documentació de Python fa referencia a que el mètode `__str()__` ha de retornar la representació "informal" de l'objecte, mentres que `__repr()__` la "formal".

* La funció `__str()__` ha de retornar la cadena de texte que es mostra per pantalla si cridem a la funció `str()`. Això és lo que fa Python quan utilitzem `print`. Sol retornar el nom de la classe.
* De `__repr()__`, per un altre costat, 'espera que ens retorni una cadena de texte amb una representació única de l'objecte. Idealment, la cadena retornada per `__repr()__` hauria de ser aquella que, passada a `eval()`, retorna el mateix objecte.

Continuem amb la classe `circulo`:

	...
	def __str__(self):
		clase = type(self).__name__
		msg = "{0} de radio {1}"
		return msg.format(clase, self.radio)

	def __repr__(self):
		clase = type(self).__name__
		msg = "{0}({1})"
		return msg.format(clase, self.radio)


Suposem que estem utilitzant la classe `circulo` sense la instrucció `print` en el getter. 

	>>> c1=circulo(3)
	>>> print(c1)
	circulo de radio 3
	>>> repr(c1)
	'circulo(3)'
	>>> type(eval(repr(c1)))
	<class 'circulo2.circulo'>

## Comparació d'objectes \_\_eq\_\_

Tampoc podem comparar dos `circulos` sense definir `__eq()__`, ja que sense aquest mètode Python compararà posicions en memòria.

Continuem amb la classe `circulo`:
	
	...
	def __eq__(self,otro):
		return self.radio==otro.radio

	>>> c1=circulo(5)
	>>> c2=circulo(3)
	>>> c1 == c2
	False

Si volem utilitzar `<`, `<=`, `>` y `>=` haurem de reescriure els mètodes: `__lt()__`, `__le()__`, `__gt()__` i `__ge()__`

## Operar amb objectes \_\_add\_\_ y \_\_sub\_\_

Si volem operar amb els operadors `+` i `-`:

	def __add__(self,otro):
		self.radio+=otro.radio

	def __sub__(self,otro):
		if self.radio-otro.radio>=0:
			self.radio-=otro.radio
		else:
			raise ValueError("No se pueden restar")

	>>> c1=circulo(5)
	>>> c2=circulo(3)
	>>> c1 + c2
	>>> c1.radio
	8	
	

	>>> c1=circulo(5)
	>>> c2=circulo(3)
	>>> c1 - c2
	>>> c1.radio
	2
	>>> c1 - c2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_python3/curso/u52/circulo2.py", line 42, in __sub__
	    raise ValueError("No se pueden restar")
	ValueError: No se pueden restar

## Més mètodes especials

Existeixen molts més mètodes especials que podem sobreesciure en les nostres classes per afegir funcionalitat a les mateixes Pots veure la [documentació oficial](https://docs.python.org/3.11/reference/datamodel.html#special-method-names) per aprendre més sobre elles.
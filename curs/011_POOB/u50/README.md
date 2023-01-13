# Programació orientada a objectes

## Introducció a la Programació Orientada a Objectes

La Programació Orientada a Objectes (POO) es basa en l'agrupació d'objectes de diferents classes que interactuen entre sí i que, en conjunt, aconsegueixen que un programa compleixi el seu  propósit. A Python qualsevol element del llenguatge pertany a una classe i totes las classes tenen el mateix rang i s'utilitzen de la mateixa manera.

## Definició de classe, objecte, atributs i mètodes

* Anomenem classe a la representació abstracta d'un concepte. Per exemple, "perro", "número entero" o "servidor web".
* Les classes es composen d'atributs i mètodes.
* Un objecte és cadascuna de les instàncies d'una classe.
* Els atributs defineixen les característiques propies de l'objecte i modifiquen el seu estat. Son dades associades a les classes i als objectes creats a partir d'elles.
* Un atribut de classe es compartit por totes les instancies d'una classe. Es defineixen dintre de la classe (després de l'encapçalament de la classe) però mai dintre d'un mètode. Aquest tipus de variables no s'utilizen amb tanta freqüència como les variables d'instància.
* Un atribut d'objecte es defineix dintre d'un mètode i pertany a un objecte determinat de la classe instanciada.
* Els mètodes son blocs de codi (o funcions) d'una classe que s'utilitzen per definir el comportament dels objectes.

Definim la nostra primera classe:

	>>> class clase():
	...    at_clase=1
	...    def metodo(self):
	...      self.at_objeto=1
	... 
	>>> type(clase)
	<class 'type'>
	>>> clase.at_clase
	1
	>>> objeto=clase()
	>>> objeto.at_clase
	1
	>>> objeto.at_objeto

	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'clase' object has no attribute 'at_objeto'
	>>> objeto.metodo()
	>>> objeto.at_objeto
	1

## Atributs de objectes

Per definir atributs d'objectes, ni ha prou amb definir una variable dintre dels mètodes, es una bona idea definir tots els atributs de les nostres instancies en el constructor, de manera que es crein amb algun valor vàlid. 

## Mètode constructor __init__

Com hem vist anteriorment els atributs d'objectes no es creen fins que no hem executat el mètode. Tenim un mètode especial, anomenat constructor `__init__`, que ens permet inicialitzar els atributs de objectes. Aquest mètode es crida cada vegada que es crea una nova instancia de la classe.

## Definint mètodes. El parámetre self

El mètode constructor, al igual que tots els mètodes de qualsevol classe, rep com a primer paràmetre a la instancia sobre la que està treballant. Per convenció a aquest primer paràmetre se li sol anomenar `self` (que podríem traduir com jo mateix), però pot anomenar-se de qualsevol manera.

Per referir-se als atributs d'objectes s'ha de fer a partir de l'objecte `self`.

## Definició d'objectes

Anem a crear una nova classe:

	import math

	class punto():
	""" Representació d'un punto en el pla, els atributos son x e y
	que representen els valors de les coordenades cartesianes."""

	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def distancia(self, otro):
		""" Retorna la distància entre els dos punts. """
		dx = self.x - otro.x
		dy = self.y - otro.y
		return math.sqrt((dx*dx + dy*dy))
		
Per crear un objecte, utilitzem el nom de la classe enviant com paràmetre els valors que va a rebre el constructor.

	>>> punto1=punto()
	>>> punto2=punto(4,5)
	>>> print(punto1.distancia(punto2))
	6.4031242374328485

Podem accedir i modificar els atributs de objecte:

	>>> punto2.x
	4
	>>> punto2.x = 7
	>>> punto2.x
	7



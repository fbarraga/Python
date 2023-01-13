# Polimorfisme, herencia i delegació
	
## Polimorfisme

El polimorfisme és la tècnica que ens possibilita que l'invocar un determinat mètode d'un objecte, podrán obtenir-se distints resultats segons la classe de l'objecte. Això es deu a que diferents objectes poden tenir un mètode amb un mateix nom, però que realitzi diferents operacions.

Per exemple podems recórrer amb una estructura `for` diferents classes d'objecte, degut a que el mètode especial `__iter__` està definida en cadascuna de las classes. Un altre exemple sería que amb la funció `print` podem imprimir diferents classes d'objecte, en aquest cas, el mètode especial `__str__` està definit en totes les classes.

A més això és possible ja que python és dinàmic, és a dir en temps d'execució és quan es determina el tipus d'un objecte. Exemple:

	class gato():
		def hablar(self):
			print("MIAU")	

	class perro():
		def hablar(self):
			print("GUAU")	

	def escucharMascota(animal):
		animal.hablar()	

	if __name__ == '__main__':
		g = gato()
		p = perro()
		escucharMascota(g)
		escucharMascota(p)

## Herencia

La herencia es un mecanisme de la programació orientada a objectes que serveix per crear classes noves a partir de classes preexistents. Es prenen (hereden) atributs i mètodes de les classes antigues i se les modifica per modela una nova situació.

La classe des de la que s'hereda s'anomena classe base i la que es construeix a partir d'ella es una classe derivada.

Si la nostra classe base és la classe `punto`, podem crear una nova classe de la següent manera:

	class punto3d(punto):
		def __init__(self,x=0,y=0,z=0):
			super().__init__(x,y)
			self.z=z
		@property
		def z(self):
			return self._z	

		@z.setter
		def z(self,z):
			self._z=z	

		def __str__(self):
			return super().__str__()+":"+str(self.z)	

		def distancia(self,otro):
			dx = self.x - otro.x
			dy = self.y - otro.y
			dz = self.z - otro.z
			return (dx*dx + dy*dy + dz*dz)**0.5	

Creem dos objectes de cada classe i veiem els atributs i mètodes que tenen definit:

	>>> p=punto(1,2)
	>>> dir(p)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', '_y', 'distancia', 'x', 'y']
	>>> p3d=punto3d(1,2,3)
	>>> dir(p3d)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', '_y', '_z', 'distancia', 'x', 'y', 'z']

## La funció super()

La funció `super()` em proporciona una referència a la classe base. I podem observar també que hem reescritt el mètode `distancia` i `__str__`.

	>>> p.distancia(punto(5,6))
	5.656854249492381
	>>> p3d.distancia(punto3d(2,3,4))
	1.7320508075688772
	>>> print(p)
	1:2
	>>> print(p3d)
	1:2:3

## Herència múltiple

La herència múltiple es refereix a la possibilitat de crear una classe a partir de múltiples classes superiors. Es importante anomenar adequadament els atributs i els mètodes en cada classe per no crear conflicteszas.

	class Telefono:
	    "Clase teléfono"
	    def __init__(self,numero):
	        self.numero=numero
	    def telefonear(self):
	        print('llamando')
	    def colgar(self):
	        print('colgando') 
	    def __str__(self):
	        return self.numero	

	class Camara:
	    "Clase camara fotográfica"
	    def __init__(self,mpx):
	        self.mpx=mpx
	    def fotografiar(self):
	        print('fotografiando')        
	    def __str__(self):
	        return self.mpx
	class Reproductor:
	    "Clase Reproductor Mp3"
	    def __init__(self,capcidad):
	        self.capacidad=capcidad
	    def reproducirmp3(self):
	        print('reproduciendo mp3')                  
	    def reproducirvideo(self):
	        print('reproduciendo video')                  
	    def __str__(self):
	        return self.capacidad	

	class Movil(Telefono, Camara, Reproductor):
	    def __init__(self,numero,mpx,capacidad):
	        Telefono.__init__(self,numero)
	        Camara.__init__(self,mpx)
	        Reproductor.__init__(self,capacidad)
	    def __str__(self):
	        return "Número: {0}, Cámara: {1},Capacidad: {2}".format(Telefono.__str__(self),Camara.__str__(self),Reproductor.__str__(self))

Veiem els atributs i mètodes d'un objecte `Movil`:

	>>> mimovil=Movil("645234567","5Mpx","1G")
	>>> dir(mimovil)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'capacidad', 'colgar', 'fotografiar', 'mpx', 'numero', 'reproducirmp3', 'reproducirvideo', 'telefonear']
	>>> print(mimovil)
	Número: 645234567, Cámara: 5Mpx,Capacidad: 1G

## Funcions issubclass() y isinstance() 

La funció `issubclass(SubClase, ClaseSup)` s'utilitza per comprovar si una classe (SubClasse) es filla d'una altra superior (ClaseSup), retornant True o False segons sigui el cas. 

	>>> issubclass(Movil,Telefono)
	True

La funció booleana `isinstance(Objeto, Clase)` s'utilitza per comprovar si un objecte pertany a una classe o classe superior. 

	>>> isinstance(mimovil,Movil)
	True

## Delegació

Anomenem delegació a la situació en la que una classe conté (com atributs) una o més instancies d'un altra classe, a les que delegarà part de les seves funcionalitats.

A partir de la classe `punto`, podem crear la classe `circulo` d'aquesta manera:

	class circulo():	

		def __init__(self,centro,radio):
			self.centro=centro
			self.radio=radio	

		def __str__(self):
			return "Centro:{0}-Radio:{1}".format(self.centro.__str__(),self.radio)	

i creem un objecte `circulo`:

	>>> c1=circulo(punto(2,3),5)
	>>> print(c1)
	Centro:2:3-Radio:5

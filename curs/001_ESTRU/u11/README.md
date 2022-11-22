# Entrada i sortida estàndard

## Funció input

Ens permet llegir per teclat informació. Retorna una cadena de caràcters i pot tenir com argument una cadena que es mostra en pantalla.

*Exemples*

	>>> nom=input("Nom:")
	Nom:josep
	>>> nom
	'josep'
	>>> edat=int(input("Edat:"))
	Edat:23
	>>> edat
	23
	
## Funció print

Ens permet escriure en la sortida estándar. Podem indicar varis dades a imprimir, que per defecte estarán separats per un espai (es pot indicar el separador) i per defecte es termina amb un caràcter salt de línea `\n` (també podem indicar el caràcter final). Podem també imprimir varies cadenes de texte utilizant la concatenació.

*Exemples*

	>>> print(1,2,3)
	1 2 3
	>>> print(1,2,3,sep="-")
	1-2-3
	>>> print(1,2,3,sep="-",end=".")
	1-2-3.>>> 

	>>> print("Hola son les",6,"de la tarda")
	Hola son les 6 de la tarda
	>>> print("Hola son les "+str(6)+" de la tarda")
	Hola son les 6 de la tarda

## Formatejant cadenes de caràcters
	
Existeix dos formes d'indicar el format de impressió de las cadenes. En la documentació trobarem :
	* [estilo antiguo 2.x](https://docs.python.org/2/library/stdtypes.html#string-formatting) 
	* [estilo nuevo 3.x](https://docs.python.org/3/library/string.html#string-formatting).

*Exemples del estil antic*

	>>> print("%d %f %s" % (2.5,2.5,2.5))
	2 2.500000 2.5

	>>> print("%s %o %x"%(bin(31),31,31))
	0b11111 37 1f

	>>> print("El producto %s cantidad=%d precio=%.2f"%("cesta",23,13.456))
	El producto cesta cantidad=23 precio=13.46	

## Funció format()

Per utilitzar el nou estil en python3 tenim una funció `format` i un métode `format` a la classe `str`. Exemples utilizant la función `format`:

*Exemples*

	>>> print(format(31,"b"),format(31,"o"),format(31,"x"))
	11111 37 1f

	>>> print(format(2.345,".2f"))
	2.35


[Index](../../README.md)
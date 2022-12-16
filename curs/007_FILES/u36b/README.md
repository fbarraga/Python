# Lectura i escriptura de fitxers de texte

## Funció open()

La funció [open()](https://docs.python.org/3.11/library/functions.html#open) s'utilitza normalment amb dos paràmetres (fitxer amb el que anem a treballar i mode d'accés) i ens retorna un objecte de tipus fitxer.

	>>> f = open("exemple.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

### Modes d'accés

Els modes què podem seleccionar son:

<table>
	<tr>
		<td>Mode</td>
		<td>Comportament</td>
		<td>Punter</td>
	</tr>
	<tr><td>r</td><td>Només lectura</td><td>A l'inici del fitxer</td></tr>
	<tr><td>rb</td><td>Només lectura en mode binari </td><td></td></tr>
	<tr><td>r+</td><td>Lectura i escriptura </td><td>A l'inici del fitxer</td></tr>
	<tr><td>rb+</td><td>Lectura i escriptura binari</td><td>A l'inici del fitxer</td></tr>
	<tr><td>w</td><td>Només escriptura. Sobreescriu si existeix. Crea el fitxer si no existeix.</td><td>A l'inici del fitxer</td></tr>
	<tr><td>wb</td><td>Només escriptura en mode binari. Sobreescriu si existeix. Crea el fitxer si no existeix.</td><td>A l'inici del fitxer</td></tr>
	<tr><td>w+</td><td>Escriptura i lectura. Sobreescriu si existeix. Crea el fitxer si no existeix.</td><td>A l'inici del fitxer</td></tr>
	<tr><td>wb+</td><td>Escriptura i lectura binaria. Sobreescriu si existeix. Crea el fitxer si no existeix.</td><td>A l 'inici del fitxer</td></tr>
	<tr><td>a</td><td>Añadido (agregar contenido). Crea el archivo si no existe.</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>ab</td>Añadido en modo binario. Crea si éste no existe<td></td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>a+</td><td>Añadido y lectura. Crea el archivo si no existe.</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>ab+</td><td>Añadido y lectura en binario. Crea el archivo si no existe</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	
</table>

### Codificació de caràcters

Si treballem amb fitxers de texte podem indicar també el paràmetre `encoding` que serà la codificació de caràcters utilitzats al treballar amb el fitxer. Per defecte s'utilitzarà la que estigui indicada pel sistema:

	>>> import locale
	>>> locale.getpreferredencoding()
	'UTF-8'

I per últim també podem indicar el parámetre `errors` que controla el comportament quan es troba algún error al codificar o decodificar caràcters.

## Objecte fitxer

Al obrir un fitxer amb un determinat mode d'accés la funció `open()` ens retorna un objecte de tipus fitxers. El fitxer obert sempre s'ha de tancar amb el mètode `close()`:

	>>> f = open("exemple.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

Es poden accedir a les següents propietats d'un objecte file:

* `closed`: retorna `True` si el fitxer s'ha tancat. De lo contrari, `False`.
* `mode`: retorna el mode d'obertura.
* `name`: retorna el nom del fitxer
* `encoding`: retorna la codificació de caràcteres d'un fitxer de texte

Podem obrir-lo i tancar-lo amb la mateixa instrucció amb la següent estructura:

	>>> with open("ejemplo.txt", "r") as fitxer: 
	...    contenido = fitxer.read()
	>>> fitxer.closed
	True

## Mètodes principals

### Mètodes de lectura

	>>> f = open("exemple1.txt","r")
	>>> f.read()
	'Hola que tal\n'

	>>> f = open("exemple1.txt","r")
	>>> f.read(4)
	'Hola'
	>>> f.read(4)
	' que'
	>>> f.tell()
	8
	>>> f.seek(0)
	>>> f.read()
	'Hola que tal\n'

	>>> f = open("exemple2.txt","r")	
	>>> f.readline()
	'Línea 1\n'
	>>> f.readline()
	'Línea 2\n'
	>>> f.seek(0)
	0
	>>> f.readlines()
	['Línea 1\n', 'Línea 2\n']

### Mètodes d'escriptura

	>>> f = open("exemple3.txt","w")
	>>> f.write("Prova 1\n")
	9
	>>> print("Prova 2\n",file=f)
	>>> f.writelines(["Prova 3","Prova 4"])
	>>> f.close()
	>>> f = open("exemple3.txt","r")
	>>> f.read()
	'Prpva 1\nProva 2\n\Prova 3Prova 4'

## Recorregut de fitxers

	>>> with open("exemple3.txt","r") as fitxer:
	...    for linia in fitxer:
	...        print(linia)

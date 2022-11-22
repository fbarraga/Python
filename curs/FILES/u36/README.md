# Lectura i escriptura de fitxers de texte

## Funció open()

La funció [open()](https://docs.python.org/3.11/library/functions.html#open) s'utilitza normalment amb dos paràmetres (fitxer amb el que anem a treballar i mode d'accés) i ens retorna un objecte de tipus fitxer.

	>>> f = open("exemple.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

### Modes d'accés

Los modos que podemos indicar son los siguientes:

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

Com podem comprovar podem treballar amb fitxers binaris i amb fitxers de text.

### Codificació de caràcters

Si trabajamos con fichero de textos podemos indicar también el parámetro `encoding` que será la codificación de caracteres utilizadas al trabajar con el fichero, por defecto se usa la indicada en el sistema:

	>>> import locale
	>>> locale.getpreferredencoding()
	'UTF-8'

Y por último también podemos indicar el parámetro `errors` que controla el comportamiento cuando se encuentra con algún error al codificar o decodificar caracteres.

## Objeto fichero

Al abrir un fichero con un determinado modo de acceso con la función `open()` se nos devuelve un objeto fichero. El fichero abierto siempre hay que cerrarlo con el método `close()`:

	>>> f = open("ejemplo.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

Se pueden acceder a las siguientes propiedades del objeto file:

* `closed`: retorna `True` si el archivo se ha cerrado. De lo contrario, `False`.
* `mode`: retorna el modo de apertura.
* `name`: retorna el nombre del archivo
* `encoding`: retorna la codificación de caracteres de un archivo de texto

Podemos abrirlo y cerrarlo en la misma instrucción con la siguiente estructura:

	>>> with open("ejemplo.txt", "r") as archivo: 
	...    contenido = archivo.read()
	>>> archivo.closed
	True

## Métodos principales

### Métodos de lectura

	>>> f = open("ejemplo.txt","r")
	>>> f.read()
	'Hola que tal\n'

	>>> f = open("ejemplo.txt","r")
	>>> f.read(4)
	'Hola'
	>>> f.read(4)
	' que'
	>>> f.tell()
	8
	>>> f.seek(0)
	>>> f.read()
	'Hola que tal\n'

	>>> f = open("ejemplo2.txt","r")	
	>>> f.readline()
	'Línea 1\n'
	>>> f.readline()
	'Línea 2\n'
	>>> f.seek(0)
	0
	>>> f.readlines()
	['Línea 1\n', 'Línea 2\n']

### Métodos de escritura

	>>> f = open("ejemplo3.txt","w")
	>>> f.write("Prueba 1\n")
	9
	>>> print("Prueba 2\n",file=f)
	>>> f.writelines(["Prueba 3","Prueba 4"])
	>>> f.close()
	>>> f = open("ejemplo3.txt","r")
	>>> f.read()
	'Prueba 1\nPrueba 2\n\nPrueba 3Prueba 4'

## Recorrido de ficheros

	>>> with open("ejemplo3.txt","r") as fichero:
	...    for linea in fichero:
	...        print(linea)

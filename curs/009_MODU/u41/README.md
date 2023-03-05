# Mòduls estàndards: mòduls de sistema

Python té els seus propis mòduls, els quals formen part de la seva llibreria de mòduls estàndard, que també poden ser importats. En aquesta unitat anem a estuir les funcions principals de mòduls relacionats amb el sistema operatiu i especialment amb el treball amb fitxers i directoris.

## Mòdul os

El mòdul [os](https://docs.python.org/3.11/library/os.html#module-os) ens permet accedir a funcionalitats dependenes del Sistema Operatiu. Sobre tot, aquelles que ens refereixen informació sobre l'entorn del mateix i ens permeten manipular l'estructura de directoris.

<table>
<thead>
<tr>
  <th>Descripció</th>at
  <th>Mètode</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Saber si es pot accedir a un arxiu o directori</td>
  <td><code>os.access(path, mode_de_acces)</code></td>
</tr>
<tr>
  <td>Conèixer el directori actual</td>
  <td><code>os.getcwd()</code></td>
</tr>
<tr>
  <td>Canviar de directori de treball</td>
  <td><code>os.chdir(nuevo_path)</code></td>
</tr>
<tr>
  <td>Canviar el directori de treball arrel</td>
  <td><code>os.chroot()</code></td>
</tr>
<tr>
  <td>Canviar els permissos d'un arxiu o directori</td>
  <td><code>os.chmod(path, permisos)</code></td>
</tr>
<tr>
  <td>Canviar el propietari d'un arxiu o directorio</td>
  <td><code>os.chown(path, permissos)</code></td>
</tr>
<tr>
  <td>Crear un directori</td>
  <td><code>os.mkdir(path[, mode])</code></td>
</tr>
<tr>
  <td>Crear directoris recursivament</td>
  <td><code>os.mkdirs(path[, mode])</code></td>
</tr>
<tr>
  <td>Eliminar un fitxer</td>
  <td><code>os.remove(path)</code></td>
</tr>
<tr>
  <td>Eliminar un directori</td>
  <td><code>os.rmdir(path)</code></td>
</tr>
<tr>
  <td>Eliminar directoris recursivamente</td>
  <td><code>os.removedirs(path)</code></td>
</tr>
<tr>
  <td>Renombrar un fitxer</td>
  <td><code>os.rename(actual, nou)</code></td>
</tr>
<tr>
  <td>Crear un enllaç simbòlic</td>
  <td><code>os.symlink(path, nom_desti)</code></td>
</tr>
</tbody>
</table>

	>>> import os
	>>> os.getcwd()
	'/home/francesc/github/python/curs/u40'
	>>> os.chdir("..")
	>>> os.getcwd()
	'/home/francesc/github/python/curs'

El mòdul os també ens proveeix del submòdul path (os.path) el qual ens permet accedir a certes funcionalitats relacionades amb els noms de les rutes de fitxers i directoris.

<table>
<thead>
<tr>
  <th>Descripció</th>
  <th>Mètode</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Ruta absoluta</td>
  <td><code>os.path.abspath(path)</code></td>
</tr>
<tr>
  <td>Directori base</td>
  <td><code>os.path.basename(path)</code></td>
</tr>
<tr>
  <td>Saber si un directori existeix</td>
  <td><code>os.path.exists(path)</code></td>
</tr>
<tr>
  <td>Conèixer el darrer accés a un directori</td>
  <td><code>os.path.getatime(path)</code></td>
</tr>
<tr>
  <td>Conèixer tamany del directori</td>
  <td><code>os.path.getsize(path)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és absoluta</td>
  <td><code>os.path.isabs(path)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és un fitxer</td>
  <td><code>os.path.isfile(path)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és un directori</td>
  <td><code>os.path.isdir(path)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és un enllaç simbòlic</td>
  <td><code>os.path.islink(path)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és un punt de muntatge</td>
  <td><code>os.path.ismount(path)</code></td>
</tr>
</tbody>
</table>

### Executar comandes del sistema operatiu. Mòdul subprocess

Amb la funció `system()` del mòdul `os` ens permet executar comandes del sistema operatiu.

	>>> os.system("ls")
	curs  model.odp  README.md
	0

La funció ens retorna un codi per indicar si l'instrucció s'ha executat amb èxit.

Tenim una altre manera d'executar comandes del sistema operatiu que ens dona més funcionalitat, per exemple ens permet guardar la sortida de la comanda en una variable. Per fer-ho podem utilitzar el mòdul [subprocess](https://docs.python.org/3.11/library/subprocess.html)

	>>> import subprocess
	>>> subprocess.call("ls")
	curs  model.odp  README.md
	0

	>>> salida=subprocess.check_output("ls")
	>>> print(salida.decode())
	curs
	model.odp
	README.md

	>>> salida=subprocess.check_output(["df","-h"])

	>>> salida = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
	>>> salida.communicate()[0]

## Mòdul shutil

El mòdul [shutil](https://docs.python.org/3.11/library/shutil.html#module-shutil) de funcions per realitzar operacions d'alt nivell amb fitxers i directoris. Dintre de les operacions que es poden realitzar estàn copiar,moure i borrar fitxers i directories; i copiar els permissos i l'estat dels fitxers.

<table>
<thead>
<tr>
  <th>Descripció</th>
  <th>Mètode</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Copia un fitxers complert o part</td>
  <td><code>shutil.copyfileobj(fsrc, fdst[, length])</code></td>
</tr>
<tr>
  <td>Copia el contingut complet (sense metadades) d'un fitxer</td>
  <td><code>shutil.copyfile(src, dst, *, follow_symlinks=True)</code></td>
</tr>
<tr>
  <td>copia els permissos d'un fitxer origen a un destí</td>
  <td><code>shutil.copymode(src, dst, *, follow_symlinks=True)</code></td>
</tr>
<tr>
  <td>Copia els permissos, la data-hora de l'últim accés, la data-hora de la darrera modificació i els atributs d'un fitxer origen a un fitxer destí</td>
  <td><code>shutil.copystat(src, dst, *, follow_symlinks=True)</code></td>
</tr>
<tr>
  <td>Copia un fitxer (només dades i permissos)</td>
  <td><code>shutil.copy(src, dst, *, follow_symlinks=True)</code></td>
</tr>
<tr>
  <td>Copia fitxers (dades, permissos i metadades) </td>
  <td><code>shutil.move(src, dst, copy_function=copy2)</code></td>
</tr>
<tr>
  <td>Obté informació de l'espai total, usat i lliure, en bytes </td>
  <td><code>shutil.disk_usage(path)</code></td>
</tr>
<tr>
  <td>Obtenir la ruta d'un fitxer executable </td>
  <td><code>shutil.chown(path, user=None, group=None)</code></td>
</tr>
<tr>
  <td>Saber si una ruta és un enllaç simbòlic</td>
  <td><code>shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)</code></td>
</tr>
</tbody>
</table>


## Mòduls sys 

El mòdul [sys](https://docs.python.org/3.11/library/sys.html#module-sys) és el encarregat de proveir variables i funcionalitats, directament relacionades amb l'intèrpret.

Algunes variables definides en el mòdul:

<table>
<thead>
<tr>
  <th>Variable</th>
  <th>Descripció</th>
</tr>
</thead>
<tbody>
<tr>
  <td><code>sys.argv</code></td>
  <td>Retorna una lista con todos los argumentos pasados por línea de comandos. Al ejecutar <code>python modulo.py arg1 arg2</code>, retornará una lista: <code>['modulo.py', 'arg1', 'arg2']</code></td>
</tr>
<tr>
  <td><code>sys.executable</code></td>
  <td>Retorna el path absoluto del binario ejecutable del intérprete de Python</td>
</tr>
<tr>
  <td><code>sys.platform</code></td>
  <td>Retorna la plataforma sobre la cuál se está ejecutando el intérprete</td>
</tr>
<tr>
  <td><code>sys.version</code></td>
  <td>Retorna el número de versión de Python con información adicional</td>
</tr>
</tbody>
</table>

Y algunos métodos:

<table>
<thead>
<tr>
  <th>Método</th>
  <th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
  <td><code>sys.exit()</code></td>
  <td>Forzar la salida del intérprete</td>
</tr>
<tr>
  <td><code>sys.getdefaultencoding()</code></td>
  <td>Retorna la codificación de caracteres por defecto</td>
</tr>
</tbody>
</table>

## Execució de scripts amb arguments

Podem enviar informació (arguments) a un programa quan s'executa como un script, per exemple:

	#!/usr/bin/env python	
	import sys
	print("Has instroducido",len(sys.argv),"argumento")
	suma=0
	for i in range(1,len(sys.argv)):
		suma=suma+int(sys.argv[i])
	print("La suma es ",suma)

	$  python3 sumar.py 3 4 5
	Has introducido 4 argumento
	La suma es  12

## Altres mòduls interessants

### pathlib
Permet manipular rutes de sistemes d'arxius de forma agnòstica en qualsevol sistema 
operatiu. El mòdul pathlib és similar a l'os.path, però pathlib ofereix una interfície de 
nivell més alt, i, sovint, més convenient, que os.path.

### glob
Inclou funcions per buscar en una ruta tots els noms d'arxius i/o directoris que 
coincideixin amb un determinat patró que pot contenir comodins com els que s'utilitzen 
en un intèrpret de comandaments tipus Unix (*,?, []).

### filecmp
Defineix funcions per comparar fitxers i directoris

***
[Index](../../../README.md)

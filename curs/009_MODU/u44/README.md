# Instal·lació de mòduls

Python té una molt activa comunitat de desenvolupadors i usuaris que desenvolupen tant els mòduls estandards de python, com mòduls i paquets desenvolupats per tercers.

## PyPI y pip

* El *Python Package Index* o *PyPI*, es el repositori de paquets de software oficial per aplicacions de tercers en el llenguatge de programació Python.

* `pip`: Sistema de gestió de paquets utilizat per instal·lar i administrar paquets de software escrits en Python que es troben allotjats en el repositori *PyPI*.

## Instal·lació de mòduls python

Per instal·lar un nou paquet python hi ha varies opcions:

1. Utilitzar el que estigui empaquetat en la distribució que estiguis utilitzant. Podem tenir problemes si necesitem una versió determinada.

		# apt-cache show python3-requests
		...
		Version: 2.4.3-6
		...

2. Instal·lar pip en el nostre equip, i com superusuari instal·lar el paquet python que ens interesa. Aquesta solució ens pot donar molts problemes, ja que podem trencar les dependencies entre versions dels nostre paquest python instal·lats en el sistema i algun pot deixar de funcionar. (Això aplica a Linux ja que python forma part del sistema operatiu).
3. 
		# pip search requests
		...
		requests (2.13.0)      - Python HTTP for Humans.
		...

4. Utilitzar entorns virtuals: es un mecanisme que ens permet gestionar programes i paquets python sense tenir permissos d'administració, es a dir, qualsevol usuari sense privilegis pot tenir un o més espais aillats ( ja veurem més endavant que els entorns virtuals es guarden en directoris) on poder instal·lar diferents versions de programes i paquets python. Per crear els entorns virtual utilitzarem el programa `virtualenv` o el mòdul `venv`.

## Actualitzar els mòduls de python

Sovint haurem d'actualitzar la versió dels moduls de python
Podem consultar els moduls que s'han d'actualitzar executant:

	# pip list --obsolete

Per actualitzar un modul ho fem amb la comanda:

	# pip install <nom modul> --upgrade

## Instal·lar moduls antics

A vegades pot ser que tinguem una versió de Python superior a la versió amb la que s'hagués fet el mòdul o requereixi el modul. Podem instal·lar el modul utilitzant la següent comanda.

	# pip install <nom modul> --pre



## Creant entornos virtuals en linux amb `virtualenv`

Podem utiliztar aquest software para treballar amb qualsevol distribució de python.

	# apt-get install python-virtualenv

Si volem crear un entorn virtual amb python3:

	$ virtualenv -p /usr/bin/python3 entorno2

La opció `-p` ens permet indicar l'intèrpret que s'utilizarà en l'entorn.

Per activar el nostre entorn virtual:

	$ source entorno2/bin/activate
	(entorno2)$ 

I per desactivar-ho:

	(entorno2)$ deactivate
	$

## Creant entorns virtuals amb `venv`

A partir de la versió 3.3 de python podem utilizar el módulo `venv` per crear l'entorn virtual.

Instal·lem el següent paquet per instal·lar el mòdul:

	# apt-get install python3-venv

Ara ja com un usuari sense privilegis podem crar un entorn virtual amb python3:

	$ python3 -m venv entorno3

L'opció `-m` de l'interpret ens permet executar un módul com si fos un programa.

Per activar i desactivar l'entorn virtual:

	$ source entorno3/bin/activate
	(entorno3)$ deactivate
	$ 


## Creants entorns virtuals en Windows amb virtualenv

S'instal·la el mòdul de virtual env

```
pip install virtualenv
```

Desde la carpeta del nostre projecte executem:
```
virtualenv .venv
```
On `.venv` es la carpeta del nostre entorn virtual. Es recomana utilitzar aquest nom (.venv)

## Instal·lant paquets en el nostre entorn virtual

Independientement del sistema utilitzat per crear el nostre entorn virtual, una vegada que ho tenim activat podem instal·lar paquets python en ell utilitzat l'eina `pip` (que la tenim instal·lada automàticament en el nostre entorn). Partint d'un entorn activat podem, per exemple, instal·lar la darrera versió de django:

	(entorno3)$ pip install django

Si volem veure els paquets que tenim instal·lats amb les seves dependencies:

	(entorno3)$ pip list
	Django (4.30.5)
	pip (2.1.6)
	setuptools (5.5.1)

Si necesitem buscar un paquet podem utilitzar la següent opció:

	(entorno3)$ pip search requests

Si a continuació necesitem instal·lar una versió determinada del paquet, que no sigui la darrera, podem fer-ho de la següent manera:

	(entorno3)$ pip install requests=="2.12"

Si necessitem borrar un paquet podemos executar:

	(entorno3)$ pip uninstall requests

I,per instal·lar la darrera versió simplement:

	(entorno3)$ pip install requests	

Per acabar de veeure les opcions de l'eina pip, ara veure com podem guardar en un fitxer (que se sol dir  `requirements.txt`) la llista de paquets instal·lats, que ens permet de manera senzilla crear un altre entorn virtual en una alra màquina amb els mateixos paquets instal·lats. Per fer-ho anem a utilitzar la següent opció de `pip`:

	(entorno3)$ pip freeze
	Django==4.30.5
	requests==2.13.0

I si volem guardar aquesta informació en un fitxer que poguem distribuir:

	(entorno3)$ pip freeze > requirements.txt

De tal manera que un altre usuari, en un altre entorn, tenint aquest fitxer pot instal·lar els mateixos paquets de la següent manera:

	(entorno4)$ pip install -r requirements.txt


***
[Index](../../../README.md)

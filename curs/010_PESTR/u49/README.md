# Programació estructurada i modular: Exemple complet

Partint del fitxer csv `liga.csv` amb els resultats de les jornades de lliga 2015-2016, realitzar un programa que mostri la taula de classificació al final de la lliga, en el qual ha d'aparèixer l'ordre que ha quedat cada equip, els partits guanyats, els empatats i perduts, i per últim els punts aconseguits.

Per realitzar aquest programa hem de construir diverses funcions:

* `LlegirPartits()`: Funció que llegeix el fitxer CSV i retorna les dades del mateix en una llista de diccionaris.
* `impClassificacio(lliga)`:Rep la llista de diccionaris generat a parir de la funció anterior, genera les dades de la classificació i les imprimeix per pantalla.

Aquesta funció utilitza interna les funcions següents:

* `Equips(dades)`: Funció que rep la llista de diccionaris amb les dades de la lliga i retorna un conjunt amb els equips de la lliga.
* `InfoEquips(dades,equips)`: Funció que rep la llista de diccionaris amb les dades de la lliga i el conjunt d'equips i retorna una llista de tuplas, a cada tupla es guarda un equip amb els partits guanyats, empatats i perduts i els punts obtinguts.

	Aquesta funció utilitza internament:

	* `QuiGana(resultat)`: Funció que rep un resultat i retorna un 0 si és un empat, un 1 si guanya l'equip de casa i -1 si guanya l'equip visitant.
	* `Punts(info)`: Funció que rep una llista amb els partits guanyats, empatats i perduts i retorna els punts obtinguts.

* `Classificacio(dades)`: Rep la llista generada amb la funció anterior i l'ordena segons el nombre de punts.


***
[Index](../../../README.md)

# UF2: Persistència amb Bases de Dades BDR,BDOR,BDOO
## Activitat 1: Treball amb Base de Dades

### Explicació

* Aquesta pràctica s'haurà d'explicar al professor i s'haurà de fer funcionar amb Linux.

* L’elecció del bloc d’exercicis es realitzarà en funció del següents càlcul:
	D	són els dos darrers números del DNI de l’alumne.
	A	són els dos darrers números del vostre any de naixement.
    M	és el número que correspon al mes de la vostra data de naixement

N = (D+A+M) mod 3

| N   | BLOC |
|-----|------|
| 0   |  A   |
| 1   |  B   |
| 2   |  C   |


## A GESTOR DE COMPTES BANCARIS
Crear un programa, amb **Python i Pyscopg**, que permeti gestionar les dades referents als comptes corrents 
dels clients d’una entitat bancària.
El programa permetrà les següents operacions:
  * Llistar les dades personals de tots els clients.
  * Llistar les dades personals dels clients amb una edad inferior a N anys.
  * Llistar les dades personals dels clients amb una edad superior a N anys.
  * Llistar els comptes corrents dels que disposa una persona.
  * Llistar el saldo dels comptes corrents del que disposa una persona.
  * Ingressar diners a un compte corrent.
  * Retirar diners d’un compte corrent.
  * Realitzar un traspàs de diners entre dos comptes corrents d’una mateixa persona.
  * Realitzar una transferència de diners d’un compte corrent d’una persona a un compte corrent d’una 
altre persona.
  * Llistar l’historial d’operacions d’un compte corrent.


L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat
* +2Punts si utilitzeu un ORM

## B GESTOR D’UN APARCAMENT PÚBLIC
Crear un programa, amb **Python i Psycopg2**, que permeti gestionar les dades referents a l’ús d’un 
aparcament públic.
El programa permetrà les següents operacions:
  * Obtenir el número de places disponibles.
  * Obtenir el número de places ocupades.
  * Donat el número de matrícula d’un vehicle que vol sortir de l’aparcament, l’import que ha de pagar.
  * Donades una data i una hora, el número de places ocupades.
  * Donat el número de matrícula d’un vehicle, l’historial d’estacionaments a l’aparcament.
  * Donat el número d’una plaça d’aparcament, l’historial d’estacionaments.
  * Donada una data, llistat de les deu places més ocupades durant la data, indicant el número 
d’ocupacions i ordenat de més a menys.


L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat.
* +2Punts si utilitzeu un ORM


## C GESTOR D’UN MUSEU
Crear un programa, amb **Python i Psycopg2**, que permeti gestionar les dades referents als béns culturals d’un 
museu.
El programa permetrà les següents operacions:
* Llistat de tots els béns.
* Llistat de les diferents col·leccions.
* Afegir un bé a una col·lecció.
* Donat el nom d’una col·lecció, un llistat de tots els seus béns.
* Donat una data, llistat de tots els béns que són anteriors a la data indicada.


L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat.
* +2Punts si utilitzeu un ORM


## COL·LECCIÓ MUSICAL
Crear un programa, amb **Python i Psycopg2**, que permeti emmagatzemar les dades d’una col·lecció de discos de vinil.
El programa permetrà les següents operacions:

* Afegir un disc (amb les seves dades).
* Donada una cadena de text, que representa el nom d’un/a intèrpret o grup, obtenir un llistat de tots els discos de la col·lecció que el nom del/a intèrpret o el grup inclou la cadena de text.
* Donat una cadena de text, que representa un gènere musical, obtenir un llistat dels discos de la col·lecció que contenen cançons del gènere indicat.
● Donat un any, obtenir un llistat dels discos de la col·lecció
● Modificar les dades d’un disc.
● Eliminar un disc.

L’usuari interactuarà amb el programa mitjançant mitjançant menús i l’introducció de dades a través del teclat.


## AGENDA TELEFÒNICA
Crear un programa, amb **Python i Psycopg2**, que permeti emmagatzemar les dades referents als números de telèfons d’un grup de persones. S’ha de tenir en compte que una persona pot disposar de més d’un número de telèfon.
El programa permetrà les següents operacions:
* Afegir una persona.
* Afegir un número de telèfon d’una persona.
* Obtenir un llistat del nom i cognoms de totes les persones (ordenat pels cognoms).
* Donada una cadena de text, els números de telèfon de les persones que els seus cognoms contenen la cadena de text.
* Modificar les dades d’una persona.
* Eliminar un número de telèfon.
* Eliminar una persona.

L’usuari interactuarà amb el programa mitjançant mitjançant menús i l’introducció de dades a través del teclat.

## GESTOR DE L’INVENTARI D’UNA BOTIGA
Crear un programa, amb **Python i Psycopg2**, que permeti gestionar les dades referents a l’inventari d’una botiga.
El programa permetrà les següents operacions:
* Afegir un producte.
* Afegir unitats d’un producte.
* Obtenir un llistat dels productes disponibles.
* Donat el nom d’un producte, el seu codi de referència.
* Donat un codi de referència, indicar quantes unitats hi ha disponibles.
* Donat un codi de referència, obtenir un llistat històric de les seves existències.
* 
L’usuari interactuarà amb el programa  mitjançant menús i l’introducció de dades a través del teclat
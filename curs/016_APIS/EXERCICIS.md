# UF4: Recuperació de dades accedint a APIs

## Activitat 1: Treball amb APIs

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


## A - L'HOME DEL TEMPS
Crear un programa, amb **Python** , que permeti recuperar la temperatura de les 4 provincies catalanes i inserti les dades en una base de dades MongoDB.

El programa permetrà les següents operacions:
  * Introduir les ciutats d'on es vol consultat la temperatura
  * Consultar les temperatures a la web de OpenWeatherMap.
  * Llistar les temperatures de totes les ciutats.
  * Llistar les temperatures d'una ciutat entre dues dates.

L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat.
Podeu consultar l'ajuda de l'API a https://openweathermap.org/api

## B - LA LIGA DE FUTBOL
Crear un programa, amb **Python**, que permeti recuperar els resultats dels partits de la Liga de futbol i inserti les dades en una base de dades MongoDB.

El programa permetrà les següents operacions:
  * Consultar els resultats a la web de resultados-futbol.com.
  * Llistar els resultats a una data.
  * Llistar tots els equips de la Lliga.


L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat.
Podeu consultar l'ajuda de l'API a https://www.resultados-futbol.com/api/documentacion


## C - LA FESTA DEL CINEMA
Crear un programa, amb **Python**, que permeti recuperar la cartellera de pel·lícules que hi ha les poblacions escollides.

El programa permetrà les següents operacions:
  * Introduir les ciutats d'on es vol consultar la cartellera
  * Consultar les cartelleres a la web de themoviedb.org.
  * Llistar la cartellera de Girona.
  * Buscar si una pel·lícula està en cartellera.


L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat.
Podeu consultar l'ajuda de l'API a https://api.themoviedb.org




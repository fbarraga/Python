# Introducció a Python
## Activitat 6: Treball amb fitxers

### Explicació

* Aquesta pràctica s'haurà d'explicar al professor i s'haurà de fer funcionar amb Linux.

* L’elecció del bloc d’exercicis es realitzarà en funció del següents càlcul:
	D	són els dos darrers números del DNI de l’alumne.
	A	són els dos darrers números del vostre any de naixement.
    M	és el número que correspon al mes de la vostra data de naixement

N = (D+A+M) mod 5

| N   | BLOC |
|-----|------|
| 0   |  A   |
| 1   |  B   |
| 2   |  C   |
| 3   |  D   |
| 4   |  E   |

### A. GESTOR DE FITXERS

Crear un programa que permeti gestionar fitxers i directoris.
El programa permetrà les següents operacions:

* Llistar els fitxers d’un directori.
* Obtenir informació d’un fitxer (nom, grandària, data de modificació, etc).
* Eliminar un fitxer.
* Eliminar un directori.
* Cercar fitxers a partir d’un patró en el nom.
* Comprimir un fitxer.
* Comprimir un directori.
* Copiar un fitxer d’un directori a un altre.
* Copiar un directori a un altre.
* Moure un fitxer d’un directori a un altre.
* Moure un directori a un altre.
* Mostrar el contingut d’un fitxer de text pla.
  
Es recomana que totes les operacions que realitzi el programa hauràn de estar implementades mitjançant 
funcions. L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat

### B. GESTOR DE DADES DEL PERSONAL

Crear un programa que donat un fitxer XML amb les dades (personals i profesionals) de les persones que 
treballen a una empresa permeti la seva gestió.
Indicacions:

* El programa en primer lloc haurà de carregar en memòria (llista, diccionari, etc) les dades del fitxer i quan finalitzi actualitzar els canvis si es necessàri.

* El programa permetrà les següents operacions:
    * Obtenir un llistat per la pantalla de les dades bàsiques (dni, nom i cognoms) de totes les persones.
    * Donat un text mostrar les dades de la persona que el seu dni és igual al text indicat.
    * Afegir una persona.
    * Eliminar una persona.
  
* Es recomana que totes les operacions que realitzi el programa hauràn de estar implementades mitjançant 
funcions.L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat

### C. RESULTATS D’UNA CURSA

Crear un programa que obtingui les diferents classificacions d’una cursa.

Aclaracions:

* Les dades de les persones que han participat estaran disponibles a dos fitxers JSON, el primer contindrà les dades personals de les persones (dni, nom, cognoms, data de naixement i número de dorsal) i el segon les dades dels diferents controls (id del control, dorsal, timestamp).
* El programa permetrà obtenir les diferents classificacions: absoluta (inclou totes les persones), menors de deu anys i majors de setanta anys.
* El programa inclourà la possibilitat de volcar les classificacions en diferents fitxers JSON amb el nom de fitxer a escollir per l’usuari.
* Es recomana que totes les operacions que realitzi el programa hauràn de estar implementades mitjançant 
funcions.
* L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat

### D. GESTIÓ DEL PAGAMENT D’UN APARCAMENT

Crear un programa que indiqui quan ha de pagar un vehicle al sortir d’un aparcament.

Aclaracions:
* Les dades dels vehicles que han entrat a l’aparcament (matricula, timestamp) estaran disponibles a un fitxer JSON. 
* Els preu a pagar per minut pot variar cada mes, la informació dels preus estarà emmagatzemada a un fitxer JSON.
* El programa haurà d’indicar quan ha de pagar un vehicle en funció dels minuts que ha estat estacionat a 
l’aparcament.
* Es recomana que totes les operacions que realitzi el programa hauràn de estar implementades mitjançant 
funcions.
* L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat


### E. GESTIÓ D'UNA BIBLIOTECA

Crear un programa que permeti gestionar una biblioteca i el procés de prestec de llibres.

Aclaracions:
* Les dades dels llibres que hi ha a la biblioteca  (isbn,nom,autor) estaran disponibles a un fitxer CSV. 
* Els llibres es podran prestar gratuitament per un periode de 7 dies. En cas d'entrega posterior s'haurà de pagar 5€ per dia de retras. Tots els préstecs s'hauran de guardar en un fitxer CSV.
* Els socis de la biblioteca (DNI, nom, idsoci, telefon) els guardarem a un fitxer JSON.
* El programa haurà de permetre prestar llibres i fer el retorn.En el cas de retorn amb penalització, s'haurà d'informar al soci que ha de pagar l'import.
* Es recomana que totes les operacions que realitzi el programa hauràn de estar implementades mitjançant 
funcions.
* L’usuari interactuarà amb el programa mitjançant menús i l’introducció de dades a través del teclat




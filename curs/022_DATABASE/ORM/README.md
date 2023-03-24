# Mapatge Objecte Relacional (ORM)

## Què es un ORM?
El mapatge d'objectes-relacional (ORM, Object-relational mapping) és una tècnica de programació per convertir dades de 
llenguatges de programació orientats a objectes en la seva  representació en bases de dades relacionals, a través de la 
definició de les correspondències entre els diferents sistemes. 

El seu ús s'ha incrementat en els darrers anys, millorant el SQL per la capacitat de delimitar el nombre de registres d'una consulta a més d'alliberar al programador de l'escriptura mnual per crear les consultes i gestionar les dades en el RDBMS

L'ORM coné eines que permeten la conversió d'objectes per ser enmmagatzemats en una BDR. També dona la possibilitat de utilitzar les característiques propies de POO, especialment l'herencia i el polimorfisme. Igualment recuperar les dades emmagatzemades de la BDR, ja que converteix els registres en objectes.

Com a resum, podem dir que un ORM funciona como una solució intermitja que  facilitando la tarea del programador  accedint a les dades d'una manera senzilla i agnòstica del SGBDR que utilitzis.

## Avantatges i desavantages d'un ORM

Les eines ORM ofereixen una sèrie d' avantatges per al programador com són:

* Desenvolupament Ràpid
* Abstracció de la base de dades utilitzada
* Seguretat de la capa d'accés
* Facilitat per al manteniment del codi
* Llenguatge propi per a la realització de consultes

Pero no tot son avantatges, també té algunes desavantages com:

*L'aprenentatge del llenguatge de l' eina ORM pot resultar ser complex ja que, per poder treure el màxim partit a l' eina, cal conèixer en profunditat com funciona la mateixa.
* En entorns de gran càrrega, aquest tipus de solució penalitza el rendiment a causa dels processos de transformació de les consultes que es facin cap a la base de dades.


# Python y ORM

Python disposa de varis ORM pero els més populars i utilitzats son:
* PeeWee és un ORM lleuger que permet interactuar amb bases de dades MySQL, PostgreSQL i SQLite
* Alchemy és un ORM complet que permet interactuar amb 
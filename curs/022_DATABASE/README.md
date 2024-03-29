# UF2
## Accés a Base de Dades (BDR,BDOR,BDOO)

### Introducció

Per poder connectar a una base de dades necessitem utilitzar un *connector* o *driver*.
Un connector per tant és un element del programa que permet que un  llenguatge de programació pugui interactuar amb una base de  dades a través d’un sistema de gestió de bases de dades.

Existeix un connector diferent per cadascun dels sistemes gestors de base de dades al que ens volem connectar. Així per exemple tenim:

   1. PostGreSQL: **psycopg2**
   2. MySQL:**mysql.connector**
   3. SQLServer: **pymssql**
   4. Oracle: **oracledb**

Tots aquests connectors es poden instal·lar mitjançant la comanda:

`pip install <nom del connector>`


# Drivers/Connectors Genèrics

## ODBC: (Open DataBase Connectivity) 

Família de connectors creats per Microsoft, que s’integra en el 
sistema operatiu de Windows i que permet afegir múltiples  connectors a diverses bases de dades SQL de forma molt senzilla i transparent, ja que els connectors son autoinstal·lables i totalment configurables des de les mateixes eines del sistema operatiu

El driver de `python` per treballar amb ODBC s'anomena **pyodbc**.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/odbc.png?raw=true)


## JDBC: (Java DataBase Connectivity)

Connectors creats per Sun Microsystems, es tracta d’un API connector de bases de dades, implementat específicament per usar amb el llenguatge `Java`. Es tracta d’un API forca similar a ODBC quant a funcionalitat, però adaptat a les especificitats de Java.

![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/jdbc.png?raw=true)


## Python Llibreries SQL

Pots consultar aquest link per tenir més informació sobre les llibreries més utilitzades en Python [Realpython](https://realpython.com/python-sql-libraries/)


***
[Index](../../README.md)

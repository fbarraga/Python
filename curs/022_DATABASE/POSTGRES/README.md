# Connexió a Base de dades Postgres

## Introducció

Per poder treballar amb postgres desde Python haurem d'instal·lar el mòdul psycopg2.Pots consultar totes les opcions d'aquest mòdul:
*[pypi](https://pypi.org/project/psycopg2/)
*[github](https://github.com/psycopg/psycopg2)



## Instal·lem el mòdul psycopg2 de Python

```
pip install psycopg2
```

## Connectar a la base de dades

Per connectar a la base de dades haurem d'especificar com a mínim aquests paràmetres:

```python
import psycopg2
connexio = psycopg2.connect(host="localhost", dbname="hr", user="usuariprova", password="12345")  
```

|Paràmetre| Valor |
|---------|-------|
|**host**| ip o nom del servidor de base de dades|
|**dbname**| nom de la base de dades|
|**user**| usuari per connectar a la bd|
|**password**| password per connectar a la bd|

## Cursors

Un cop hagim establert la connexió contra la Base de Dades podem obrir un cursor i executar comandes SQL.


Creem dintre del Postgres una base de dades d'exemple que farem servir amb els exemples de codi:

```sql
CREATE DATABASE dbprova;  
CREATE USER usuariprova WITH PASSWORD '12345';  CREATE ROLE
GRANT ALL PRIVILEGES ON DATABASE dbprova TO usuariprova;
```


```python
import psycopg2

connexio = psycopg2.connect(host="localhost", dbname="hr", user="usuariprova", password="12345")  
cur = connexio.cursor()
cur.execute("SELECT * FROM tprova;")  
```

El cursor recuperarà de la base de dades tots els registres que retorni la sentència SQL. A partir d'aquí podem fer el recorregut del cursor a través de les comandes fetchone, y fetchall

### Seleccionem un registre de la base de dades: FETCHONE


```python
# programa.py
import psycopg2

connexio = psycopg2.connect(host="localhost", dbname="hr", user="usuariprova", password="12345")  
cur = connexio.cursor()
cur.execute("SELECT * FROM tprova;")  
reg = cur.fetchone()

while reg is not None:  
    print(f"{reg[0]},{reg[1]}");  
    reg = cur.fetchone()
    cur.close()  
connexio.close()
```

Sortida:
```
regular@debian:~$ python3 programa.py
1,aaaaa  
2,bbbbb  
3,ccccc
```

### Seleccionem tots els registres: FETCHALL


```python
# programa.py
import psycopg2
connexio = psycopg2.connect(host="localhost", dbname="dbprova", user="usuariprova", password="12345")  
cur = connexio.cursor()
cur.execute("SELECT * FROM tprova;")  
registres = cur.fetchall()

for reg in registres:  
    print(f"{reg[0]},{reg[1]}");
    cur.close()  
connexio.close()
```

Sortida:
```
regular@debian:~$ python3 programa.py
1,aaaaa  
2,bbbbb  
3,ccccc
```

### Tancar la connexió: CLOSE

Després de treballar amb la nostra base de dades, i al igual que fem amb els fitxers hem de tancar la connexió per tal d'alliberar els recursos.


## Inserir registres

```python
posts = [
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "Anyone up for a late-night party today?", 3),
]

post_records = ", ".join(["%s"] * len(posts))

insert_query = (
    f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, posts)
```


***
[Index](../../../README.md)





# Connexió a Base de dades Postgres

## Exemple

Creem dintre del postgres una base de dades d'exemple:

```sql
CREATE DATABASE dbprova;  
CREATE USER usuariprova WITH PASSWORD '12345';  CREATE ROLE
GRANT ALL PRIVILEGES ON DATABASE dbprova TO usuariprova;
```


## Instal·lem el mòdul psycopg2 de Python

```
pip install psycopg2
```

Per connectar a la base de dades haurem d'especificar com a mínim aquests paràmetres:
|Paràmetre| Valor |
|---------|-------|
|**host**| ip o nom del servidor de base de dades|
|**dbname**| nom de la base de dades|
|**user**| usuari per connectar a la bd|
|**password**| password per connectar a la bd|


```python
import psycopg2

connexio = psycopg2.connect(host="localhost", dbname="hr", user="usuariprova", password="12345")  
cur = connexio.cursor()
cur.execute("SELECT * FROM tprova;")  
reg = cur.fetchone()

while reg is not None:  
    print(f"{reg[0]},{reg[1]}");  
    reg = cur.fetchone()
    cur.close()  connexio.close()
```

Sortida:
```
regular@debian:~$ python3 programa.py
1,aaaaa  
2,bbbbb  
3,ccccc
```
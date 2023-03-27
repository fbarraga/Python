# ORM : Peewee

## Instal·lació de Peewee
Per instal·lar [Peewee](https://docs.peewee-orm.com/en/latest/) podem utilitzar el pip:

```python
pip install peewee
```

## Exemple: Creació de taules

El primer que es fa amb un ORM es definir el model de dades. Cada classe del nostre ORM es transformarà en una taula, i cada atribut en un camp. Existeix un mapatge de tipus que fa internament el ORM.

Creem dintre de postgresql una base de dades que l'anomenarem **db_agenda**

```sql
CREATE DATABASE db_agenda;
CREATE USER uagenda WITH PASSWORD '12345';
GRANT ALL PRIVILEGES ON DATABASE db_agenda TO uagenda;
```

Ara escriurem el codi utilitzant el ORM per tal de que ens crei les taules.


```python
from peewee import *

bdd_agenda = PostgresqlDatabase(
                             'db_agenda',
                             user='uagenda',
                             password='12345',
                             host='localhost',
                            port=5432)

class BaseModel(Model):
    class Meta:
      database = bdd_agenda

class Persona(BaseModel):
    id_p = AutoField()
    nom = TextField()
    cognoms = TextField()
    data_naixement = DateField()

class Telefon(BaseModel):
    id_t = AutoField()
    persona_id = ForeignKeyField(Persona)
    numero = CharField()


bdd_agenda.connect()
bdd_agenda.create_tables([Persona, Telefon])
bdd_agenda.close()
```
Si anem a mirar la base de dades després d'executar el programa veure'm que ens ha creat les taules.

Es poden consultar quins tipus de dades podem tenir en el model, en el següent [link](https://docs.peewee-orm.com/en/latest/peewee/models.html)


## Exemple: Inserció de registres

```python
from peewee import *

bdd_agenda = PostgresqlDatabase(
                    'db_agenda',
                    user='uagenda',
                    password='12345',
                    host='localhost',
                    port=5432)

class BaseModel(Model):
    class Meta:
        database = bdd_agenda

class Persona(BaseModel):
    id_p = AutoField()
    nom = TextField()
    cognoms = TextField()
    data_naixement = DateField()

class Telefon(BaseModel):
    id_t = AutoField()
    persona_id = ForeignKeyField(Persona)
    numero = CharField()

bdd_agenda.connect()

agarcia = Persona(
                  nom = 'antoni',
                  cognoms = 'garcia sanchez',
                  data_naixement = '1978-09-21')
tel_agarica = Telefon(
                      persona_id = 1,
                      numero = '972335794')

agarcia.save()
tel_agarica.save()
bdd_agenda.close()
```

## Exemple: Modificació de registres

```python
from peewee import *
bdd_agenda = PostgresqlDatabase(
                            'db_agenda',
                            user='uagenda',
                            password='12345',
                            host='localhost',
                            port=5432)

class BaseModel(Model):
    class Meta:
        database = bdd_agenda

class Persona(BaseModel):
    id_p = AutoField()
    nom = TextField()
    cognoms = TextField()
    data_naixement = DateField()

class Telefon(BaseModel):
    id_t = AutoField()
    persona_id = ForeignKeyField(Persona)
    numero = CharField()

bdd_agenda.connect()
Telefon.update(numero = '972356758').where(Telefon.id_t == 1).execute()
bdd_agenda.close()
```
## Exemple: Eliminar registres

````python
from peewee import *
bdd_agenda = PostgresqlDatabase(
                        'db_agenda',
                        user='uagenda',
                        password='12345',
                        host='localhost',
                        port=5432)
class BaseModel(Model):
    class Meta:
        database = bdd_agenda

class Persona(BaseModel):
    id_p = AutoField()
    nom = TextField()
    cognoms = TextField()
    data_naixement = DateField()

class Telefon(BaseModel):
    id_t = AutoField()
    persona_id = ForeignKeyField(Persona)
    numero = CharField()

bdd_agenda.connect()
Telefon.delete().where(Telefon.numero == '972356758').execute()
bdd_agenda.close()
```






***
[Index](../../../README.md)

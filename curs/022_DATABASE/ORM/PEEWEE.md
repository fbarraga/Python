# ORM : Peewee

## Instal·lació de Peewee
Per instal·lar Peewee podem utilitzar el pip:

```python
pip install peewee
```

## Exemple de funcionament

El primer que es fa amb un ORM es definir el model de dades. Cada classe del nostre ORM es transformarà en una taula, i cada atribut en un camp. Existeix un mapatge de tipus que fa internament el ORM.

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
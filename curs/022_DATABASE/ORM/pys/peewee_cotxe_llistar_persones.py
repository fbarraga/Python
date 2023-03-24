from peewee import *
bdd_cotxes = PostgresqlDatabase('db_cotxes', user='uscot', password='12345', host='localhost', port=5432)
class BaseModel(Model):
 class Meta:
     database = bdd_cotxes
class Persona(BaseModel):
 id_p = AutoField()
 nom = TextField()
 cognoms = TextField()
class Cotxe(BaseModel):
 id_c = AutoField()
 marca = CharField()
 model = CharField()
 matricula = CharField()
class Propietat(BaseModel):
 id_p = AutoField()
 cotxe_id = ForeignKeyField(Cotxe)
 persona_id = ForeignKeyField(Persona)
 data_compra = DateField()
bdd_cotxes.connect()
cadena = input('Cadena de text dels cognoms? ')
consulta = Persona.select().where(Persona.cognoms.contains(cadena))
for r in consulta:
 print(f"{r.cognoms}, {r.nom}")
bdd_cotxes.close()
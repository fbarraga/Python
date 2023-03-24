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
consulta = Cotxe.select().order_by(Cotxe.marca)
#consulta = Cotxe.select().order_by(Cotxe.marca).desc()
for r in consulta:
 print(f"{r.marca} {r.model}")
bdd_cotxes.close()

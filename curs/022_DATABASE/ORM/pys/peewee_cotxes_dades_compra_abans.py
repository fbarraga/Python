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
cad_data = input('Data de compra anterior a? ')
consulta_data = Propietat.select().where(Propietat.data_compra < cad_data)
if consulta_data:
 for r in consulta_data:
    consulta_cotxe = Cotxe.select().where(Cotxe.id_c == r.cotxe_id)
    for c in consulta_cotxe:
     print(f"{c.marca} {c.model} {r.data_compra}")
else:
 print("Cap cotxe!")
bdd_cotxes.close()
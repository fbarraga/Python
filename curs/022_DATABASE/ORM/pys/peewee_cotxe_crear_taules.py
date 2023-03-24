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
dades_persones = [{'nom': 'anna', 'cognoms': 'pou rull'}, {'nom': 'pere', 'cognoms': 'massa rou'}]
dades_cotxes = [
 {'marca': 'renault', 'model': 'clio', 'matricula': '4532CJF'},
 {'marca': 'seat', 'model': 'ibiza', 'matricula': '1243BDR'},
 {'marca': 'opel', 'model': 'corsa', 'matricula': '7658JLK'},
 {'marca': 'renault', 'model': 'megane', 'matricula': '3428LMN'}
]
dades_propietat = [
 {'cotxe_id': '3', 'persona_id': '1', 'data_compra': '2018-04-29'},
 {'cotxe_id': '4', 'persona_id': '2', 'data_compra': '2019-12-14'}
]
bdd_cotxes.connect()
bdd_cotxes.create_tables([Persona, Cotxe, Propietat])
Persona.insert_many(dades_persones).execute()
Cotxe.insert_many(dades_cotxes).execute()
Propietat.insert_many(dades_propietat).execute()
bdd_cotxes.close()

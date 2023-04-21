from peewee import *

bdd_agenda = PostgresqlDatabase(
                             'db_agenda',
                             user='uagenda',
                             password='12345',
                             host='192.168.56.102',
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
te
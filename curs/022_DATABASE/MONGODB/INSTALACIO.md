# MongodB

## MongoDB "on premise"

MongoDB es pot instal3lar sobre plataforma Windows / Linux encara que es preferible utilitzar Linux. El procediment d'instal·lació  el podeu consultar en la [documentació oficial de MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)


## MongoDB SaaS "cloud"

MongoDB pot ser utilitzada desplegant la base de dades al cloud i connectant-nos des del nostre ordinador. És un servei gratuit per una base de dades simple, i de pagament quan volem fer definicions més complexes.

Per poder desplegar una base de dades en Cloud, utilitzarem [Mongo Atlas](https://www.mongodb.com/atlas). Els passos que haurem de fer per poder-la crear son:

* Registrarnos dintre de Mongo Atlas (És aconsellable utilitzar el compte de Google o Github)
* Crear una organització.
* Crear un projecte. (per agrupar les bases de dades/Aplicacions que creem)
* Definir un cluster (Database Deployment). Un cluster es un conjunt de servidors que executarà la teva base de dades. Amb la opció gratuita només podem seleccionar l'opció més simple, pero podriem tenir una base de dades replicada en diferents llocs, backups, polítiques de contingència,etc.
    ![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/mongodb_inst00.png?raw=true)
* Escollim el nom de la base de dades i la ubicació. (Per exemple Parking i Europa)
* Assignem usuari i password a la base de dades.
* Especifiquem des d'on ens connectarem. Podem aplicar filtres de IPs. Revisem quina es la nostra IP i l'afegim dintre de les IPs validades.

Una vegada desplegat la Base de dades, podem administrar-la des del nostre ordinadoramb el **Mongo Shell**

Per executar-ho podem 
```
mongosh "mongodb+srv://parking.1jvwodg.mongodb.net/Parking" --apiVersion 1 --username adminbdd
```

## Eines per la gestió de la base de dades

### MongoDB Shell

Es pot descarregar l'eina des d'aquest [link](https://www.mongodb.com/try/download/shell)
MongoShell es una aplicació en mode comanda que ens permet executar comandes en el nostre MongoDB. Es recomenat quan utilitzem scripts que interactuen amb la base de dades. 
Actua de la mateixa manera que el psql de Postgresql o el sqlplus d'Oracle. Podeu consultar més informació en el següent [link](https://www.mongodb.com/docs/mongodb-shell/)


### MongoDB Compass (GUI)

Es pot descarregar l'eina des d'aquest [link](https://www.mongodb.com/try/download/compass)

Es una eina GUI que permet administrar la base de dades des d'una interfície gràfica. Inclou dintre de la solució el MongoShell. Es correspondria al PGAdmin4 de Postgresql o al Enterprise Manager d'Oracle. Podeu consultar més informació en aquest [link](https://www.mongodb.com/docs/compass/master/)


## Ordres bàsiques a MongoDB

`help`: Mostra informació sobre l'ajuda
`db`: Mostra la base de dades en ús
`db.stats`: Mostra informació sobre la base de dades en ús
`use database`: Crea una base de dades (si el nom indicat existeix, fa la connexió a aquesta bd)
`show dbs`: Mostra les bases de dades amb contingut (no buides)
`db.dropdatabase()`: Borra la base de dades en ús
`db.createCollection()`: Crea una col·lecció (equivalent a una taula SQL)
`show collections`: Mostra les col·leccions en ús
`db.collection.drop`: Borra la col·lecció en ús de la base de dades en ús
`db.collection.insertOne`: Insereix un document dintre de la col·lecció en ús

```mongo
> db
biblioteca
> show collections
autors
llibres
> db.autors.insertOne( { id: "1", cognoms: "rodoreda i gurguí", nom: "mercè" } );
{
"acknowledged" : true,
"insertedId" : ObjectId("605c6c1d2e50ebf3923f1b3d")
}
>
``` 


***
[Index](../../../README.md)

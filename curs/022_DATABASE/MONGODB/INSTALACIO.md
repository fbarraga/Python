# MongodB

## MongoDB "on premise"

## MongoDB SaaS "cloud"

MongoDB pot ser utilitzada desplegant la base de dades al cloud i connectant-nos des del nostre ordinador. És un servei gratuit per una base de dades simple, i de pagament quan volem fer definicions més complexes.

Per poder desplegar una base de dades en Cloud, utilitzarem [Mongo Atlas](https://www.mongodb.com/atlas). Els passos que haurem de fer per poder-la crear son:

    1. Crear un usuari dintre de Mongo Atlas (És aconsellable utilitzar el compte de Google o Github)
    2. Crear una organització.
    3. Crear un projecte. (per agrupar les bases de dades/Aplicacions que creem)
    4. Definir un cluster. Un cluster es un conjunt de servidors que executarà la teva base de dades. Amb la opció gratuita només podem seleccionar l'opció més simple, pero podriem tenir una base de dades replicada en diferents llocs, backups, polítiques de contingència,etc.
    ![Tabla](https://github.com/fbarraga/Python/blob/master/master/assets/mongodb_inst00.png.png?raw=true)
    5. Escollim el nom de la base de dades i la ubicació.
    6. Assignem usuari i password a la base de dades.
    7. Especifiquem des d'on ens connectarem. Podem aplicar filtres de IPs.


***
[Index](../../../README.md)
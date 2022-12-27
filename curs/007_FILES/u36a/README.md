# Serialització

## Procés de serialització/ deserialització

El procés de serialització consisteix a transformar un objecte determinat en un text a partir d'un llenguatge específic, per ser emmagatzemat o bé transferit i, finalment, restablert a l'objecte original.
Per exemple, desar una llista de Python en un arxiu de text o base de dades, i després carregar quan sigui necessari. Formats comuns entre els diferents llenguatges de programació inclouen CSV, XML i JSON

Igual que el Transporter a Star Trek, es tracta d'agafar quelcom complicat i convertir-lo en una seqüència plana d'1 i 0, després agafar aquesta seqüència d'1 i 0 (possiblement en un altre lloc, possiblement en un altre moment) i reconstruir el complicat original ". alguna cosa.”

## Com puc seleccionar la millor tècnica de serialització?

Hi ha molts i molts (i molts)  sistemes de serialització però els podem agrupar entre llegible per humans ("text") o no llegible per humans ("binari”), seguit d'una llista de cinc tècniques (n'hi ha més) disposades més o menys en ordre creixent de sofisticació.

* Decidiu entre els formats llegibles pels humans ("text") i els no llegibles pels humans ("binaris").
    
* Utilitzeu la solució menys sofisticada quan els objectes que s'han de serialitzar no formen part d'una jerarquia d'herència (és a dir, quan són tots de la mateixa classe) i quan no contenen punters a altres objectes.
    
* Utilitzeu el segon nivell de sofisticació quan els objectes que s'han de serialitzar formen part d'una jerarquia d'herència, però quan no contenen punters a altres objectes.
    
* Utilitzeu el tercer nivell de sofisticació quan els objectes a serialitzar contenen punters a altres objectes, però quan aquests punters formen un arbre sense cicles ni juntes.
    
* Utilitzeu el quart nivell de sofisticació quan els objectes que s'han de serialitzar contenen punters a altres objectes i quan aquests punters formen un gràfic sense cicles i amb unions només a les fulles.

* Utilitzeu la solució més sofisticada quan els objectes que s'han de serialitzar contenen punters a altres objectes i quan aquests punters formen un gràfic que pot tenir cicles o unions.

## Com puc decidir si serialitzar en format llegible per a humans ("text") o no llegible per humans ("binari")?

Amb cura.

No hi ha una resposta "correcta" a aquesta pregunta; realment depèn dels teus objectius. A continuació, es mostren alguns dels avantatges i desavantatges del format ("text") llegible per humans i el format ("binari") no llegible per humans:

* El format de text és més fàcil de "comprovar a l'escriptori". Això vol dir que no haureu d'escriure eines addicionals per depurar l'entrada i la sortida; podeu obrir la sortida serialitzada amb un editor de text per veure si sembla correcte.
* El format binari normalment utilitza menys cicles de CPU. Tanmateix, això només és rellevant si la vostra aplicació està vinculada a la CPU i teniu intenció de fer la serialització i/o la no serialització en un bucle/coll d'ampolla interior. Recordeu: el 90% del temps de la CPU es gasta en el 10% del codi, la qual cosa significa que no hi haurà cap benefici pràctic de rendiment tret que el vostre "mesurador de CPU" estigui vinculat al 100% i el vostre codi de serialització i/o de no serialització estigui consumint una part saludable d'aquest 100%.
* El format de text us permet ignorar problemes de programació com sizeof i little-endian vs big-endian.
* El format binari us permet ignorar les separacions entre valors adjacents, ja que molts valors tenen longituds fixes.
* El format de text pot produir resultats més petits quan la majoria dels números són petits i quan necessiteu codificar textualment resultats binaris, per exemple, uuencode o Base64.
* El format binari pot produir resultats més petits quan la majoria dels números són grans o quan no necessiteu codificar textualment els resultats binaris.

Podríeu pensar en altres per afegir-hi també... El més important a recordar és que una mida no s'adapta a tots: feu una decisió acurada aquí.

Una cosa més: independentment del que trieu, és possible que vulgueu iniciar cada fitxer / flux amb una etiqueta "màgica" i un número de versió. El número de versió indicaria les regles de format. D'aquesta manera, si decidiu fer un canvi radical en el format, espereu que encara podreu llegir la sortida produïda pel programari antic.


***
[Index](../../../README.md)

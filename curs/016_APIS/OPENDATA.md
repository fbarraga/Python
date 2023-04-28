# Open Data 

## Què és OpenData o Dades Obertes?

Les dades obertes (open data en anglès) són conjunts de dades produïdes o recopilades per organismes públics que les administracions públiques posen a disposició de la ciutadania perquè les pugui utilitzar lliurement de manera senzilla i còmoda.

Les dades obertes tenen un gran valor potencial i són essencials per a la transparència de les administracions públiques, l’eficiència i la igualtat d’oportunitats a l’hora de crear riquesa.

L'objectiu principal de l’obertura de dades és posar a disposició de la societat, i fer-les públiques, les dades que gestiona l’Administració, de manera que qualsevol persona o organització pugui fer-les servir. Amb aquest servei, les administracions augmenten la transparència, ja que el ciutadà accedeix a una visió real de la prestació de serveis. A més, la reutilització de dades obertes per part d’empreses, entitats, associacions i ciutadania en general permet elaborar nous productes i serveis que aporten valor, innovació, coneixement i oportunitats de negoci.

Les llicències i els termes d’ús de les dades obertes estan sotmesos a les lleis de reutilització de la informació del sector públic. En alguns casos, poden tenir llicències de propietat intel·lectual, tot i que es tendeix a obrir-les sense condicions, sempre que es mantinguin sense manipular i amb la citació obligatòria de la font i de la seva darrera actualització. Per a més informació, podeu consultar l’apartat "Termes d’ús i llicències".

## Què és un dataset?

El terme dataset, procedent de l’anglès, es refereix a un conjunt de dades, habitualment estructurades, que s’han utilitzat per construir una informació publicada en catàlegs de dades o bé es mostren d’una manera independent.

Les dades en brut s’organitzen en datasets per poder ser indexades i localitzades més fàcilment. Per aconseguir-ho, es fan servir diferents camps que defineixen el grup de dades, com ara la descripció, la freqüència d’actualització, el format o la llicència d’ús, entre d’altres.

ELs organismes publics integren datasets organitzats en diversos formats, categories i fonts de dades que permeten a la ciutadania disposar d’un gran ventall de dades diferents. Es poden usar dades molt diverses dels diferents organismes : dades geogràfiques, meteorològiques, estadístiques, econòmiques, administratives, turístiques, jurídiques, de mobilitat, entre d’altres.

Exemples d'aquests datasets els podem consultar a :

https://opendata-ajuntament.barcelona.cat/data/ca/dataset

https://governobert.gencat.cat/ca/dades_obertes/inici
     
Per exemple les dades obertes de la Generalitat de Catalunya ens ofereix les següents categories entre altres:

    * Ciencia i Tecnologia
    * Comerç
    * Cultura i oci
    * Demografia
    * Economia
    * ...

## Quins son els formats de dades?

Aquests organismes publiquen la informació agrupada en diferents catàlegs, i accessible mitjançant diferents mètodes i formats. El més habitual es que poguem consultar-la mitjançant la crida a una API REST o descàrrega directe de fitxer.

Els datasets disponibles a la plataforma de dades obertes es poden exportar en múltiples formats. A continuació es detallen breument:

 
* CSV / TSV
És un format obert, senzill i d’ús molt estès per representar dades tabulades. Aquests fitxers es poden obrir tant amb editors de text (bloc de notes de Windows, MS Word) com amb editors de fulls de càlcul (MS Excel, OpenOffice Calc, etc.). Les dades s’estructuren en columnes separades per un caràcter determinat (generalment el separador és una coma o un punt i coma per als CSV, i tabulació per als TSV). Totes les files tenen els mateixos camps, i al final de cada fila hi ha un salt de línia. A més, es disposa de les opcions d’exportació "CSV for Excel" i "CSV for Excel" (Europa). Aquestes opcions estan formatades de manera que, quan s’obren amb MS Excel, el programa interpreta el separador i mostra les columnes de manera separada, facilitant-ne la lectura. Més informació a http://tools.ietf.org/html/rfc4180.

* JSON
Format lleuger d’intercanvi de dades entre aplicacions informàtiques. Ofereix senzillesa a les màquines en la generació i interpretació de les dades. Està basat en un subconjunt del llenguatge de programació JavaScript, adequat per a la programació per part del client. Més informació a http://json.org/json-es.html.

* XML
Format obert que permet representar les dades de forma estructurada i jeràrquica mitjançant etiquetes. És un llenguatge dissenyat per facilitar la reutilització de les dades mitjançant altres programes o aplicacions. Més informació a https://www.w3.org/TR/2006/REC-xml11-20060816/.

* RDF-XML
RDF és una especificació per estructurar les dades en tripletes, en la forma subjecte-atribut-valor, que permet incorporar informació semàntica a les dades. RDF és una especificació abstracta i no es limita a un format concret. En la plataforma de dades obertes, es poden descarregar fitxers RDF serialitzats com a XML. Més informació a https://www.w3.org/TR/REC-rdf-syntax/.

* RSS
És un format del llenguatge XML que permet la distribució de continguts de pàgines web. Facilita la publicació d’informació actualitzada als usuaris subscrits a la font RSS sense necessitat d’usar un navegador, utilitzant un programari especialitzat en aquest format.

 En el cas de datasets que contenen dades geogràfiques, addicionalment als formats esmentats anteriorment, també es poden exportar en els formats específics següents per a la representació de dades geogràfiques:

* KML/KMZ
El format KML és una notació específica d'XML per a la representació de dades geogràfiques. Els fitxers KML permeten representar diverses geometries (punts, polígons, models 3D, etc.) expressades en latitud, longitud i, opcionalment, altitud. Es poden distribuir també agrupats en un ZIP (anomenat KMZ) i poden contenir altres recursos, com ara descripcions o imatges associades als elements geogràfics. Es poden obrir i processar amb programari que implementi KML i KMZ, com és el cas de Google Earth. Més informació a https://developers.google.com/kml/documentation/kmlreference.

* SHP
Shapefile és un format propietari de dades espacials d’ús molt estès per a l’intercanvi d’informació geogràfica entre sistemes d’informació geogràfica (SIG). És un format vectorial d’emmagatzematge digital on es guarda la localització d’elements geogràfics i els atributs associats, però sense capacitat per emmagatzemar informació topològica. El generen diversos fitxers (mínim tres) i té tres tipus d’extensions: .shp, .shx i .dbf. Més informació a http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf.

* GeoJSON
El format GeoJSON és un format obert per representar diferents estructures de dades geogràfiques conjuntament amb atributs no geogràfics, basant-se en el format JSON. Més informació a http://geojson.org/geojson-spec.html.

* Original
Aquesta opció permet baixar el fitxer en el mateix format en què va ser pujat a la plataforma de dades obertes.

## Què es pot fer amb aquestes dades?

Les dades obertes es poden utilitzar per a qualsevol tipus de finalitat: per exemple, permeten consultar informació sobre diferents temàtiques i construir aplicacions, en especial programari i formes de visualització, que utilitzen la informació lliure com a font.

Entre altres usos, es poden fer estudis estadístics socioeconòmics, que, a posteriori, seran utilitzats per moltes empreses amb propòsits d’anàlisi de mercats i avaluació de risc comercial, màrqueting i vendes.

Els periodistes de dades empren les dades obertes com a matèria primera en comptes d’altres fonts d’informació, i treballen en l’anàlisi crítica de la informació, amb l’objectiu d’oferir representacions de la informació comprensibles i molt intuïtives.


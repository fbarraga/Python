
## Introducció

Extensible Markup Language, comunment conegut com XML és un llenguatge dissenyat específicament per ser fàcil d'interpretar tant per humans com per ordinadors en conjunt. 

El llenguatge defineix un conjunt de regles que s'utilitzen per codificar un document en un format específic. 

En general, el procés de lectura de les dades d'un fitxer XML i l'anàlisi dels seus components lògics es coneix com a Anàlisi. Per tant, quan ens referim a la lectura d'un fitxer xml ens referim a l'anàlisi del document XML. 


## Instal·lació de llibreries necessaries

Hi ha dues biblioteques que es podrien utilitzar amb el propòsit d'analitzar xml. Són:
1.	BeautifulSoup utilitzat al costat de l'analitzador xml lxml
2.	Biblioteca Elementtree.


Ús de BeautifulSoup juntament amb l'analitzador lxml

Amb el propòsit de llegir i escriure el fitxer xml, estaríem utilitzant una biblioteca Python anomenada BeautifulSoup. Per instal·lar la biblioteca, escriviu l'ordre següent al terminal.

`pip install beautifulsoup4`

Beautiful Soup admet l'analitzador HTML inclòs a la biblioteca estàndard de Python, però també admet una sèrie d'analitzadors Python de tercers. Un és l'analitzador lxml (utilitzat per analitzar documents XML/HTML). lxml es podria instal·lar executant l'ordre següent al processador d'ordres del vostre sistema operatiu:

`pip install lxml`

## Lectura de fitxers XML amb BeautifulSoup

Lectura de dades d'un fitxer XML
Es requereixen dos passos per analitzar un fitxer xml:
1.	Cerca d'etiquetes
2.	Extracció d'etiquetes

## Escriptura de fitxers XML amb BeautifulSoup

Escriure un fitxer xml és un procés primitiu, raó per la qual això és el fet que els fitxers xml no estan codificats d'una manera especial. La modificació de seccions d'un document xml requereix que s'analitzi a través d'ell al principi. E



## Lectura de fitxers XML amb ElementTree

Ús d'Elementree
El mòdul Elementree ens proporciona una gran quantitat d'eines per manipular fitxers XML. La millor part d'això és la seva inclusió a la biblioteca integrada estàndard de Python. Per tant, no cal instal·lar cap mòdul extern per al propòsit. Com que el xmlformat és un format de dades inherentment jeràrquic, és molt més fàcil representar-lo per un arbre. El mòdul proporciona ElementTree proporciona mètodes per representar tot el document XML com un sol arbre. 

Per llegir un fitxer XML utilitzant ElementTree, en primer lloc, importem la classe ElementTree que es troba dins de la biblioteca XML, sota el nom ET (common convension). A continuació, passeu el nom del fitxer xml al mètode ElementTree.parse(), per habilitar l'anàlisi del nostre fitxer xml. A continuació, obteniu l'arrel (etiqueta principal) del nostre fitxer xml mitjançant getroot(). A continuació, es mostrarà (imprès) l'etiqueta arrel del nostre fitxer xml (de manera no explícita). A continuació, mostreu els atributs de la subetiqueta de la nostra etiqueta principal utilitzant root[0].attrib. root[0] per a la primera etiqueta d'arrel pare i attrib per obtenir els seus atributs. A continuació, mostrem el text inclòs dins de la 1a subetiqueta de la 5a subetiqueta de l'arrel de l'etiqueta.



## Escriptura de fitxers XML amb ElementTree

1).-En primer lloc, creem una etiqueta arrel (pare) amb el nom d'escacs utilitzant l'ordre ET. Element('escacs'). Totes les etiquetes caurien per sota d'aquesta etiqueta, és a dir, un cop definida una etiqueta arrel, es podrien crear altres subelements a sota. A continuació, vam crear un subtag/subelement anomenat Obertura dins de l'etiqueta d'escacs utilitzant l'ordre ET. SubElement(). 
2).-A continuació, hem creat dues subetiquetes més que es troben a sota de l'etiqueta Obertura anomenada E4 i D4. 
3).-A continuació, hem afegit atributs a les  etiquetes E4 i D4 mitjançant set() que és un mètode que es troba dins de SubElement(), que s'utilitza per definir atributs a una etiqueta. 
4).-A continuació, hem afegit text entre les  etiquetes E4 i D4 utilitzant el text de l'atribut que es troba dins de la funció SubElement. Al final vam convertir el tipus de dades dels continguts que estàvem creant des de 'xml.etree.ElementTree.Element' a objecte de bytes, utilitzant l'ordre ET.tostring() (tot i que el nom de la funció és tostring() en determinades implementacions converteix el tipus de dades a 'bytes' en lloc de 'str'). 
5).-Finalment, hem rentat les dades a un fitxer anomenat gameofsquares.xml que és una obertura en mode 'wb' per permetre escriure-hi dades binàries. Al final, vam guardar les dades al nostre fitxer.



***
[Index](../../../README.md)

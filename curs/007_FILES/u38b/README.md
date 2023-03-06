
## Introducció

E**X**tensible **M**arkup **L**anguage, comunment conegut com XML és un llenguatge dissenyat específicament per ser fàcil d'interpretar tant per humans com per ordinadors en conjunt. 

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


El mòdul Elementree ens proporciona una gran quantitat d'eines per manipular fitxers XML. La millor part d'això és la seva inclusió a la biblioteca integrada estàndard de Python. Per tant, no cal instal·lar cap mòdul extern per al propòsit. Com que el xmlformat és un format de dades inherentment jeràrquic, és molt més fàcil representar-lo per un arbre. El mòdul proporciona ElementTree proporciona mètodes per representar tot el document XML com un sol arbre. 

Per llegir un fitxer XML utilitzant ElementTree seguirem aquestes passes:
1. Importem la classe ElementTree que es troba dins de la biblioteca XML, sota el nom ET (common convension).
2. Passem el nom del fitxer xml al mètode ElementTree.parse(), per habilitar l'anàlisi del nostre fitxer xml. 
3. Obtenir l'arrel (etiqueta principal) del nostre fitxer xml mitjançant getroot(). 
4. Es mostrarà (imprès) l'etiqueta arrel del nostre fitxer xml (de manera no explícita). 
5. Mostreu els atributs de la subetiqueta de la nostra etiqueta principal utilitzant root[0].attrib. root[0] per a la primera etiqueta d'arrel pare i attrib per obtenir els seus atributs.
6. Mostrar el text inclòs dins de la 1a subetiqueta de la 5a subetiqueta de l'arrel de l'etiqueta.

```xml
<?xml version="1.0" encoding="utf-8"?>
<saranghe>
    <child name="Frank" test="0">
     FRANK lives EVERYONE
    </child>
    <unique>
     Add a video URL here
    </unique>
    <child name="Texas" test="1">
     Exclusively
    </child>
    <unique>
     Add a workbook URL here
    </unique>
    <data>
     Add the content of your article here
        <family>
        Add the font of your text here
        </family>
        <size>
        Add the font size of your text here
        </size>
    </data>
</saranghe>
```


```python
# importem el mòdul element tree
# sota l'alias ET
import xml.etree.ElementTree as ET

# Passem el path del fitxers xml
# xper poder inciiar el proces de parsing

tree = ET.parse('../data/dict.xml')

# Agafem el tag de pare del document xml
root = tree.getroot()

# Imprimim el root (parent) tag
# del document xmls, along with
# its memory location
print(root)

# Imprimim els atributs del primer tag des
# del pare
print(root[0].attrib)

# Imprimim el text contingut dintre
# del primer subtage en el 5e tag des del
# pare

print(root[5][0].text)
```


## Escriptura de fitxers XML amb ElementTree

1. En primer lloc, creem una etiqueta arrel (pare) amb el nom d'escacs utilitzant l'ordre ET. Element('escacs'). Totes les etiquetes caurien per sota d'aquesta etiqueta, és a dir, un cop definida una etiqueta arrel, es podrien crear altres subelements a sota. A continuació, vam crear un subtag/subelement anomenat Obertura dins de l'etiqueta d'escacs utilitzant l'ordre ET. SubElement(). 
2. A continuació, hem creat dues subetiquetes més que es troben a sota de l'etiqueta Obertura anomenada E4 i D4. 
3. A continuació, hem afegit atributs a les  etiquetes E4 i D4 mitjançant set() que és un mètode que es troba dins de SubElement(), que s'utilitza per definir atributs a una etiqueta. 
4. A continuació, hem afegit text entre les  etiquetes E4 i D4 utilitzant el text de l'atribut que es troba dins de la funció SubElement. Al final vam convertir el tipus de dades dels continguts que estàvem creant des de 'xml.etree.ElementTree.Element' a objecte de bytes, utilitzant l'ordre ET.tostring() (tot i que el nom de la funció és tostring() en determinades implementacions converteix el tipus de dades a 'bytes' en lloc de 'str'). 
5. Finalment, hem rentat les dades a un fitxer anomenat gameofsquares.xml que és una obertura en mode 'wb' per permetre escriure-hi dades binàries. Al final, vam guardar les dades al nostre fitxer.

```python
import xml.etree.ElementTree as ET

# This is the parent (root) tag
# onto which other tags would be
# created
data = ET.Element('chess')

# Adding a subtag named `Opening`
# inside our root tag
element1 = ET.SubElement(data, 'Opening')

# Adding subtags under the `Opening`
# subtag
s_elem1 = ET.SubElement(element1, 'E4')
s_elem2 = ET.SubElement(element1, 'D4')

# Adding attributes to the tags under
# `items`
s_elem1.set('type', 'Accepted')
s_elem2.set('type', 'Declined')

# Adding text between the `E4` and `D5`
# subtag
s_elem1.text = "King's Gambit Accepted"
s_elem2.text = "Queen's Gambit Declined"

# Converting the xml data to byte object,
# for allowing flushing data to file
# stream
b_xml = ET.tostring(data)

# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open("GFG.xml", "wb") as f:
	f.write(b_xml)

```

***
[Index](../../../README.md)

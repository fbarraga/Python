import sys
import xml.etree.ElementTree as ET

idioma = sys.argv[1]
nom_fitxer = "missatges.xml"
arbre = ET.parse(nom_fitxer)
arrel = arbre.getroot()
for fill in arrel:
 if (fill.attrib.get('salutacio')):
    missatge_salutacio = fill.attrib.get('salutacio')
 if idioma == missatge_salutacio: s = fill.text
 if (fill.attrib.get('comiat')):
    missatge_comiat = fill.attrib.get('comiat')
 if idioma == missatge_comiat: c = fill.text
print(f"{s} ... {c}")

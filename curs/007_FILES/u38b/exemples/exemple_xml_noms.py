import xml.etree.ElementTree as ET
nom_fitxer = "persones.xml"
arbre = ET.parse(nom_fitxer)
arrel = arbre.getroot()
for per in arrel.findall('persona'):
 per_nom = per.find('nom').text
 per_cog = per.find('cognoms').text
 nom_complert = f"{per_cog}, {per_nom}"
 print(nom_complert)

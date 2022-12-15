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

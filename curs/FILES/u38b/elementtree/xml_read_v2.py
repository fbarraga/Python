# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('../data/dict.xml')

# getting the parent tag of
# the xml document
root = tree.getroot()

# printing the root (parent) tag
# of the xml document, along with
# its memory location
print(root)

# printing the attributes of the
# first tag from the parent
print(root[0].attrib)

# printing the text contained within
# first subtag of the 5th tag from
# the parent
print(root[5][0].text)

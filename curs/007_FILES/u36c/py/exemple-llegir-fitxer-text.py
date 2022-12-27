import sys

nom_fitxer = sys.argv[1]
fitxer = open(nom_fitxer)
linies = fitxer.readlines()
print(linies)
print()
fitxer.close()
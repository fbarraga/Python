import csv

fitxer = open("exemple1.csv")
contingut = csv.reader(fitxer)
list(contingut)

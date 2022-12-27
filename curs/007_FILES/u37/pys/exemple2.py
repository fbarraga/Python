import csv

fitxer = open("exemple2.csv")
contingut = csv.reader(fitxer,quotechar='"')
for row in contingut:
   print(row)
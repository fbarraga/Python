import csv

fitxer = open("exemple3.csv","w")
contingut = csv.writer(fitxer)
contingut.writerow(['4/5/2015 13:34', 'Apples', '73'])
contingut.writerows(['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14'])
fitxer.close()
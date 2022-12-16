# Serialització

## Procés de serialització

El procés de serialització consisteix a transformar un objecte determinat en un text a partir d'un llenguatge específic, per ser emmagatzemat o bé transferit i, finalment, restablert a l'objecte original.
Per exemple, desar una llista de Python en un arxiu de text o base de dades, i després carregar quan sigui necessari. Formats comuns entre els diferents llenguatges de programació inclouen CSV, XML i JSON

# Gestionar fitxers CSV

## Mòdul CSV

El mòdul [csv](https://docs.python.org/3.4/library/csv.html) ens permet treballar amb fitxers csv.
Un fitxer CSV (comma-separated values)  es un tipus de document en format obert senzill per representar dades en format de taula, en la que les columnes es separen per comes(o per un altre caràcter).

## Llegir fitxers CSV

Per llegir un fitxer CSV utilitzem la funció `reader()`:

	>>> import csv
	>>> fitxer = open("exemple1.csv")
	>>> contingut = csv.reader(fitxer)
	>>> list(contingut)
	[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
	>>> list(contingut)
	[]
	>>> fitxer.close()

Podem guardar la llista obtinguda en una variable i accedir amb ella indicant fila i columna.

	...
	>>> dades = list(contingut)
	>>> dades[0][0]
	'4/5/2015 13:34'
	>>> dades[1][1]
	'Cherries'
	>>> dades[2][2]
	'14'

Per suposat podem recorrer el resultat:

	...
	>>> for row in contingut:
		print("Fila "+str(contingut.line_num)+" "+str(row))	

	Fila 1 ['4/5/2015 13:34', 'Apples', '73']
	Fila 2 ['4/5/2015 3:41', 'Cherries', '85']
	Fila 3 ['4/6/2015 12:46', 'Pears', '14']
	Fila 4 ['4/8/2015 8:59', 'Oranges', '52']
	Fila 5 ['4/10/2015 2:07', 'Apples', '152']
	Fila 6 ['4/10/2015 18:10', 'Bananas', '23']
	Fila 7 ['4/10/2015 2:40', 'Strawberries', '98']

Veiem un altre exemple una mica més complexe:

	>>> import csv
	>>> fitxer = open("exemple2.csv")
	>>> contingut = csv.reader(fitxer,quotechar='"')
	>>> for row in contingut:
	...   print(row)
	... 
	['Año', 'Marca', 'Modelo', 'Descripción', 'Precio']
	['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
	['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00']
	['1999', 'Chevy', 'Venture "Extended Edition, Very Large"', '', '5000.00']
	['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL!\nair, moon roof, loaded', '4799.00']

## Escriure fitxers CSV

	>>> import csv
	>>> fitxer = open("exemple3.csv","w")
	>>> contingut = csv.writer(fitxer)
	>>> contingut.writerow(['4/5/2015 13:34', 'Apples', '73'])
	>>> contingut.writerows(['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14'])
	>>> fitxer.close()

	$ cat exemple3.csv
	4/5/2015 13:34,Apples,73
	4/5/2015 3:41,Cherries,85
	4/6/2015 12:46,Pears,14


***
[Index](../../../README.md)

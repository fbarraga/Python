
# Gestionar fitxers CSV

## Mòdul CSV

El mòdul [csv](https://docs.python.org/3.4/library/csv.html) ens permet treballar amb fitxers csv.
Un fitxer CSV (comma-separated values)  es un tipus de document en format obert senzill per representar dades en format de taula, en la que les columnes es separen per comes(o per un altre caràcter).

## Llegir fitxers CSV

Per llegir un fitxer CSV utilitzem la funció `reader()`:

	>>> import csv
	>>>
	>>> fitxer = open("exemple1.csv")
	>>> contingut = csv.reader(fitxer)
	>>> list(contingut)

	[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
	>>> list(contingut)
	[]
	>>> fitxer.close()

Quan fem el csv.reader podem especificar quin es el delimitador que separa els caps. A vegades ens trobarem que enlloc d'utilitzar la ',' s'utilitza el ';'

	>>>    csv_reader = csv.reader(csv_file, delimiter=';')

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
	>>>
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


També podem llegir el fitxer i posar-ho en un diccionari mitjançant el mètode *DictReader*:

	>>> import csv
	>>>
	>>> with open('employee_birthday.txt', mode='r') as csv_file:
	>>>     csv_reader = csv.DictReader(csv_file)
	>>>     line_count = 0
	>>>     for row in csv_reader:
	>>>       if line_count == 0:
	>>>            print(f'Column names are {", ".join(row)}')
	>>>            line_count += 1
	>>>        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row>>>>>>["birthday month"]}.')
	>>>        line_count += 1
	>>>    print(f'Processed {line_count} lines.')	

## Escriure fitxers CSV

	>>> import csv
	>>>
	>>> fitxer = open("exemple3.csv","w")
	>>> contingut = csv.writer(fitxer)
	>>> contingut.writerow(['4/5/2015 13:34', 'Apples', '73'])
	>>> contingut.writerows(['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14'])
	>>> fitxer.close()

	$ cat exemple3.csv
	4/5/2015 13:34,Apples,73
	4/5/2015 3:41,Cherries,85
	4/6/2015 12:46,Pears,14

Quan fem el csv.writer podem especificar també les  opcions delimiter, quotechar y quoting. El següent exemple faria que el separador dels camps fos la coma, les cadenes estiguessin entre cometes.
 	
	>>> contingut = csv.writer(fitxer,delimiter=',', quotechar='"')


També ho podem escriure directament des d'un diccionari a través del mètode *DictWriter*:

	>>> import csv

	>>> with open('employee_file2.csv', mode='w') as csv_file:
	>>>     fieldnames = ['emp_name', 'dept', 'birth_month']
	>>>     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    >>> writer.writeheader()
    >>> writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    >>> writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


Pots trobar més informació en aquest link de [Real Python](https://realpython.com/python-csv/)

***
[Index](../../../README.md)

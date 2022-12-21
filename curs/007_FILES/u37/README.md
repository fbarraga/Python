
# Gestionar fitxers CSV

## Mòdul CSV

El mòdul [csv](https://docs.python.org/3.4/library/csv.html) ens permet treballar amb fitxers csv.
Un fitxer CSV (comma-separated values)  es un tipus de document en format obert senzill per representar dades en format de taula, en la que les columnes es separen per comes(o per un altre caràcter).

### Llegir fitxers CSV

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

Quan fem el csv.reader podem especificar quin es el delimitador que separa els camps. A vegades ens trobarem que enlloc d'utilitzar el delimitador ',' s'utilitza un altre per exemple ';'

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

### Escriure fitxers CSV

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

Quan fem el csv.writer podem especificar també les opcions *delimiter*, *quotechar* y *quoting*. El següent exemple faria que el separador dels camps fos la coma, les cadenes estiguessin entre cometes.
 	
	>>> contingut = csv.writer(fitxer,delimiter=',', quotechar='"')


També ho podem escriure directament des d'un diccionari a través del mètode *DictWriter*:

	>>> import csv

	>>> with open('employee_file2.csv', mode='w') as csv_file:
	>>>     fieldnames = ['emp_name', 'dept', 'birth_month']
	>>>     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    >>> writer.writeheader()
    >>> writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    >>> writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


## Mòdul Pandas

La biblioteca CSV de Python no és l'únic mètode per treballar amb fitxers CSV també és possible amb [pandas](http://pandas.pydata.org/index.html). És molt recomanable utilitzar aquest mòdul (temes de Datascience i ML) si teniu moltes dades per analitzar.

Pandas és una biblioteca Python de codi obert que proporciona eines d'anàlisi de dades d'alt rendiment i estructures de dades fàcils d'utilitzar. *Pandas* està disponible per a totes les instal·lacions de Python, però és una part clau de la distribució Anaconda i funciona molt bé als quaderns de Jupyter per compartir dades, codi, resultats d'anàlisi, visualitzacions i text narratiu.

Primer de tot haurem d'instal·lar el mòdul:

	$ pip install pandas

### Lectura amb pandas

Llegir el CSV en un [Pandas DataFrame](https://realpython.com/pandas-dataframe/) és ràpid i senzill:


	>>> import pandas
	>>> df = pandas.read_csv('hrdata.csv')
	>>> print(df)

Tres línies de codi, i només una d'elles fa el treball real. pandas.read_csv() obre, analitza i llegeix el fitxer CSV proporcionat i emmagatzema les dades en un DataFrame. La impressió del DataFrame dóna com a resultat la sortida següent:


|            Name  | Hire Date|  Salary | Sick Days remaining |
|------------------|----------|---------|---------------------|				 
|0 | Graham Chapman|  03/15/14|  50000.0|                   10|
|1 |    John Cleese|  06/01/15|  65000.0|                    8|
|2 |      Eric Idle|  05/12/14|  45000.0|                   10|
|3 |    Terry Jones|  11/01/13|  70000.0|                    3|
|4 |  Terry Gilliam|  08/12/14|  48000.0|                    7|
|5 |  Michael Palin|  05/23/13|  66000.0|                    8|

Aquí hi ha alguns punts que val la pena destacar:

1. Primer, els pandas van reconèixer que la primera línia del CSV contenia noms de columnes i els van utilitzar automàticament. 
2. Tanmateix, els pandas també utilitzen índexs enters de base zero al DataFrame. Això és perquè no li vam dir quin hauria de ser el nostre índex.
3. A més, si mireu els tipus de dades de les nostres columnes , veureu que Pandas ha convertit correctament les columnes de Salari i Dies de malaltia restants en números, però la columna Data de contractació continua sent una cadena. Això es confirma fàcilment en mode interactiu:

		>>> print(type(df['Hire Date'][0]))
		<class 'str'>


Per utilitzar una columna diferent com a índex DataFrame, afegiu el paràmetre opcional index_col:

		>>> import pandas
		>>> df = pandas.read_csv('hrdata.csv', index_col='Name')
		>>> print(df)

i la sortida ens quedaria:

|Name			 |Hire Date|   Salary | Sick Days remaining|
|----------------|---------|----------|--------------------|
|Graham Chapman  |03/15/14 |50000.0   |                10  |
|John Cleese     |06/01/15 |65000.0   |                 8  |
|Eric Idle       |05/12/14 |45000.0   |                10  |
|Terry Jones     |11/01/13 |70000.0   |                 3  |
|Terry Gilliam   |08/12/14 |48000.0   |                 7  |
|Michael Palin   |05/23/13 |66000.0   |                 8  |


A continuació, arreglem el tipus de dades del camp Data de contractació. Podeu forçar els pandas a llegir les dades com a data amb el paràmetre opcional parse_dates, que es defineix com una llista de noms de columnes per tractar-los com a dates:

	>>> import pandas
	>>> df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
	>>> print(df)

|      Name     | Hire Date |  Salary | Sick Days remaining|
|---------------|-----------|---------|--------------------|
|Graham Chapman |2014-03-15 | 50000.0 |                  10|
|John Cleese    |2015-06-01 | 65000.0 |                   8|
|Eric Idle      |2014-05-12 | 45000.0 |                  10|
|Terry Jones    |2013-11-01 | 70000.0 |                   3|
|Terry Gilliam  |2014-08-12 | 48000.0 |                   7|
|Michael Palin  |2013-05-23 | 66000.0 |                   8|

Ara la data està formatejada correctament, podem veure que ara és de tipus data sii ho consultem:

	>>> print(type(df['Hire Date'][0]))
	<class 'pandas._libs.tslibs.timestamps.Timestamp'>


Si els fitxers CSV no tenen noms de columnes a la primera línia, podeu utilitzar el paràmetre opcional de noms per proporcionar una llista de noms de columnes. També podeu utilitzar-lo si voleu substituir els noms de columnes proporcionats a la primera línia. En aquest cas, també heu de dir a pandas.read_csv() que ignori els noms de columnes existents mitjançant el paràmetre opcional header=0:

	>>> import pandas
	>>> df = pandas.read_csv('hrdata.csv', 
	>>>            index_col='Employee', 
	>>>            parse_dates=['Hired'], 
	>>>            header=0, 
	>>>            names=['Employee', 'Hired','Salary', 'Sick Days'])
	>>> print(df)




Pots trobar més informació en aquest link de [Real Python](https://realpython.com/python-csv/)

***
[Index](../../../README.md)

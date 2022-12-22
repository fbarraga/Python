# Mòduls estàndards: mòduls de hora i dates

## Mòdul time

El temps es mesurat com un número real que representa els segons transcorreguts des del 1 de gener de 1970. Per lo tanto es impossible representar dates anteriors a aquesta data i posteriors a 2038	(tamany del float en la llibreria C (32 bits)).

	>>> import time
	>>> time.time()
	1488619835.7858684

Per convertir la quantitat de segons a la data i hora local:

	>>> tiempo = time.time()
	>>> time.localtime(tiempo)
	time.struct_time(tm_year=2017, tm_mon=3, tm_mday=4, tm_hour=10, tm_min=37, tm_sec=19, tm_wday=5, tm_yday=63, tm_isdst=0)

Si volem obtenir la data i hora actual:

	>>> time.localtime()
	time.struct_time(tm_year=2017, tm_mon=3, tm_mday=4, tm_hour=10, tm_min=37, tm_sec=30, tm_wday=5, tm_yday=63, tm_isdst=0)

Ens retorna una estructura de la qual podem accedir a varis camps.

	>>> tiempo = time.localtime()
	>>> tiempo.tm_year
	2017

Podem representar la data i hora com una cadena:

	>>> time.asctime()
	'Sat Mar  4 10:41:41 2017'
	>>> time.asctime(tiempo)
	'Sat Mar  4 10:39:21 2017'

O amb un determinat format:

	>>> time.strftime('%d/%m/%Y %H:%M:%S')
	'04/03/2017 10:44:52'
	>>> time.strftime('%d/%m/%Y %H:%M:%S',tiempo)
	'04/03/2017 10:39:21'

# Mòdulo datetime

Els mòduls datetime i calendar amplien les possibilitats del mòdul time que dona les funcions per manipular expresions de temps.

	>>> from datetime import datetime
	>>> datetime.now()
	datetime.datetime(2017, 3, 4, 10, 52, 12, 859564)
	>>> datetime.now().day,datetime.now().month,datetime.now().year
	(4, 3, 2017)

Per comparar dates i hores:

	>>> from datetime import datetime, date, time, timedelta
	>>> hora1 = time(10,5,0)
	>>> hora2 = time(23,15,0)
	>>> hora1>hora2
	False

	>>> fecha1=date.today()
	>>> fecha2=fecha1+timedelta(days=2)
	>>> fecha1
	datetime.date(2017, 3, 4)
	>>> fecha2
	datetime.date(2017, 3, 6)
	>>> fecha1<fecha2
	True

Podem imprimir aplicant un format:

	>>> fecha1.strftime("%d/%m/%Y")
	'04/03/2017'
	>>> hora1.strftime("%H:%M:%S")
	'10:05:00'

Podem convertir una cadena a un `datetime`:

	>>> tiempo = datetime.strptime("12/10/2017","%d/%m/%Y")

I podem treballar amb quantitats (segons, minuts, hores, dies, setmanes,...) amb `timedelta`:

	>>> hoy = date.today()
	>>> ayer = hoy - timedelta(days=1)
	>>> diferencia = hoy - ayer
	>>> diferencia
	datetime.timedelta(1)

	>>> fecha1=datetime.now()
	>>> fecha2=datetime(1995,10,12,12,23,33)
	>>> diferencia=fecha1-fecha2
	>>> diferencia
	datetime.timedelta(7813, 81981, 333199)

# Mòdul calendar

Podem obtenir el calendario del mes actual:

	>>> año = date.today().year 
	>>> mes = date.today().month
	>>> calendario_mes = calendar.month(año, mes)
	>>> print(calendario_mes)
	     March 2017
	Mo Tu We Th Fr Sa Su
	       1  2  3  4  5
	 6  7  8  9 10 11 12
	13 14 15 16 17 18 19
	20 21 22 23 24 25 26
	27 28 29 30 31

I per mostrar tots els mesos de l'any:

	>>> print(calendar.TextCalendar(calendar.MONDAY).formatyear(2017,2, 1, 1, 2))


***
[Index](../../../README.md)

# Estructura del programa

* Un programa python està format por instruccions que acaben en un caràcter de "salt de línia". 
* El punt i coma “;” es pot utilitzar per separar varies sentencies en una mateixa linia, pero no es recomana el seu ús.
* Una linia comença en la darrera posició, si tenim instruccions dintre de un bloc d'una estructura de control de flux s'haurà de fer una indentació.
* La identació es pot fer amb espais i tabulacions però ambdos tipus no es poden barrejar. Es recomanda  utilitzar 4 espais. ([Guía d'estil de python](https://www.python.org/dev/peps/pep-0008/))
* La barra invertida "\\" al final de línia s'utilitza per dividir una linea molt llarga en dos o més linies.
* Les expresions entre parèntesis "()", claus "{}" y corxets "[]" separats per comes "," es poden escriure ocupant varies linies.
* Quan el bloc a aplicar la sangria només ocupa una linia aquesta pot esciure's després dels dos punts.

## Comentaris

Els comentaris s'utilitzen per:
* Explicar codi Python
* Fer el codi més llegible
* Prevenir l'execució quan estem fent proves

S'utiliza el caràcter `#` per indicar els comentaris. 

Exemple de comentari amb una línia:

	#This is a comment
	print("Hello, World!")

	print("Hello, World!") #This is a comment

Exemple de comentari amb varies linies `###`

	"""
	This is a comment
	written in
	more than just one line
	"""
	print("Hello, World!")


## Paraules reservades

	False      class      finally    is         return
	None       continue   for        lambda     try
	True       def        from       nonlocal   while
	and        del        global     not        with
	as         elif       if         or         yield
	assert     else       import     pass
	break      except     in         raise

## Exemple

	#!/usr/bin/env python	

	# Sangrat amb 4 espais	

	edad = 23
	if edad > =18:
	   print('Es major')  
	else:
	   print('Es menor')	

	# Cada bloc de instruccions dintre d'una estructura de control
	# ha d'estar tabulada	

	if num >=0:
		while num<10:
			print (num)
			num = num +1	

	# El punt i coma “;” es pot utilitzar per separar varies sentències 
	# en una mateixa linia, però no s'aconsella el seu ús.	

	edat = 15; print(edat)	

	# Quan el bloc on aplicar sangria només ocupa una linia 
	# aquesta es pot escriure després dels dos punts:   	

	if blau: print('Cel')	

	# La barra invertida “\” permet escriure una linia de
	# codi massa extensa en varies linees:	

	if condicio1 and condicio2 and condicio3 and \  
	    condicio4 and condicio5:	

	# Las expresions entre parèntesis, claus o corxets poden 
	# ocupar varies linies:	

	dies = ['dilluns', 'dimarts', 'dimecres', 'dijous',
	        'divendres', 'dissabte', 'diumenge'] 

***
[Index](../../../README.md)

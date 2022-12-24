# Exercicis de diccionaris

1. Escriu un programa que llegeixi una cadena i retorni un diccionari amb la quantitat d'aparicions de cada paraula a la cadena. Per exemple, si rep "Qué lindo día que hace hoy" haurà de  retornar: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1

2. Tenim guardat en un diccionari els codis morse coresponents a cada caràcter. Escriu un programa que llegeixi una paraula i la mostri utilitzant el codi morse.

		>>> codigo = {
	    	'A': '.-',     'B': '-...',    'C': '-.-.',
	    	'D': '-..',    'E': '.',       'F': '..-.',
	    	'G': '--.',    'H': '....',    'I': '..',
	    	'J': '.---',   'K': '-.-',     'L': '.-..',
	    	'M': '--',     'N': '-.',      'O': '---',
	    	'P': '.--.',   'Q': '--.-',    'R': '.-.',
	    	'S': '...',    'T': '-',       'U': '..-',
	    	'V': '...-',   'W': '.--',     'X': '-..-',
	    	'Y': '-.--',   'Z': '--..',    '1': '.----',
	    	'2': '..---',  '3': '...--',   '4': '....-',
	    	'5': '.....',  '6': '-....',   '7': '--...',
	    	'8': '---..',  '9': '----.',   '0': '-----',
	    	'.': '.-.-.-', ',': '--..--',  ':': '---...',
	    	';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
	    	'"': '.-..-.', "'": '.----.',  '+': '.-.-.',
	    	'-': '-....-', '/': '-..-.',   '=': '-...-',
	    	'_': '..--.-', '$': '...-..-', '@': '.--.-.',
	    	'&': '.-...',  '(': '-.--.',   ')': '-.--.-'
		>>>	}		


3. Continuant amb el programa: ara feu que el programa demani un codi morse separat per espais i retorni la cadena corresponent.

4. Crea un diccionari que contingui com a clau el nom d'una persona i coma valor una llista amb totes les seves aficions.  Desenvolupa un programa que agregi aficions a la persona:
    * Si la persona no existeix l'agregui al diccionari amb una lista que conté un sol element.
    * Si la persona existeix i l'afició existeix en la llista, no tingui cap efecte.
    * Si la persona existeix i l'afició no existeix en la llista, agregui l'afició a la llista.
	* Es deixa de demanar persones quan introduim el caràcter "*".

5. La funció email_list rep un diccionari, que conté noms de domini com a claus i una llista d'usuaris com a valors. Crear un programa per generar una llista que contingui adreces de correu electrònic completes (p. ex., diana.prince@gmail.com).

		>>> def email_list(domains):
		>>> ...

		>>>print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


6. La funció groups_per_user rep un diccionari, que conté noms de grups amb la llista d'usuaris. Els usuaris poden pertànyer a diversos grups. Crear un programa per tornar un diccionari amb els usuaris com a claus i una llista dels seus grups com a valors.

		>>> def groups_per_user(group_dictionary):
		>>> ...

		>>> print(groups_per_user({"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"] }))


7. El mètode dict.update actualitza un diccionari amb els elements procedents de l'altre diccionari, de manera que se substitueixen les entrades existents i s'afegeixen noves entrades. Quin és el contingut del diccionari "armari" al final del codi següent?

		>>> wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
		>>> new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
		>>> wardrobe.update(new_items)

Opcions:

	a. {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
	b. {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
	c. {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black', 'white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
	d. {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

8. La funció suma_preus retorna el preu total de tots els queviures del diccionari. Fes un programa per realitzar aquesta funció.

		>>> def suma_preus(basket):
		>>> ...

		>>> super = {"bananas": 1.56, "pomes": 2.50, "taronges": 0.99, "pa": 4.59, "cafe": 6.99, "llet": 3.39, "ous": 2.98, "formatge": 5.44}
		>>> print(suma_preus(super)) # Ha d'imprimir 28.44


9. Realitza el codi per iterar a través de les claus i valors del diccionari car_prices, imprimint informació sobre cadascun.

		>>> def car_listing(car_prices):
		>>> ...
	
		>>> print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

10. Pere i Marta organitzen una festa. Van enviar invitacions als seus amics i cadascun va recopilar les respostes en diccionaris de python, amb els noms dels seus amics i quants convidats porta cada amic. Cada diccionari és una llista parcial, però la llista de Marta té informació més actualitzada sobre el nombre de convidats. Crear un programa per combinar els dos diccionaris en un sol, amb cada amic llistat només una vegada, i el nombre de convidats del diccionari de Marta té prioritat, si hi ha un nom repetit als dos diccionaris. A continuació, imprimiu el diccionari resultant.

		>>> def combina_invitats(guests1, guests2):
		>>> ...

		>>> Pere_invitats = { "Joan":2, "Maite":3, "David":1, "Josep":3, "Carla":2, "Terry":1, "Robert":4}
		>>> Marta_invitats = { "David":4, "Laia":1, "Robert":2, "Joan":1, "Mar":3, "Erik":5}

		>>> print(combine_invitats(Marta_invitats, Pere_invitats))

***
[Index](../../../README.md)

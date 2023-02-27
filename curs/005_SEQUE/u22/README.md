
# Introducció a Python
## Activitat 4: Treballem amb llistes

1. Realitzar un programa que llegeix per teclat números i els guarda en una llista, el procés finalitza quan introduim un número negatiu. Mostra el màxim dels números que hem guardat a la llista, i després mostra els números pars.

```
Exemple:
	Entrada
		Entra un número: 1
		Entra un número: 4
		Entra un número: 6
		Entra un número: -1

	Sortida:
		Llista: [1,4,6]
		Maxim: 6
		Parells: [4,6]
```

2. Realitzar un programa que, donada una llista, retorni una nova llista on el contingut sigui igual a la original però invertida. 

```
Exemple:
	Entrada:
		Llista [‘Digues’, ‘bon’, ‘día’, ‘al’, ‘pare’], 
	Sortida:
		[‘pare’, ‘al’, ‘día’, ‘bon’, ‘Digues’].
```

3. Donada una llista de cadenes, es demana una cadena por teclat i s'indica si está a la llista, indica quantes vegades apareix a la llista,  llegeix una altra cadena i substitueix la primera per la segona en la llista, y al final borra la cadena de la llista

4. Donada una llista, fer un programa que indiqui si està ordenada o no.

5. Donada una llista de noms de fitxers, volem canviar el nom de tots els fitxers amb extensió hpp a l'extensió h. Per fer-ho, ens agradaria generar una nova llista anomenada newfilenames, que constarà dels nous noms de fitxer. Omple els espais en blanc del codi utilitzant qualsevol dels mètodes que has après fins ara, com ara un bucle for o una comprensió de llista.

6. Crea una funció que converteixi el text en `anglesí`: una simple transformació de text que modifica cada paraula movent el primer caràcter al final i afegint "ay" al final. Per exemple, python acaba com a ythonpay.

        >>> def conv_anglesi(text):
        >>> ...

        >>> print(conv_anglesi("hello how are you"))                            # Retorna "ellohay owhay reaay ouyay"
        >>> print(conv_anglesi("programming in python is fun"))                 # Retorna "rogrammingpay niay ythonpay siay unfay"

7. Els permisos d'un fitxer en un sistema Linux es divideixen en tres conjunts de tres permisos: llegir, escriure i executar per al propietari, el grup i altres. Cadascun dels tres valors es pot expressar com un nombre octal que suma cada permís, amb 4 corresponents a llegir, 2 a escriure i 1 a executar. O es pot escriure amb una cadena utilitzant les lletres r, w i x o - quan no es concedeix el permís.
  Per exemple:
  640 és lectura/escriptura per al propietari, lectura per al grup i cap permís per als altres; convertit en una cadena, seria: "rw-r-----"
  755 és llegir/escriptura/executar per al propietari i llegir/executar per al grup i altres; convertit en una cadena, seria: "rwxr-xr-x"
  Crear un programa  converteixi un permís en format octal a un en format de cadena.

        >>> def octal_a_string(octal):
        >>> ...
    
        >>> print(octal_a_string(755))                                          # Retorna rwxr-xr-x
        >>> print(octal_a_string(644))                                          # Retorna rw-r--r--
        >>> print(octal_a_string(750))                                          # Retorna rwxr-x---
        >>> print(octal_a_string(600))                                          # Retorna rw-------


8. La funció group_list accepta un nom de grup i una llista de membres, i retorna una cadena amb el format: nom_grup: membre1, membre2, … Per exemple, llista_grup("g", ["a","b","c"] ) retorna "g: a, b, c". Crear un programa per fer-ho.

        >>> def grup_llista(group, users):
    
        >>> print(grup_llista("Marketing", ["Miquel", "Carla", "Jon", "Sasha"]))     # Retorna "Marketing: Miquel, Carla, Jon, Sasha"
        >>> print(grup_llista("Enginyeria", ["Quim", "Joel", "Tomas"]))              # Retorna "Engineering: Quim, Joel, Tomas"
        >>> print(grup_llista("Usuaris", ""))                                        # Retorna "Usuaris:"

9. Utilitzeu una comprensió de llista per crear una llista de nombres al quadrat (n*n). La funció rep les variables inici i final, i retorna una llista de quadrats de nombres consecutius entre inici i final inclusivament. Per exemple, quadrats(2, 3) hauria de retornar [4, 9].
    
        >>> def quadrats(start, end):
	    >>> ...

        >>> print(quadrats(2, 3))                                                 # Retorna [4, 9]
        >>> print(quadrats(1, 5))                                                 # Retorna [1, 4, 9, 16, 25]
        >>> print(quadrats0, 10))                                                 # Retorna [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
***
[Index](../../../README.md)

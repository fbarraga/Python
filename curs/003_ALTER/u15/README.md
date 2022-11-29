# Estructura de control: Alternatives/Condicionals

Si al avaluar l'expressió lògica obtenim el resultat True executa un bloc d'instruccions, en cas contrari executa un altre bloc.

## Alternatives simples

*Exemples*

	if numero<0:
		print("Número és negatiu")

## Alternatives dobles

*Exemples*

	if numero<0:
		print("Número és negatiu")	
	else:
		print("Número és positiu")

## Alternatives múltiples

*Exemples*

	if numero>0:
		print("Número és negatiu")	
	elif numero<0:
		print("Número és positiu")
	else:
		print("Número és zero")

## Expressió reduïda del if

*Exemples*

	>>> lang="es"
	>>> saludo = 'HOLA' if lang=='es' else 'HI'
	>>> saludo
	'HOLA'


## Expressió match / case

A partir de la versió 3.10 de Python s'incorpora una funcionalitat que trobem amb moltes llenguatges de programació que es el switch/case. En python utilitzarem les paracules match/case

*Exemples*

	lang = input("What's the programming language you want to learn? ")

	match lang:
    	case "JavaScript":
        	print("You can become a web developer.")
    	case "Python":
        	print("You can become a Data Scientist")
    	case "PHP":
        	print("You can become a backend developer")
    	case "Solidity":
        	print("You can become a Blockchain developer")
		case "Java":
        	print("You can become a mobile app developer")
    	case _:
        	print("The language doesn't matter, what matters is solving problems.")


***
[Index](../../../README.md)

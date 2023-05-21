# Exercicis de nivell mig

1. L'alfabet anglès conté 26 caràcters i els telèfons mòbils només tenen deu dígits al teclat. Diverses lletres es mapegen a cada tecla numèrica, com es mostra a la imatge inferior, de manera que es pugui escriure un missatge amb pulsacions repetitives. Per exemple, per inserir el caràcter B, cal prémer 22. Per introduir una seqüència de dos caràcters a partir de la mateixa tecla, l'usuari ha de fer una pausa abans de prémer el botó una segona vegada. Per exemple, 2 2 indica AA, mentre que 22 indica B (es mostra un "caràcter d'espai" per indicar una pausa). Heu de crear un programa que calculi la seqüència de tecles que cal prémer per escriure un cert missatge.

2. Realitzar un programa que simuli el joc de les tres en ratlla. Cada jugador només ha de col·locar la fitxa una vegada per torn i no ha de ser sobre una casella ja ocupada. En cas que el jugador faci trampa, el guanyador serà l'altre. Per guanyar cal aconseguir fer una línia recta (horitzontal, vertical o diagonal) amb la mateixa fitxa. El tauler és de 3x3 i qualsevol casella podrà estar buida o ocupada només per una fitxa X o 0. El programa ha de realitzar les operacions següents:

    * Mostrar el tablero por pantalla.
    * Poner una ficha en una cuadricula comprobando que no está ocupada.
    * Comprobar si se produce tres en raya e indicar si es de X o de O, o si hay empate.

Exemple d'execució:

```console
[' ', ' ', ' ']
[' ', ' ', ' ']
[' ', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 2
Introdueix la coordenada Y del 1 al 3: 2
Introdueix 0 per cercle o X para creu: X
[' ', ' ', ' ']
[' ', 'X', ' ']
[' ', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 2
Introdueix la coordenada Y del 1 al 3: 1
Introdueix 0 per cercle o X para creu: 0
[' ', ' ', ' ']
['0', 'X', ' ']
[' ', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 2
Introdueix la coordenada Y del 1 al 3: 1
Introdueix 0 per cercle o X para creu: X
Aquesta coordenada ja està sient utilitzada, utilitzi una lliure.
[' ', ' ', ' ']
['0', 'X', ' ']
[' ', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 3
Introdueix la coordenada Y del 1 al 3: 1
Introdueix 0 per cercle o X para creu: X
[' ', ' ', ' ']
['0', 'X', ' ']
['X', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 1
Introdueix la coordenada Y del 1 al 3: 2
Introdueix 0 per cercle o X para creu: 0
[' ', '0', ' ']
['0', 'X', ' ']
['X', ' ', ' ']
Introdueix la coordenada X del 1 al 3: 1
Introdueix la coordenada Y del 1 al 3: 3
Introdueix 0 per cercle o X para creu: X
[' ', '0', 'X']
['0', 'X', ' ']
['X', ' ', ' ']
La partida l'ha guanyat el jugador amb la fitxa X.
```

3. Realitzar un programa que pregunti a l'usuari per un número enter impar i dibuixi un rombe amb el número de filas introducidas por el usuario.


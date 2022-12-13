# Dades

## Literals, variables i expressions

### Literals

Els literals ens permeten representar valors. Aquests valors poden ser de diferents tipus, d'aquesta manera podem tenir.

**Literals numèrics**

* Per representar números enters utilitzem xifres enteres (Exemples: 3, 12, -23). Si volem representar-los de forma binaria començarem per la seqüència `0b` (Exemples: 0b10101, 0b1100). 
  
* La representació octal la fem començant per `0o` (Exemples: 0o377, 0o7) i per últim, la representació hexadecimal es comença per `0x` (Exemples: 0xdeadbeef, 0xfff).

* Pels números reals utilitzem un punt per separar la part entera de la decimal (12.3, 45.6). Podem indicar que la parte decimal es 0, per exemple 10., o la part entera es 0, per exemplo .001, Per la representació de números molt grans o molt petits podem utilitzar la representació exponencial (Exemples: 3.14e-10,1e100).

* Per últim, també podem representar números complexes, amb una part real i una altra imaginaria (Exemple: 1+2j)

**Literals cadenes**

Ens permeten representar cadenes de caràcters. Per delimitar les cadenes podems utilitzar el caràcter ' o el carácter ". També podem utilitzar la combinació ''' quan la cadena ocupa més d'una línia. 

Exemples:

	'hola que tal!'
	"Molt bé"

	'''Podem \n
	anar al cine'''

Les cadenes anteriors son del tipus `str`, si volem representar una cadena de tipus `byte` podrem fer-ho de la següent manera:

	b'Hola'
	B"Molt bé"

Amb el caràcter \, podem posar alguns caracters, per exemple:

	\\ 	Backslash (\) 	 
	\' 	Single quote (') 	 
	\" 	Double quote (") 	 
	\a 	ASCII Bell (BEL) 	 
	\b 	ASCII Backspace (BS) 	 
	\f 	ASCII Formfeed (FF) 	 
	\n 	ASCII Linefeed (LF) 	 
	\r 	ASCII Carriage Return (CR) 	 
	\t 	ASCII Horizontal Tab (TAB) 	 
	\v 	ASCII Vertical Tab (VT)


### Variables

Una variable és un identificador que referencia a un valor. Estudiarem més endavant que python utiliza tipat dinàmic, per lo tant no s'utilitza el concepte de variable com magatzem d'informació. Per a que una variable referencii a un valor s'utilitza l'operador d'assignació `=`.

El nom d'una variable, ha de començar per una lletra o pel caràcter guió baix, seguit de lletres, números o guions baixos. No s'ha de declarar la variable abans d'utilitzar-la, el tipus de la variable será el mateix que el del valor al que fa referència. Per lo tant el seu tipus pot canviar en qualsevol moment:

	>>> var = 5
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>

S'ha de tenir en compte que Python diferencia entre majúscules i minúscules en el nom de la variable, però només es recomana utilitzar minúscules.

#### Definició, borrat i ámbit de variables

Per crear una variable simplement hem d'utilitzar un operador d'assignació, el més utilitzat `=` . Si volem borrar la variable utilitzarem la instrucció `del`. Per exemple:

	>>> a = 5
	>>> a
	5
	>>> del a
	>>> a
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined

Podem tenir també variables que no tinguin assignat cap tipus de dades:

	>>> a = None
	>>> type(a)
	<class 'NoneType'>

L'àmbit d'una variable es refereix a la zona del programa on s'ha definit i existeix aquesta variable. Com a primera aproximació les variables creades dintre de funcions o classes tenen un àmbit local, és a dir no existeixen fora de la funció o de la classe.


### Expressions

Una expresió és una combinació de variables, literals, operadors, funcions i expressions, que després de la seva avaluació o càlcul ens retornen un valor d'un determinat tipus. 

Veiem exemples d'expressions:

	a + 7
	(a ** 2) + b


### Operadors. Precedència d'operadors en Python

Els operadors que podem utilitzar es classifiquen segons el tipus de dades amb els quee treballin. Exemples:

	+       -       *       **      /       //      %
	<<      >>      &       |       ^       ~
	<       >       <=      >=      ==      !=
	-=      *=      /=      //=     %=

Podem classificar-los en varis tipus:

* Operadors aritmétics
* Operadors de cadenes
* Operadors d'asignació
* Operadors de comparació
* Operadors lògics
* Operadors a nivell de bit
* Operadors de pertanyença
* Operadors de identitat

La precedència d'operadors és la següent:

1. Els parèntesis trenquen la precedència.
2. La potencia (**)
3. Operadors unaris (~ + -)
4. Multiplicar, dividir, mòdul i divisió entera (* /% // )
5. Suma i resta (+ -)
6. Desplaçament nivell de bit (>> <<)
7. Operador binari AND (&)
8. Operadors binari OR i XOR (^ |)
9. Operadors de comparació (<= < > >=)
10. Operadors d'igualtat (<> == !=)
11. Operadors d'assignació (= %= /= //= -= += *= **=)
12. Operadors d'identitat (is, is not)
13. Operadors de pertanyença (in, in not)
14. Operadors lògics (not, or, and)

## Funció eval()

La funció `eval()` rep una expressió como una cadena i l'executa.

	>>> x=1
	>>> eval("x + 1")
	2

***
[Index](../../../README.md)

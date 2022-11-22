# Dades

## Literals, variables i expresiones

### Literals

Els literals ens permeten representar valors. Aquests valors poden ser de diferents tipus, d'aquesta manera podem tenir.

**Literals numèrics**

* Per representar números enters utilitzem xifres enteres (Ejemplos: 3, 12, -23). Si volem representar-los de forma binaria començarem per la seqüència `0b` (Exemples: 0b10101, 0b1100). 
  
* La representació octal la fem començant per `0o` (Ejemplos: 0o377, 0o7) i per últim, la representació hexadecimal es comença per `0x` (Exemples: 0xdeadbeef, 0xfff).

* Pels números reales utilitzem un punt per separar la part entera de la decimal (12.3, 45.6). Podem indicar que la parte decimal es 0, per exemple 10., o la part entera es 0, per exemplo .001, Per la representació de números molt grans o molt petits podem utilitzar la representació exponencial (Exemples: 3.14e-10,1e100).

* Por último, también podemos representar números complejos, con una parte real y otra imaginaria (Ejemplo: 1+2j)

**Literals cadenes**

Ens permeten representar cadenes de caràcters. Per delimitar les cadenes podems utilitzar el caràcter ' o el carácter ". També podem utilitzar la combinació ''' quan la cadena ocupa més d'una línoa. 

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

Una variables es un identificador que referencia a un valor. Estudiaremos más adelante que python utiliza tipado dinámico, por lo tanto no se usa el concepto de variable como almacén de información. Para que una variable referencie a un valor se utiliza el operador de asignación `=`.

El nombre de una variable, ha de empezar por una letra o por el carácter guión bajo, seguido de letras, números o guiones bajos. No hay que declarar la variable antes de usarla, el tipo de la variable será el mismo que el del valor al que hace referencia. Por lo tanto su tipo puede cambiar en cualquier momento:

	>>> var = 5
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>

Hay que tener en cuanta que python distingue entre mayúsculas y minúsculas en el nombre de una variable, pero se recomienda usar sólo minúsculas.

#### Definición, borrado y ámbito de variables

Como hemos comentado anteriormente para crear una variable simplemente tenemos que utilizar un operador de asignación, el más utilizado `=` para que referencia un valor. Si queremos borrar la variable utilizamos la instrucción `del`. Por ejemplo:

	>>> a = 5
	>>> a
	5
	>>> del a
	>>> a
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined

Podemos tener también variables que no tengan asignado ningún tipo de datos:

	>>> a = None
	>>> type(a)
	<class 'NoneType'>

El ámbito de una variable se refiere a la zona del programa donde se ha definido y existe esa variable. Como primera aproximación las variables creadas dentro de funciones o clases tienen un ámbito local, es decir no existen fuera de la función o clase. Concretaremos cuando estudiamos estos aspectos más profundamente.


### Expresiones

Una expresión es una combinación de variables, literales, operadores, funciones y expresiones, que tras su evaluación o cálculo nos devuelven un valor de un determinado tipo. 

Veamos ejemplos de expresiones:

	a + 7
	(a ** 2) + b


### Operadores. Precedencia de operadores en python

Los operadores que podemos utilizar se clasifican según el tipo de datos con los que trabajen y podemos poner algunos ejemplos:

	+       -       *       **      /       //      %
	<<      >>      &       |       ^       ~
	<       >       <=      >=      ==      !=
	-=      *=      /=      //=     %=

Podemos clasificaros en varios tipos:

* Operadores aritméticos
* Operadores de cadenas
* Operadores de asignación
* Operadores de comparación
* Operadores lógicos
* Operadores a nivel de bit
* Operadores de pertenencia
* Operadores de identidad

La procedencia de operadores es la siguiente:

1. Los paréntesis rompen la procedencia.
2. La potencia (**)
3. Operadores unarios (~ + -)
4. Multiplicar, dividir, módulo y división entera (* /% // )
5. Suma y resta (+ -)
6. Desplazamiento nivel de bit (>> <<)
7. Operador binario AND (&)
8. Operadores binario OR y XOR (^ |)
9. Operadores de comparación (<= < > >=)
10. Operadores de igualdad (<> == !=)
11. Operadores de asignación (= %= /= //= -= += *= **=)
12. Operadores de identidad (is, is not)
13. Operadores de pertenencia (in, in not)
14. Operadores lógicos (not, or, and)

## Función eval()

La función `eval()` recibe una expresión como una cadena y la ejecuta.

	>>> x=1
	>>> eval("x + 1")
	2

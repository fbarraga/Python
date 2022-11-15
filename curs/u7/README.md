# Funcions i constants predefinides

## Funcions predefinidae

Tenim una serie de funcions predefinides en python3:

	abs() 		  dict() 		help()		 min() 		setattr()
	all() 		  dir() 		hex() 		 next() 	slice()
	any() 		  divmod() 		id() 		 object() 	sorted()
	ascii() 	  enumerate()	input() 	 oct() 		staticmethod()
	bin() 		  eval() 		int() 		 open() 	str()
	bool()		  exec() 		isinstance() ord() 		sum()
	bytearray()	  filter() 		issubclass() pow() 		super()
	bytes() 	  float() 		iter() 	 	 print() 	tuple()
	callable() 	  format() 		len() 		 property() type()
	chr() 		  frozenset() 	list() 		 range() 	vars()
	classmethod() getattr() 	locals() 	 repr() 	zip()
	compile() 	  globals() 	map() 		 reversed()	__import__()
	complex() 	  hasattr() 	max() 		 round() 	 
	delattr() 	  hash() 		memoryview() set() 	 

Totes aquestes funcions i alguns elements comuns del llenguatge están definides en el mòdul [builtins](https://docs.python.org/3/library/builtins.html).

### Alguns exemples de funcions

* La entrada i sortida d'informació es fa amb la funció `print` i la funció `input`:
* Tenim algunes funcions matemàtiques com: `abs`, `divmod`, `hex`, `max`, `min`,...
* Hi ha funcions que treballen amb caràcters i cadenes: `ascii`, `chr`, `format`, `repr`,...
* A més tenim funcions que creen o converteixen a determinats tipus de dades: `int`, `float`, `str`, `bool`, `range`, `dict`, `list`, ...


## Constants predefinides

En el mòdul [builtins](https://docs.python.org/3/library/builtins.html) es defineixen les següents constants:

* `True` y `False`: Valors booleans
* `None` especifica que alguna variable o objecte no té assignat cap tipus.

Hay alguna constante más que veremos a los largo del curso si es necesario.

## Ajuda a python

Un funció fundamental quan volem obtenir informació sobre els diferents aspectes del llenguatge es `help`. Podem usarla entrant en una sessió interactiva:

	>>> help()	

	Welcome to Python 3.4's help utility!	

	If this is your first time using Python, you should definitely check out
	the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.	

	Enter the name of any module, keyword, or topic to get help on writing
	Python programs and using Python modules.  To quit this help utility and
	return to the interpreter, just type "quit".	

	To get a list of available modules, keywords, symbols, or topics, type
	"modules", "keywords", "symbols", or "topics".  Each module also comes
	with a one-line summary of what it does; to list the modules whose name
	or summary contain a given string such as "spam", type "modules spam".

	help>

O demanant ajuda d'un terme determinat, per exemple:

	>>> help(print)

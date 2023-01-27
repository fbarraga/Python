# Tipus especials de funciones

## Nested functions

En python podem tenir una funció dintre d'una altra. Per exemple

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)  # prints 11
```

 Output: 11


## Funcions passats com a argument o retornar valor

Una altra opció es passar la funció com un argument més.Això en alguns casos ens pots servir per reduir codi. Un exemple el podem trobar:

```python
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10
```
Un exemple de retorn de funció com a valor el tenim:

```python
def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"
 Output: Hello, Atlantis!

```

## Funcions recursives

Una funció recursiva es aquella que al executar-se fa crides a si mateixa. Per lo tant hem de tenir "un cas base" que fa terminar el bucle de crides. Veiem un exemple:

	>>> def factorial(numero):
	...     if(numero == 0 or numero == 1):
	...         return 1
	...     else:
	...         return numero * factorial(numero-1)
	... 
	>>> factorial(5)
	120

## Funcions lambda

Las funcions lambda ens serveix per crear petites funcions anònimes, de una sola línea sobre la marxa.

	>>> cuadrado = lambda x: x**2
	>>> cuadrado(2)

Com podem veure les funcions lambda no tenen nom. Pero gràcies a que lambda crea una referència a un objecte funció, la podem cridar.

	>>> lambda x: x**2
	<function <lambda> at 0xb74469cc>
	>>>
	>>> (lambda x: x**2)(3)
	9

Un altre exemple:

	>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	>>> pairs.sort(key=lambda pair: pair[1])
	>>> pairs
	[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

## Decoradors

Els decoradors són funcions que reben com a paràmetres altres funcions i retornen com a resultat altres funcions amb l'objectiu d' alterar el funcionament original de la funció que es passa com a paràmetre. Hi ha funcions que tenen en comú moltes funcionalitats, per exemple les de maneig d'errors de connexió de recursos I/O (que s'han de programar sempre que usem aquests recursos) o les de validació de permisos en les respostes de peticions de servidors, en comptes de repetir el codi de rutines podem abstreure, bé sigui el maneig d'error o la resposta de peticions,  en una funció decorador.

	>>> def tablas(funcion):
	...     def envoltura(tabla=1):
	...         print('Tabla del %i:' %tabla)
	...         print('-' * 15)
	...         for numero in range(0, 11):            
	...             funcion(numero, tabla)
	...         print('-' * 15)
	...     return envoltura
	... 
	>>> @tablas
	... def suma(numero, tabla=1):
	...     print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))
	... 
	>>> @tablas
	... def multiplicar(numero, tabla=1):
	...     print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

	# Muestra la tabla de sumar del 1
	suma()	
	# Muestra la tabla de sumar del 4 
	suma(4)	
	# Muestra la tabla de multiplicar del 1
	multiplicar()	
	# Muestra la tabla de multiplicar del 10
	multiplicar(10)  

## Funciones generadoras

Un generador és un tipus concret de iterador. Es una funció que permet obtenir els resultats pas a pas.

	>>> def par(inicio,fin):
	...   for i in range(inicio,fin):
	...     if i % 2==0:
	...       yield i

	>>> datos = par(1,5)
	>>> next(datos)
	2
	>>> next(datos)
	4

	>>> for i in par(20,30):
	...   print(i,end=" ")
	20 22 24 26 28

	>>> lista_pares = list(par(1,10))
	>>> lista_pares
	[2, 4, 6, 8]


***
[Index](../../../README.md)


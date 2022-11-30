# Estructura de control: Repetitives

![](https://github.com/fbarraga/Python/blob/master/master/assets/iterativa.png?raw=true)

## while

L'estructura `while` ens permet repetir un bloc d'instruccions mentres al evaluar una expressió lògica ens retorna  True. Pot tenir una estructura `else` que s'executarà al terminar el bucle.

*Exemple*

	anyo = 2001 
	while anyo <= 2017: 
    	print ("Informes del Año", anyo) 
    	año += 1
    else:
    	print ("Hemos terminado")

## for

L'estructura `for` ens permet iterar els elementss de una secuencia (lista, rango, tupla, diccionario, cadena de caracteres,...). Puede tener una estructura `else` que se ejecutará al terminar el bucle.

*Ejemplo*

	for i in range(1,10):
        print (i)
	else:
        print ("Hemos terminado")

## Instrucciones break, continue y pass

### break

Termina la ejecución del bucle, además no ejecuta el bloque de instrucciones indicado por la parte `else`.

### continue
	
Deja de ejecutar las restantes instrucciones del bucle y vuelve a iterar.

### pass

Indica una instrucción nula, es decir no se ejecuta nada. Pero no tenemos errores de sintaxis.

## Recorriendo varias secuencias. Función zip()

Con la instrucción `for` podemos ejecutar más de una secuencia, utilizando la función `zip`. Esta función crea una secuencia donde cada elemento es una tupla de los elementos de cada secuencia que toma cómo parámetro.

*Ejemplo*

	>>> list(zip(range(1,4),["ana","juan","pepe"]))
	[(1, 'ana'), (2, 'juan'), (3, 'pepe')]

Para recorrerla:

	>>> for x,y in zip(range(1,4),["ana","juan","pepe"]):
	...     print(x,y)	
	1 ana
	2 juan
	3 pepe

***
[Index](../../../README.md)

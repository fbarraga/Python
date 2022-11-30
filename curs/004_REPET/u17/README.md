# Estructura de control: Repetitives

Podem veure el funcionament de les estructures repetitives en el següent fluxograma:

<p align="center">
  <img  src="https://github.com/fbarraga/Python/blob/master/master/assets/iterativa.png">
</p>


## while

L'estructura `while` ens permet repetir un bloc d'instruccions mentres al evaluar una expressió lògica ens retorna  True. Pot tenir una estructura `else` que s'executarà al terminar el bucle.

*Exemple*

	anyo = 2001 
	while anyo <= 2017: 
    	print ("Informes del any", anyo) 
    	año += 1
    else:
    	print ("Hem acabat")

## for

L'estructura `for` ens permet iterar els elementss de una secuencia (lista, rango, tupla, diccionario, cadena de caracteres,...). Puede tener una estructura `else` que se ejecutará al terminar el bucle.

*Exemple*

	for i in range(1,10):
        print (i)
	else:
        print ("Hem acabat")

## Instruccions break, continue i pass

### break

Acaba l'execució del bucle, a més no executa el bloc d'instruccions indicat amb la part `else`.

### continue
	
Deixa d'executar les instruccions que falten del bucle i torna a iterar.

### pass

Indica una instrucció nul·la, es a dir no s'executa res. Però no tenim errors de sintaxis.

## Recorriendo varias secuencias. Función zip()

Amb la instrucció `for` podem executar més d'una seqüència, utilizant la funció `zip`. Aquesta funció crea una seqüència on cada element es una tupla dels elements de cada seqüència que retorna cóm a paràmetre.

*Exemple*

	>>> list(zip(range(1,4),["ana","juan","pepe"]))
	[(1, 'ana'), (2, 'juan'), (3, 'pepe')]

Per recorrer-la:

	>>> for x,y in zip(range(1,4),["ana","juan","pepe"]):
	...     print(x,y)	
	1 ana
	2 juan
	3 pepe

***
[Index](../../../README.md)

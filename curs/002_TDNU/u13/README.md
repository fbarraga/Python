# Tipus de dades booleanes

## Tipus booleà

El tipus booleà o lògic es considera en python3 com un subtipus del tipus enter. Es pot representar amb dos valores: vertader o fals (True, False).

## ¿Quins valors s'interpreten com False?

Quan s'avalua una expressió, hi ha determinats valors que s'interpreten com a False:

* `None`
* `False`
* Qualsevol número 0. (0, 0.0, 0j)
* Qualsevol seqüència buit ([], (), '')
* Qualsevol diccionari buit ({})

## Operadors booleans

Els operadors booleans s'utilizen per operar sobre expresions booleanes i es solen utilitzar en les estructures de control alternatives (if, while):

* `x or y`: Si x es fals llavors y, sino x. Aquest operador només evalua el segon argument si el primer es False.
* `x and y`: Si x es fals llavors x, sino y. Aquest operador només evalua el segon argumento si el primero es True.
* `not x`: Si x es fals llavors True, sino False.

## Operadors de comparació

`== != >= > <= <`

## Funcions all() i any()

* `all(iterador)`: Rep un iterador, per exemple una llista, i retorna True si todos els elements son verdaderos o el iterador está buit. 
* `any(iterador)`: Rep un iterador, per exemple una llista, i retorna True si algun dels seus elements es vertader, sino retorna False.

***
[Index](../../../README.md)

# Codificació de caràcters

## Introducció a la codificació de caràcters

#### ASCII

Als principis de la informàtica els ordinadors es va dissenyar per utilitzar només caràcters anglesos, per lo tant es va crear una codificació de caràcters, anomenada ASCII (American Standard Code for Information Interchange) que utilitza 7 bits per codificar els 128 caràcters necessaris en l'alfabet anglès. Posteriorment es va extendre aquesta codificació per incluir caràcters no anglesos. Al utilitzar 8 bits es poden represenar fins a un màxim de 256 caràcters. Per codificar l'alfabet llatí apareix la codificació ISO-8859-1 o Latín 1.

#### Unicode

La codificació unicode  ens permet representar tots els caràcters de tots els alfabets del món, en realitat permet més d'un milió de caràcters, ja que utilitza 32 bits per la seva representació, però en realitat només es defineixen uns 110000 caràcters diferents.

#### UTF-8

UTF-8 es un sistema de codificació de longitud variable per Unicode. Això significa que els caràcters poden utilitzar diferent número de bytes.

## La codificación de caracteres en python3

En Python 3.x les cadenes de caràcters poden ser de tres tipus: Unicode, Byte i Bytearray.

* El tipus `unicode` permet caràcters de múltiples llenguatges i cada caràcter en una cadena tindrà un valor inmutable. 
* El tipus `byte` només permetrà caràcteres ASCII i els caràcteres son també inmutables.
* El tipus `bytearray` es como el tipus `byte` però, en aquest cas, els caràcters de una cadena si son mutables.

Una cosa important a entendre, (insisteix Mark Pilgrim en su libro *Dive into Python*) es que "els bytes no son caracters, elss bytes son bytes; un carácter és en realitat una abstracció; i una cadena de caràcters és una successió d'abstraccions".

## Funcions chr() y ord()

* `chr(i)`: Ens retorna el  carácter Unicode que representa el codi `i`.

		>>> chr(97)
		'a'
		>>> chr(1004)
		'Ϭ'

* `ord(c)`: rep un caràcter `c` i retorna el codi unicode corresponent.

		>>> ord("a")
		97
		>>> ord("Ϭ")
		1004

***
[Index](../../../README.md)

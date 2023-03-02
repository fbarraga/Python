# Introducció a Python
# Activitat 3: Estructures Repetitives

1. Demanar un número per teclat i mostrar la taula de multiplicar amb un while

```
	Entrada: Entra un número:
	Sortida: 
		1 x 1 = 1	
             	1 x 2 = 2     
		 ...
```

2. Demanar un número per teclat i mostrar la taula de multiplicar amb un for

```   
   	Entrada: Entra un número:
	Sortida: 
		1 x 1 = 1	
             	1 x 2 = 2     
		 ...
```

3. Crea un programa que demani un número i calculi el seu factorial (El factorial d'un número és el producte de tots els enters entre 1 i el propi número i es representa pel nombre seguit d'un signe d'exclamació. 

```
   Entrada: Entra el numero: 5
   Sortida: 5! = 1x2x3x4x5 = 120
```

4. Crea un programa que permeti endivinar un número. En primer lloc l'aplicació demana un número sencer per teclat. A continuació va demanant números i va responent si el número a endivinar és major o menor que l' introduït. El programa acaba quan s'encerta el número.

```
	Entrada: Entra el numero secret: 9
	Entrada: Entra un número: 4
	Sortida: El numero es més gran
	Entrada: Entra el número: 6
	Sortida: El número es més gran
	Entrada: Entra el número : 9
	Sortida: Felicitats! Era el número 9
```

5. Fés un programa que mostri la taula de multiplicar dels números 1,2,3,4 i 5.

```
   Entrada: -
   Sortida: 
   		1 x 1 = 1	
            	1 x 2 = 2     
	     	...
	    	2 x 1 = 2
```

6. Escriu un programa que digui si un número introduït per teclat és o no primer. Un número primer és aquell que només és divisible entre ell mateix i la unitat.

```
   Entrada: Entra el número: 3
   Sortida: El número 3 és primer
   Entrada: Entra el número: 25
   Sortida: El número 25 no és primer
```

7. Escriu un programa en python que doni la volta a un numero. 

```
   Entrada: Entra un numero per girar: 123456 
   Sortida esperada: 654321
```

8. Escriu un programa que imprimeixi tots els factors primers d'un nombre. Considerarem que és factor primer si és un nombre primer més petit que el nombre introduit i a la vegada aquest nombre primer divideix al nombre de tal manera que la resta és zero.

``` 
Entrada: Entra un número: 100
Sortida: Els factors primers son 2,5
```

9. El codi següent pot conduir a un bucle infinit. Corregiu el codi perquè pugui acabar correctament per a tots els números.

Exemple:
```
      >>> print(es_potencia_de_dos(0)) # Retorna False
      >>> print(es_potencia_de_dos(1)) # Retorna True
      >>> print(es_potencia_de_dos(8)) # Retorna True
      >>> print(es_potencia_de_dos(9)) # Retorna False
```
Nota: proveu d'executar la vostra funció amb el número 0 com a entrada i mireu què obteniu!
```
      >>> def es_potencia_de_dos(n):
      >>> 
      >>>   while n!=0 and n % 2 == 0:
      >>>      n = n / 2
      >>> return False
 ```
```
      >>> print(es_potencia_de_dos(0)) # Retorna False
      >>> print(es_potencia_de_dos(1)) # Retorna True
      >>> print(es_potencia_de_dos(8)) # Retorna True
      >>> print(es_potencia_de_dos(9)) # Retorna False
```

10.   Crea un programa que retorni la suma de tots els divisors d'un nombre, sense incloure a si mateix. Un divisor és un nombre que es divideix en un altre sense resta.

Exemple:
```      
      >>> print(sum_divisors(0))
      # 0
      >>> print(sum_divisors(3)) # Retorna  1
      # 1
      >>> print(sum_divisors(36)) # Retorna 1+2+3+4+6+9+12+18
      # 55
      >>> print(sum_divisors(102)) # Retorna 2+3+6+17+34+51
      # 114
```

11.   Crea un programa que imprimeixi els resultats d'un nombre  multiplicat per 1 a 5. Un requisit addicional és que el resultat no superi 25 (Utilitza l'instrucció break.) 

Exemple:
```
      >>> taula_multiplicar(3) 
      # Retorna: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

      >>> taula_multiplicar(5) 
      # Retorna: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

      >>> taula_multiplicar(8)	
      # Retorna: 8x1=8 8x2=16 8x3=24
```

Grup A:
12. Crea un programa que et digui quins son els propers anys bisiests en els propers 50 anys.

   

***
[Index](../../../README.md)


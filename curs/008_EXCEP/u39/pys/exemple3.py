#!/usr/bin/env python
x =  input("Dame un número:")
y =  input("Dame otro número:")

try:
	result = int(x) / int(y)
except ValueError:
	print("Algún número no es pot convertir a entero")
except ZeroDivisionError:
	print("Divisió per zero!")
else:
	print("El resultat es", result)
finally:
	print("Acabem el programa")
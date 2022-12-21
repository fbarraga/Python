#!/usr/bin/env python
while True:
	try:
		x = int(input("Introdueix un número:"))
		break
	except ValueError:
		print ("Has d'introduir un número")

print(x)
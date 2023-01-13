#!/usr/bin/env python
cad =  input("Dona'm un número:")
try:
	print (10/int(cad))
except ValueError:
	print("No es pot convertir a enter")
except ZeroDivisionError:
	print("No es pot dividirr per zero")
except:
	print("Qualsevol altre error")

def dividir(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		return "No es pot dividir"

def dividir2(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		raise 


print(dividir(2,0))
print(dividir2(2,0))
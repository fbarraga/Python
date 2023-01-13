
def nivel(numero):
	if numero<0:
		raise ValueError("El número ha de ser positiu:"+str(numero))
	else:
		return numero

print(nivel(5))
print(nivel(-1))
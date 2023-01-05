from persona import Cliente, Empleado

#cliente1 = Cliente('Alex' , 25)
#cliente2 = Cliente('Roel', 25)
#cliente1.detalle_persona()
#print(cliente2)

empleado1 = Empleado('Alex', 25, 1500)
empleado2 = Empleado('Roel', 25, 2000)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)
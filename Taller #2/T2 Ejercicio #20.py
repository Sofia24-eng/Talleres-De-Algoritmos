#entradas
precio=float(input("Ingrese el precio del computador: $"))
tcuotas=float(input("Ingrese el precio de cada couta: $"))
#caja negra
cuotas=(12*tcuotas)
porcentaje=((precio/cuotas)*100)
#salidas
print("El porcentaje de recargo al pagar por cuotas es de :"+str(porcentaje)+str("%"))
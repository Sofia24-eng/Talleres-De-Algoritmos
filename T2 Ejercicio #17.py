#entradas
presupuesto=float(input("Ingrese el presupuesto anual destinado para el hospital: $"))
#caja negra
ginecologia=(presupuesto*0.4)
traumatologia=(presupuesto*0.3)
pediatria=(presupuesto*0.3)
#salidas
print("El área de ginecología recibira: $"+str(ginecologia))
print("El área de traumatología recibira: $"+str(traumatologia))
print("El área de pediatría recibira: $"+str(pediatria))
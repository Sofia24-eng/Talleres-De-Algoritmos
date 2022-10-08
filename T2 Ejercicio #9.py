#entradas
horas=int(input("Ingrese la cantidad de horas que trabajó: "))
valor=float(input("Ingrese el valor pagado por hora: $"))
#caja negra
sueldoxhora=(valor*horas)
impuesto=(sueldoxhora*0.2)
salario_neto=(sueldoxhora-impuesto)
#salidas
print("El valor del impuesto es de: $"+str(impuesto))
print("Su salario neto sera de: $"+str(salario_neto))
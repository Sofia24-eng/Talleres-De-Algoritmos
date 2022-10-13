#entradas
sueldo=float(input("Ingrese su sueldo: $"))
#caja negra
if(sueldo<900000):
    aumento=(0.15*sueldo)
else:
    aumento=(0.12*sueldo)
nsueldo=(sueldo+aumento)
#salidas
print("El valor del aumento es: $"+str(aumento))
print("El nuevo sueldo es: $"+str(nsueldo))
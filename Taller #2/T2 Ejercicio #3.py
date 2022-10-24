#entradas
sueldo=float(input("Ingrese su sueldo base: $"))
venta1=float(input("Ingrese la primera venta: $"))
venta2=float(input("Ingrese la segunda venta: $"))
venta3=float(input("Ingrese la tercera venta: $"))
#caja negra
comision=(venta1+venta2+venta3)*0.10
sueldo_total=(sueldo+comision)
#salidas
print("Su sueldo base es:",sueldo)
print ("Su comision es:",comision)
print("Su sueldo total es:",sueldo_total)
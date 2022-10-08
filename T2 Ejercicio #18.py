#entradas
bolivares_X=float(input("Ingrese el valor del préstamo: $"))
bolivares_Y=float(input("Ingrese el valor de los intereses a 4 años: $"))
#caja negra
interes=(bolivares_Y-bolivares_X)
i=((interes/bolivares_X)*100)
#salidas
print("El porcentaje anual que se cobró por el préstamo dué de: "+str(i)+str("%"))
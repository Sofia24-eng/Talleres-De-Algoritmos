import math
#entradas
lado1=float(input("Ingrese lado uno: "))
lado2=float(input("Ingrese lado dos: "))
lado3=float(input("Ingrese lado tres: "))
#caja negra
s=(lado1+lado2+lado3)/2
area=math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
print("El Área Es: "+str(area))
#entradas
inversion=float(input("Ingrese la cantidad que invirtió en el banco: $"))
tasa_int=float(input("Ingrese la tasa de interés: "))
#caja negra
interes=(inversion*tasa_int)
total=(inversion+interes)
if(interes>100000):
    print("La cantidad generada por motivo de intereses es",interes,"mayor que $100000")
else:
    print("La cantidad generada por motivo de intereses es",interes,"menor que $100000")
#salidas
print("Finalmente tendrá",total,"en su cuenta")
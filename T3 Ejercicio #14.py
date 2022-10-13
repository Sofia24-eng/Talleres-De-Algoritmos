#entradas
lectura_anterior=float(input("Ingrese su lectura anterior: "))
lectura_actual=float(input("Ingrese su lectura actual: "))
aseo=float(input("Ingrese el precio que paga por servicio de aseo: $"))
#caja negra
kilovatios=abs(lectura_anterior-lectura_actual)
kwh=int
if(kilovatios>=0 and kilovatios<=100):
    kwh=4600
elif(kilovatios>=101 and kilovatios<=300):
    kwh=8000
elif(kilovatios>=301 and kilovatios<=500):
    kwh=100000
elif(kilovatios>501):
    kwh=120000
monto=(kilovatios*kwh)
total=(monto+aseo)
#salidas
print("El valor que deberá pagar por luz eléctrica es: $"+str(monto))
print("El valor total a pagar por servicio de luz y aseo es: $"+str(total))
#entradas
nombre=input("Ingrese su nombre: ")
monto=float(input("Ingrese el monto de la compra: $"))
#caja negra
if(monto<50000):
    tasa=0
    precio=(monto-(monto*tasa))
    desc="0%"

elif(monto>=50000 and monto<=100000):
    tasa=0.05
    precio=(monto-(monto*tasa))
    desc="5%"

elif(monto>100000 and monto<=700000):
    tasa=0.11
    precio=(monto-(monto*tasa))
    desc="11%"

elif(monto>700000 and monto<=1500000):
    tasa=0.18
    precio=(monto-(monto*tasa))
    desc="18%"

elif(monto>1500000):
    tasa=0.25
    precio=(monto-(monto*tasa))
    desc="25%"
descuento=(monto*tasa)
#salidas
print("El descuento aplicado fué de: $"+str(descuento),"es decir el "+str(desc),"del precio original")
print(str(nombre),"Deberá pagar: $"+str(precio))
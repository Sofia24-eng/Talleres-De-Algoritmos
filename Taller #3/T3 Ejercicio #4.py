#entradas
monto=float(input("Ingrese el monto total de la compra: $"))
#caja negra
if(monto>5000000):
    inversion=(monto*0.55)
    banco=(monto*0.3)
    credito=(monto*0.15)
else:
    inversion=(monto*0.7)
    banco= (monto*0)
    credito=(monto*0.3)
interes=(credito*0.20)
#salidas
print("La inversión hecha por la empresa es de: $"+str(inversion))
print("El préstamo solicitado al banco es de: $"+str(banco))
print("El crédito a pagar es de: $"+str(credito))
print("El interés por el crédito es de: $"+str(interes))
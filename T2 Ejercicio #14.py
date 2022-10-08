#entradas
lec_actual=float(input("Ingrese su lectura actual: "))
lec_anterior=float(input("Ingrese su lectura anterior: "))
valor_kv=float(input("Ingrese el costo por kilovatio: "))
#caja negra
monto_total=abs((lec_anterior-lec_actual)*valor_kv)
#salidas
print("El monto total que debera pagar es de: $"+str(monto_total))
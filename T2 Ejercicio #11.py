#entradas
nombre=str(input("Escriba su nombre: "))
nhijos=int(input("Escriba la cantidad de hij@s que tiene: "))
horas=int(input("Ingrese el número de horas que trabaja: "))
valorxhora=float(input("Ingrese el valor pagado por hora: $"))
hora_extra=int(input("Ingrese el número de horas extra que trabaja: "))
#caja negra
sueldo=(horas*valorxhora)
h_extra=((hora_extra*sueldo)*1.25)


pago_forsozo=(sueldo*0.05)
politica_hab=(sueldo*0.02)
caja_ahorro=(sueldo*0.07)
deducciones=(pago_forsozo+politica_hab+caja_ahorro)

hijos=(nhijos*173000)
asignaciones=(250000+180000+hijos)

sueldo_neto=(sueldo+h_extra+deducciones+asignaciones)
#salidas
print("El sueldo de",nombre,"es: $"+str(sueldo))
print("Por motivo de: horas extra",nombre,"recibe $"+str(h_extra),"adicionales")
print("Por motivo de: deducciones",nombre,"recibe $"+str(deducciones),"adicionales")
print("Por motivo de: asignaciones",nombre,"recibe $"+str(asignaciones),"adicionales")
print("El sueldo neto de",nombre,"es: $"+str(sueldo_neto))
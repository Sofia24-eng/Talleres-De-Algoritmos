#entradas
categoria=int(input("Escriba la categoria a la que pertenece (1-5): "))
#caja negra
if(categoria==1):
    sueldo=5000000
    aumento=(sueldo*0.1)
    desc="10%"

elif(categoria==2):
    sueldo=4300000
    aumento=(sueldo*0.15)
    desc="15%"

elif(categoria==3):
    sueldo=3600000
    aumento=(sueldo*0.2)
    desc="20%"

elif(categoria==4):
    sueldo=2000000
    aumento=(sueldo*0.4)
    desc="40%"

elif(categoria==5):
    sueldo=900000
    aumento=(sueldo*0.6)
    desc="60%"
else:
    print("La categoría no existe")
nsueldo=(sueldo+aumento)
#salidas
print("La categoria del trabajador es:",categoria)
print("El aumento aplicado al trabajador fué de: $"+str(aumento),"es decir el "+str(desc))
print("El nuevo sueldo del trabajador es: $"+str(nsueldo))
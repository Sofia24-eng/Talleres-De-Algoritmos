#entradas
dep1=float(input("Ingrese las ventas del departamento 1: $"))
dep2=float(input("Ingrese las ventas del departamento 2: $"))
dep3=float(input("Ingrese las ventas del departamento 3: $"))
salario=float(input("Ingrese el salario que ganan los trabajadores: $"))
#caja negra
importe_glb=(dep1+dep2+dep3)
incentivo=(0.33*importe_glb)
#salidas
if(dep1>incentivo):
    extra=(salario+(salario*0.2))
    print("El salario del departamento 1 es: $"+str(extra))
else:
    print("El salario del departamento 1 es: $"+str(salario))

if(dep2>incentivo):
    extra=(salario+(salario*0.2))
    print("El salario del departamento 2 es: $"+str(extra))
else:
    print("El salario del departamento 2 es: $"+str(salario))

if(dep3>incentivo):
    extra=(salario+(salario*0.2))
    print("El salario del departamento 3 es: $"+str(extra))
else:
    print("El salario del departamento 3 es: $"+str(salario))
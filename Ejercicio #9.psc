Algoritmo Inicio_Sueldo
	//entradas
	Escribir "Sueldo Base: "
	leer sueldo
	Escribir "Venta 1: "
	Leer v1
	Escribir "Venta 2: "
	Leer v2
	Escribir "Venta 3: "
	Leer v3
	//caja negra
	comision<- (v1+v2+v3)*0.10
	sueldo_total<- sueldo+comision
	//salidas
	Escribir "Sueldo Base: $" sueldo
	Escribir "Comisióm: $" comision
	Escribir "Sueldo Total: $" sueldo_total
FinAlgoritmo


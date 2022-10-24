Algoritmo Inicio_Tiempo
	//entradas
	Escribir "Minutos: "
	Leer minutos
	//caja negra
	h<- abs(trunc(minutos/60))
	min<- abs(60*h)
	m<- (minutos-min)
	//salidas
	Escribir "Horas: " h
	Escribir "Minutos: " m
FinAlgoritmo

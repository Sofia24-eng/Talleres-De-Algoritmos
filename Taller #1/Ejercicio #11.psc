Algoritmo Inicio_Calificacion_Final
	//entradas
	Escribir "Digite Su Nota Del Trabajo Final: "
	leer tf
	Escribir "Digite Su Nota Del Examen Final: "
	leer ef
	Escribir "Digite Sus 3 Calificaciones Parciales: "
	leer c1
	leer c2
	leer c3
	//caja negra
	trabajo_final<- (tf*0.15)
	examen_final<- (ef*0.30)
	calificaciones_parciales<- ((c1+c2+c3)/3)*0.55
	calificacion_final<- (trabajo_final+examen_final+calificaciones_parciales)
	//salidas
	Escribir "Su calificación Final De La Materia Es: " calificacion_final
FinAlgoritmo

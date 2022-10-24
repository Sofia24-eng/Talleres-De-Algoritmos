Algoritmo Inicio_Coordenadas
	//entradas
	Escribir "Escriba un punto en el plano: "
	leer x1 
	leer y1
	Escribir "Escriba otro punto en el plano: "
	leer x2
	leer y2
	//caja negra
	distancia<- raiz((x2-x1)^2+(y2-y1)^2)
	//salidas
	Escribir "La distancia entre los dos puntos es: " distancia
FinAlgoritmo

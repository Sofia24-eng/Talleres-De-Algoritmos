Algoritmo Inicio_Velocidad
	Escribir "Escriba una velocidad para el vehículo 1 (Km/h): "
	leer v1
	Escribir "Escriba una velocidad para el vehículo 2 (Km/h): "
	leer v2
	Escribir "Escriba la distancia que hay entre los dos vehículos (Km): "
	leer d
	//caja negra
	v<- abs(v1-v2)
	t<- (d/v)
	m<- trunc(t*60)
	//salidas
	Escribir "el vehículo más rápido alcanzará al otro en: " m " minutos"
FinAlgoritmo

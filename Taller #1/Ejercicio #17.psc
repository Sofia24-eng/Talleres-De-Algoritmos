Algoritmo Inicio_Velocidad
	Escribir "Escriba una velocidad para el veh�culo 1 (Km/h): "
	leer v1
	Escribir "Escriba una velocidad para el veh�culo 2 (Km/h): "
	leer v2
	Escribir "Escriba la distancia que hay entre los dos veh�culos (Km): "
	leer d
	//caja negra
	v<- abs(v1-v2)
	t<- (d/v)
	m<- trunc(t*60)
	//salidas
	Escribir "el veh�culo m�s r�pido alcanzar� al otro en: " m " minutos"
FinAlgoritmo

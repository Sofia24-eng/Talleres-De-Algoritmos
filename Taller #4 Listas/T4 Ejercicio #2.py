# Tenemos la lista de edades
edades = [18, 11, 34, 63, 20, 28, 45, 22, 9]

# TODO: Imprimir el tamaño o el número de elementos de la lista edades.
print("El Tamaño Es: ",len(edades))

# TODO: Imprimir el segundo elemento de la lista de edades (debe ser un 11)
print("Segundo Elemento: ",edades[1])

# TODO: Obtener e imprimir el último elemento de la lista de edades (que debe ser un 9). Use un índice negativo.
print("Último Elemento: ",edades[-1])

# TODO: Imprimir el elemento que se encuentra en la mitad de la lista (que debe ser un 20).
print("Elemento de la Mitad: ",edades[len(edades)//2])

# TODO: Usando múltiples índices, guardar en una variable, llamada primeros los primeros 6 elementos de la lista de edades. Imprima la variable primeros.
primeros=edades[0:6]
print("Primeros Seis Elementos: ",primeros)
# TODO: Usando múltiples índices, guardar en una variable llamada ultimos los últimos 4 elementos de la lista de eddades. Imprima la varibale ultimos.
ultimos=edades[-4:]
print("Últimos Cuatro Elementos: ",ultimos)
# TODO: Guardar en otra variable ``primeros2`` otra vez los primeros 6 elementos de la lista ``edades``. Esta vez simplifique la escogencia omitiendo el índice inicial
primeros2=edades[1:7]
print("Primeros Seis Elementos Excepto el Primero: ",primeros2)
# TODO: Guardar en otra variable ``ultimos2`` otra vez los últimos 4 elementos de la lista ``edades``. Esta vez simplifique la escogencia omitiendo el índice final
ultimos2=edades[-5:-1]
print("Últimos Cuatro Elementos Excepto el Último: ",ultimos2)
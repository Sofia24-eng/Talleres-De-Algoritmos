edades = [18, 11, 34, 63, 20, 28, 45, 22, 9]
# TODO: Actualice el valor del último elemento de la lista edades. Ya no queremos que sea un 9 sino que sea un 19.
edades[-1]=19
print("Nuevo Último: ",edades[-1])
# TODO: Modifique el valor del tercer elemento de la lista de edades. Guardar un 24 en esa posición.
edades[2]=24
print("Nuevo Tercero: ", edades[2])
# TODO: Imprima la lista de edades. Verifique que el tercer elemento sea un 24, y que el último sea un 19.
print(edades)
assert edades[-1]==19 and edades[2]==24
print("Prueba superada 😎")
# TODO: Agregue los elementos 21, 32 y 16 al final de la lista edades. Imprima el tamaño de la lista y luego imprima la lista.
edades.append(21)
edades.append(32)
edades.append(16)
print("El Nuevo Tamaño Es:",len(edades), "Nueva lista es:",edades)
# TODO: Elimine el primer elemento de la lista, y luego elimine el quinto elemento de la lista de edades. Imprima la lista y el tamaño de la lista también.
edades.pop(0)
edades.pop(4)
print("Nueva Lista:",edades)
print("El Nuevo Tamaño Es:",len(edades))
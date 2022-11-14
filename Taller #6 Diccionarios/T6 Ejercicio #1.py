Ejemplo=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23] 
diccionario={}
for i in Ejemplo:
    cantidad=Ejemplo.count(i)
    diccionario.update({i:cantidad})
print(diccionario)
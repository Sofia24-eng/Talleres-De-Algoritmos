# Programa en Python para leer información de varios estudiantes. Use un while para saber si seguimos la lectura o no
informacion=[]
while True:
  nombre=input("Ingrese nombre: ")
  carrera=input("Ingrese carrera: ")
  promedio=float(input("Ingrese Promedio de la Carrera: "))
  if(nombre=="" and carrera==""):
    break
  datos=(nombre,carrera,promedio)
  informacion.append(datos)
print(informacion)
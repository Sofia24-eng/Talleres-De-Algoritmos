# Programa en Python para leer la edad de varios estudiantes. 
# Vamos a preguntar cuantos estudiantes hay = N.
c=0
estudiantes=int(input("¿Cuántos estudiantes hay? "))
edades1=[]
while True:
    if(c==estudiantes):
        break
    edad=int(input("Ingrese edad: "))
    edades1.append(edad)
    c=c+1
print("Lista: ",edades1)
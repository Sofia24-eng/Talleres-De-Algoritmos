estudiantes={}
aprobados=[]
suspendidos=[]
calificaciones=[]
alumnos=int(input("¿Cuántos Alumnos Hay? "))
while (alumnos<=10 and alumnos>0):
    for i in range(alumnos):
        nombres=input("Nombre Del Estudiante: ")
        notas=float(input("Nota De "+str(nombres)+str(": ")))
        calificaciones.append((notas))
        nota_media=((sum(calificaciones))/alumnos)
        if(nombres not in estudiantes and notas not in estudiantes):
            i=i+1
            estudiantes.update({i: {'nombre':nombres, 'nota':notas}})
        if(notas>=5.0):
            aprobados.append((nombres,notas))
        else:
            suspendidos.append((nombres,notas))
    print(estudiantes)
    print("Lista De Alumnos Aprobados:",aprobados)
    print("Lista De Alumnos Suspendidos:",suspendidos)
    print("La Nota Media Del Curso Es: ",round(nota_media,2))
    break
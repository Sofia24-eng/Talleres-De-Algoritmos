#entradas
exam_mate=float(input("Digite su nota del examen de matemática: "))
tarea1_mate=float(input("Digite su nota de la tarea 1 de matemática: "))
tarea2_mate=float(input("Digite su nota de la tarea 2 de matemática: "))
tarea3_mate=float(input("Digite su nota de la tarea 3 de matemática: "))

exam_fi=float(input("Digite su nota del examen de física: "))
tarea1_fi=float(input("Digite su nota de la tarea 1 de física: "))
tarea2_fi=float(input("Digite su nota de la tarea 2 de física: "))

exam_qui=float(input("Digite su nota del examen de química: "))
tarea1_qui=float(input("Digite su nota de la tarea 1 de química: "))
tarea2_qui=float(input("Digite su nota de la tarea 2 de química: "))
tarea3_qui=float(input("Digite su nota de la tarea 3 de química: "))

#caja negra
promedio_mat=((exam_mate*0.9)+((tarea1_mate+tarea2_mate+tarea3_mate)/3)*0.1)
promedio_fi=((exam_fi*0.8)+(((tarea1_fi+tarea2_fi)/2)*0.2))
promedio_qui=((exam_qui*0.85)+(((tarea1_qui+tarea2_qui+tarea3_qui)/3)*0.15))
promedio_general=((promedio_mat+promedio_fi+promedio_qui)/3)

#salidas
print("Su promedio en matemática es de:",round(promedio_mat,2))
print("Su promedio en física es de:",round(promedio_fi,2))
print("Su promedio en química es de:",round(promedio_qui,2))
print("Su promedio general es de:",round(promedio_general,2))
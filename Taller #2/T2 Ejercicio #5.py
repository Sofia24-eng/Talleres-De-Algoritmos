#entradas
t_f=float(input("Digite Su Nota Del Trabajo Final: "))
e_f=float(input("Digite Su Nota Del Examen Final: "))
c_p1=float(input("Digite Su primera Calificación Parcial: "))
c_p2=float(input("Digite Su segunda Calificación Parcial: "))
c_p3=float(input("Digite Su tercera Calificación Parcial: "))
#caja negra
t_final=(t_f*0.15)
e_final=(e_f*0.30)
c_parciales=(((c_p1+c_p2+c_p3)/3)*0.55)
nota_final=(t_final+e_final+c_parciales)
#salidas
print("Su calificación Final De La Materia Es:", nota_final)
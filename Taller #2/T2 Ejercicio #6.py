#entradas
mujeres=int(input("Ingrese el número de mujeres del grupo: "))
hombres=int(input("Ingrese el número de hombres del grupo: "))
#caja negra
total_grupo=(mujeres+hombres)
p_mujeres=round(((mujeres/total_grupo)*100))
p_hombres=round(((hombres/total_grupo)*100))
#salidas
print("En total hay",total_grupo,"estudiantes")
print("El porcentaje de mujeres del grupo es: "+str(p_mujeres)+str("%"))
print("El porcentaje de hombres del grupo es: "+str(p_hombres)+str("%"))
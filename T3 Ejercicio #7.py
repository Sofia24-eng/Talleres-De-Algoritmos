#entradas
distancia=float(input("Escriba la distancia recorrida en km: "))
#caja negra
if(distancia<300):
    precio=(50000+0)

if(distancia>=300 and distancia<1000):
    precio=(70000+30000*(distancia-300))

if(distancia>=1000):
    precio=(150000+9000*(distancia-1000))
#salidas
print("Se deberá cancelar:",precio,"COP")
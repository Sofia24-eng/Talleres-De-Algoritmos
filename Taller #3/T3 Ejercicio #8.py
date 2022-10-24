#entradas
from ast import Expression


P=int(input("Ingrese un valor entero para P: "))
Q=int(input("Ingrese un valor entero para Q: "))
#caja negra
expresion=(P**3+Q**4-2*P**2)
if(expresion>680):
    re="P y Q Satisfacen la expresión"
else:
    re="P y Q no Satisfacen la expresión"
#salidas
print("P^3+Q^4-2*P^2="+str(expresion))
print("Si P="+str(P),"y Q="+str(Q),"entonces los valores asignados para "+str(re),"para ser mayor que 680")

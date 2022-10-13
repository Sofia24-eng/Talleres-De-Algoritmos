#entradas
import math
datos=input()
(a,b,c)=datos.split(" ")
A= float(a)
B= float(b)
C= float(c)
#caja negra
operación=(B**2)-(4*(A*C))
D=math.sqrt(operación)
if(operación<=0 and A==0):
    print("Impossivel calcular")
else:
    R1=(-B+D)/2*A
    R2=(-B-D)/2*A
    print("R1 ="+str("{:.5f}" .format(R1)))
    print("R2 ="+str("{:.5f}" .format(R2)))
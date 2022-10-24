#entradas
A=int(input("Valor de A:"))
B=int(input("Valor de B:"))
C=int(input("Valor de C:"))
D=int(input("Valor de D:"))
#caja negra
if(D==0):
    print("[A-C]^2=",(A-C)**2)
    print("No se puede realizar la operación")
elif(D>0): #salidas
    print("[A-C]^2=",(A-C)**2)
    print("([A-B]^3)/D=",((A-B)**3)/D)
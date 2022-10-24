#entradas
from posixpath import split
N=input("Ingrese cuatro digitos: ")
(A,B,C,D)=N,split(",")
a=int(A)
b=int(B)
c=int(C)
d=int(D)
#caja negra
if( b>=9 and c>=5):
    a+1
    b=0
    c=0
    d=0
elif(b>=9 and c<5):
    b= b
    c=0
    d=0 
elif(b<9 and c>=5):
    b+1
    c=0
    d=0
else:
    c=0
    d=0
N=int(input())
#salidas
print(a,b,c,d)
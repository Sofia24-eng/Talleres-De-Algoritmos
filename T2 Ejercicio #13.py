#entradas
N1=int(input("Cantidad de billetes de 50000: "))
N2=int(input("Cantidad de billetes de 20000: "))
N3=int(input("Cantidad de billetes de 10000: "))
N4=int(input("Cantidad de billetes de 5000: "))
N5=int(input("Cantidad de billetes de 2000: "))
N6=int(input("Cantidad de billetes de 1000: "))
N7=int(input("Cantidad de billetes de 500: "))
N8=int(input("Cantidad de billetes de 100: "))
#caja negra
dinero_total=((N1*50000)+(N2*20000)+(N3*10000)+(N4*5000)+(N5*2000)+(N6*1000)+(N7*500)+(N8*100))
#salidas
print("El total de dinero que hay en el banco es: $"+str(dinero_total))
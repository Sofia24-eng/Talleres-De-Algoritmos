# Programa en Python para leer paises y capitales. Vamos a preguntar cuantos paises leer.
lista=[]
while True:
    pais=input("Ingrese País: ")
    capital=input(f"Ingrese Capital del pais({pais}): ")
    if(pais=="" and capital==""):
        break
    par=(pais,capital)
    lista.append(par)
print(lista)
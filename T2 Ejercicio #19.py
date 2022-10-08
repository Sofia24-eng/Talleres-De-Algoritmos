#entradas
xnaranjas=int(input("Ingrese el número de naranjas adquiridas: "))
yprecio=float(input("Ingrese el valor de la docena: $"))
kganancia=float(input("Ingrese la ganancia obtenida después de vender las naranjas: $"))
#caja negra
docenas_adquiridas=(xnaranjas/12)
valorxdocena=(kganancia/docenas_adquiridas)
diferencia_precios=(valorxdocena-yprecio)
ganancia=((diferencia_precios/yprecio)*100)
#salidas
print("La ganancia total después de la inversión es de: $"+str(ganancia)+str("%"))
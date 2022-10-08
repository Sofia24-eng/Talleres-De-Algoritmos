#entradas
pvp=float(input("Digite el precio inicial del producto: $"))
precio_final=float(input("Digite el precio final del producto: $"))
#caja negra
costo=round((((precio_final/pvp)*100)))
descuento=(100-costo)
#salidas 
print("El porcentaje de descuento aplicado al producto fué de:"+str(descuento)+str("%"))
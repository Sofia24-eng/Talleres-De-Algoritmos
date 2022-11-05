dividendo=int(input("Ingrese El Dividendo: "))
divisor=int(input("Ingrese El Divisor: "))
cociente=0
while True:
    if(dividendo<divisor):
        break
    dividendo=dividendo-divisor
    cociente=cociente+1
    resto=dividendo
print("El Cociente De La División Es:",cociente)
print ("El Resto De La División Es:",resto)
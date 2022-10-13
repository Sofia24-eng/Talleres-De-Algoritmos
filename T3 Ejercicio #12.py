#entradas
cop=int(input("Ingrese una cantidad entera de dinero: $"))
#caja negra
if(cop>=100000):
    sobra=cop//100000
    print("Hay "+str(sobra),"billetes de 100000")
    dinero=cop%100000
if(cop>=50000):
    sobra=cop//50000
    print("Hay "+str(sobra),"billetes de 50000")
    dinero=cop%50000
if(cop>=20000):
    sobra=cop//20000
    print("Hay "+str(sobra),"billetes de 20000")
    dinero=cop%20000
if(cop>=10000):
    sobra=cop//10000
    print("Hay "+str(sobra),"billetes de 10000")
    dinero=cop%10000
if(cop>=5000):
    sobra=cop//5000
    print("Hay "+str(sobra),"billetes de 5000")
    dinero=cop%5000
if(cop>=2000):
    sobra=cop//2000
    print("Hay "+str(sobra),"billetes de 2000")
    dinero=cop%2000
if(cop>=1000):
    sobra=cop//1000
    print("Hay "+str(sobra),"billetes de 1000")
    dinero=cop%1000
if(cop>=500):
    sobra=cop//500
    print("Hay "+str(sobra),"monedas de 500")
    dinero=cop%500
if(cop>=200):
    sobra=cop//200
    print("Hay "+str(sobra),"monedas de 200")
    dinero=cop%200
if(cop>=100):
    sobra=cop//100
    print("Hay "+str(sobra),"monedas de 100")
    dinero=cop%100
if(cop>=50):
    sobra=cop//50
    print("Hay "+str(sobra),"monedas de 50")
    dinero=cop%50
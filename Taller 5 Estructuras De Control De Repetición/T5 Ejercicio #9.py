alcohol=0
gasolina=0
diesel=0
while True:
    tipo=int(input())
    if(tipo==4):
        break
    if(tipo==1):
        alcohol=alcohol+1
    elif(tipo==2):
        gasolina=gasolina+1
    elif(tipo==3):
        diesel=diesel+1
print("MUITO OBRIGADO")
print("Alcohol:",alcohol)
print("Gasolina:",gasolina)
print("Diesel:",diesel)

#Fecha
from datetime import datetime
hoy=datetime.now()
print("Hoy es: ",hoy)
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#entradas
fecha_nacimiento=input("Ingrese su fecha de nacimiento dd/mm/yy: ")
(dia,mes,año)=fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#caja negra
edad=0
if(mes_actual>mes_nacimiento):
    edad=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        edad(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
signo=""
if((mes_nacimiento==1 and (dia_nacimiento>=21 and dia_nacimiento<=31)) or mes_nacimiento==2 and dia_nacimiento<=19):
    signo="Acuario"
elif((mes_nacimiento==2 and (dia_nacimiento>=20 and dia_nacimiento<=29)) or mes_nacimiento==3 and dia_nacimiento<=20):
    signo="Piscis"
elif((mes_nacimiento==3 and (dia_nacimiento>=21 and dia_nacimiento<=31)) or mes_nacimiento==4 and dia_nacimiento<=20):
    signo="Aries"
elif((mes_nacimiento==4 and (dia_nacimiento>=21 and dia_nacimiento<=30)) or mes_nacimiento==5 and dia_nacimiento<=21):
    signo="Tauro"
elif((mes_nacimiento==5 and (dia_nacimiento>=22 and dia_nacimiento<=31)) or mes_nacimiento==6 and dia_nacimiento<=21):
    signo="Géminis"
elif((mes_nacimiento==6 and (dia_nacimiento>=22 and dia_nacimiento<=30)) or mes_nacimiento==7 and dia_nacimiento<=22):
    signo="Cáncer"
elif((mes_nacimiento==7 and (dia_nacimiento>=23 and dia_nacimiento<=31)) or mes_nacimiento==8 and dia_nacimiento<=23):
    signo="Leo"
elif((mes_nacimiento==8 and (dia_nacimiento>=24 and dia_nacimiento<=31)) or mes_nacimiento==9 and dia_nacimiento<=22):
    signo="Virgo"
elif((mes_nacimiento==9 and (dia_nacimiento>=23 and dia_nacimiento<=30)) or mes_nacimiento==10 and dia_nacimiento<=22):
    signo="Libra"
elif((mes_nacimiento==10 and (dia_nacimiento>=23 and dia_nacimiento<=31)) or mes_nacimiento==11 and dia_nacimiento<=21):
    signo="Escorpión"
elif((mes_nacimiento==11 and (dia_nacimiento>=22 and dia_nacimiento<=30)) or mes_nacimiento==12 and dia_nacimiento<=21):
    signo="Sagitario"
elif((mes_nacimiento==12 and (dia_nacimiento>=22 and dia_nacimiento<=31)) or mes_nacimiento==1 and dia_nacimiento<=20):
    signo="Capricornio"
#salidas
print("Su edad es: ",edad)
print("Su signo zodiacal es: ",signo)
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
sexo=input("Ingrese su sexo (hombre o mujer): ")
hemoglobina=float(input("Ingrese su nivel de hemoblobina en la sangre (%): "))
#caja negra
edad=0
tiempo=""
if(mes_actual>mes_nacimiento):
    edad=(año_actual-año_nacimiento)
    tiempo="año(s)"
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
    tiempo="año(s)"
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
        tiempo="año(s)"
    elif(dia_actual>dia_nacimiento):
        edad(año_actual-año_nacimiento)
        tiempo="año(s)"
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
        tiempo="año(s)"
if(año_actual==año_nacimiento):
    edad=(mes_actual-mes_nacimiento)
    tiempo="mes(es)"

anemia=""
if((edad>0 and tiempo=="mes(es)") and (edad<=1 and tiempo=="mes(es)")and (hemoglobina>=13 and hemoglobina<=26)):
    anemia="Negativo"
elif((edad>1 and tiempo=="mes(es)") and (edad<=6 and tiempo=="mes(es)")and (hemoglobina>=10 and hemoglobina<=18)):
    anemia="Negativo"
elif((edad>6 and tiempo=="mes(es)") and (edad<=12 and tiempo=="mes(es)")and (hemoglobina>=11 and hemoglobina<=15)):
    anemia="Negativo"
elif((edad>1 and tiempo=="año(s)") and (edad<=5 and tiempo=="año(s)")and (hemoglobina>=11.5 and hemoglobina<=15)):
    anemia="Negativo"
elif((edad>5 and tiempo=="año(s)") and (edad<=10 and tiempo=="año(s)")and (hemoglobina>=12.6 and hemoglobina<=15.5)):
    anemia="Negativo"
elif((edad>10 and tiempo=="año(s)") and (edad<=15 and tiempo=="año(s)")and (hemoglobina>=13 and hemoglobina<=15.5)):
    anemia="Negativo"
elif((edad>15 and tiempo=="año(s)") and (sexo=="mujer")and (hemoglobina>=12 and hemoglobina<=16)):
    anemia="Negativo"
elif((edad>15 and tiempo=="año(s)") and (sexo=="hombre")and (hemoglobina>=14 and hemoglobina<=18)):
    anemia="Negativo"
else:
    anemia="Positivo"
#salidas
print("Su edad es: ",edad,tiempo)
print("Su resultado de anemia es:",anemia)
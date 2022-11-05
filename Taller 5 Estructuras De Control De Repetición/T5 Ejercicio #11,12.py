total_consumen=0
mujeres_menores=0
hombres=0
promedio_edad_cerveza=0
whisky=0
porc_whisky_encuestado=0
def encuesta(licor: [(bool, str, int, str)]):
    for consume,favorito,edad,sexo in encuesta:
        if(consume==True):
            total_consumen=total_consumen+1
        if(sexo=="mujer" and edad<18):
            mujeres_menores=mujeres_menores+1
        if(sexo=="hombre" and favorito!="aguardiente" and edad>=20 and edad<=25):
            hombres=hombres+1
        if(consume==True and favorito=="cerveza"):
            promedio_cerveza=(edad/len(encuesta))
        if(consume==True and favorito=="whisky"):
            whisky=whisky+1
            porc_whisky_encuestado=(whisky/len(encuesta))*100
    return total_consumen, mujeres_menores, hombres, promedio_edad_cerveza, porc_whisky_encuestado
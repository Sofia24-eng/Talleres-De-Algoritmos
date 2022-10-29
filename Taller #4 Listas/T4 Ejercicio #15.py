# Función para resolver el Ejercicio 15
#def ejercicio15(contagiados: ...
def ejercicio15(contagiados:[(str, int, int, bool)]) -> (int, int):
    mujeres_60=0
    menores=0
    for genero, edad, dias, fallece in contagiados:
        if(genero=="F" and edad>60 and fallece==True):
            mujeres_60=mujeres_60+1
        if(edad<18 and dias>7):
            menores=menores+1
    return mujeres_60, menores
# Pruebas de la función anterior
assert (ejercicio15([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True)])) == (4, 3)
print("Prueba superada 💪🏽")  
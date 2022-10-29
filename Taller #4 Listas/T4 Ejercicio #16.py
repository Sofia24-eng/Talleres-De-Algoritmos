# Función para resolver el ejercicio 16
#def ejercicio16(contagiados: [( , , , , )]) -> (int, int):
def ejercicio16(contagiados:[(str, int, int, bool)]) -> (int, int):
    mujeres=0
    hombres=0
    for genero, edad, dias, fallece in contagiados:
        if(genero=="F" and fallece==True):
            mujeres=mujeres+1
        if(genero=="M" and fallece==True):
            hombres=hombres+1
    return mujeres, hombres
# Pruebas de la función anterior
assert (ejercicio16([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True), ('F', 72, 6, True)])) == (5, 3)
print("Prueba superada 💪🏽")   
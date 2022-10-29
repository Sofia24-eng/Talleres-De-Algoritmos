# Función para resolver el ejercicio 17
#def ejercicio17(contagiados: [(, , , ,)]) -> int:
def ejercicio17(contagiados:[(str, int, int, bool)]) -> (int, int):
    personas=0
    for genero, edad, dias, fallece in contagiados:
        if(edad>=20 and edad<=30 and fallece==False):
            personas=personas+1
    return personas
# Pruebas de la función anterior
assert (ejercicio17([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True), ('F', 72, 6, True), ('F', 26, 5, False)])) == 3
print("Prueba superada 💪🏽")   
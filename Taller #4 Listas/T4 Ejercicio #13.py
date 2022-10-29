# Función para resolver el ejercicio 13
def ejercicio13(empleados: [(str, int, float)]) -> int:
    total=0
    for a,b,c in empleados:
        if((a=="gerente" or a=="contador") and (b>=45 and b<=50) and (c<2000000)):
            total=total+1
    return total 
# Pruebas de la función anterior
assert (ejercicio13([("director", 38, 1500000), ("gerente", 47, 1_450_000), ("celador", 63, 700_000), ("director", 29, 2_700_000),
                    ("contador", 51, 1_900_000), ("contador", 49, 1_900_000), ("analista", 23, 11_200_000), ("gerente", 46, 1_200_000),
                    ("contador", 39, 2_100_000), ("profesional", 36, 2_100_000), ("gerente", 45, 1_050_000), ("contador", 46, 800_000)])) == 5
print("Prueba superada 💪🏽")  
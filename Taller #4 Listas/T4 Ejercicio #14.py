# Función para resolver el Ejercicio 14: Completar los datos de entrada
def ejercicio14(materias:[(str, int, int, int, int)]) -> int:
    perdidas=0
    for a,b,c,d,e in materias:
        nota_fn=((d*0.4)+(e*0.6))
        if(nota_fn<60):
            perdidas=perdidas+1
    return perdidas
# Pruebas para la función anterior
assert (ejercicio14([("calculo", 6, 1, 45, 67), ("frances", 3, 2, 77, 89), ("calculo", 6, 1, 72, 58), ("ecuaciones", 3, 4, 68, 61),
                    ("ingles basico", 3, 2, 79, 85), ("quimica", 4, 1, 88, 92), ("fisica", 3, 2, 56,61), ("procesos", 3, 4, 75, 77),
                    ("cultura", 2, 3, 33, 21), ("deportes", 2, 1, 98, 90), ("cocina", 3, 4, 79, 98), ("estadistica", 3, 4, 53, 10)])) == 4

print("Prueba superada 💪🏽") 
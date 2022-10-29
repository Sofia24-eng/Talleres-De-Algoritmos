# Función para contar partidos
def resultados_partidos(partidos:[(int, int)]) -> (int, int, int):
    gano=0
    empato=0
    perdio=0
    for a,b in partidos:
        if(a==b):
            empato=empato+1
        elif(a>b):
            gano=gano+1
        else:
            perdio=perdio+1
    return gano,empato,perdio
# prueba de la función anterior
assert (resultados_partidos([(1, 3), (0, 0), (4, 0), (5, 3), (2, 2), (4, 3), (1, 0), (1, 2), (0, 0), (3, 2), (3, 1), (7, 0), (0, 2), (3, 3), (4, 2), (3, 4)])) == (8, 4, 4)
print("Prueba superada 💪🏽")
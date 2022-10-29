# Función que cuenta en una lista
def contar_temperaturas(temps: [float]) -> int:
    c=0
    for i in temps:
        if(i>=15 and i<=20):
            c=c+1
    return c


# Pruebas de la función anterior
assert contar_temperaturas([11, 18, 23.5, 19.5, 6, 16.3, 22.1, 4.6, 18.9, 18.6, 15.1, 16.1, 19.9, 1.5, 12, 21.7]) == 8
print("Prueba superada 💪🏽")
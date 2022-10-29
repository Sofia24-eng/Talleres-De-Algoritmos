# Función que cuenta los múltiplos
def ejercicio10(numeros: [int]) -> int:
    multiplos=0
    for i in numeros:
        if(i%2==0 and i%3==0 and i%5==0):
            multiplos=multiplos+1
    return multiplos

# Pruebas para la función anterior
assert (ejercicio10([5, 10, 30, 25, 24, 60, 12, 100, 120, 15, 90, 95, 36, 35, 72, 180])) == 5
print("Prueba superada 💪🏽")
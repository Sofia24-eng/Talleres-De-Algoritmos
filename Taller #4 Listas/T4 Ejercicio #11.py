# Función que cuenta el número de perros
def ejercicio11(perros: [str]) -> (int, int):
    fifi=0
    mateo=0
    for perro in perros:
        if(perro=="fifi"):
            fifi=fifi+1
        if(perro=="mateo"):
            mateo=mateo+1
    return fifi,mateo

# Prueba de la función anterior
assert (ejercicio11(["lila", "firulais", "romeo", "fifi", "neron", "milagro", "fifi", "lila", "cariño", "rosa", "fifi", "mateo", "rex"])) == (3,1)
print("Prueba superada 💪🏽")
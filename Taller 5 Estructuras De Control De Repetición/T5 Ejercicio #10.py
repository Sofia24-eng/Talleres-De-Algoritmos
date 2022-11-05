def estudiantes(altura: [float]) -> float:
    for i in altura:
        altura_maxima=max(altura)
    return altura_maxima
assert (estudiantes([1.67, 1.53, 1.70, 1.59, 2.11, 1.84, 1.50, 1.58, 2.00])) == 2.11
print("Prueba superada 💪🏽")
# Función que cuenta las vocales en una palabra
def ejercicio09(palabra: str) -> int:
  vocales=["a","e","i","o","u"]
  cantidad=0
  for i in palabra:
    if i in vocales:
      cantidad=cantidad+1
  return cantidad
# Pruebas de la función anterior
assert (ejercicio09("Lorem ipsum dolor sit Amet, consectetur adipiscing elit")) == 18
assert (ejercicio09("Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis")) == 25
print("Prueba superada 💪🏽")
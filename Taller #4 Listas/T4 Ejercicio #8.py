# Función que cuenta los menores de edad en una lista de edades
def ejercicio08(lista_edades:[int]) -> int:
  menores=0
  for i in lista_edades:
    if(i<18):
      menores=menores+1
  return menores
# Pruebas de la función anterior
assert ejercicio08([23, 31, 16, 11, 21, 18, 34, 45, 17, 16, 32, 43, 20, 19, 18, 16, 14, 33]) == 6
print("Prueba superada 💪🏽")
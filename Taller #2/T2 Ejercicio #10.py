#entradas
chel_aust=float(input("Digite una cantidad de chelines austriacos: ")) #1
drac_grie=float(input("Digite una cantidad de dracmas griegos: ")) #2
pesetas=float(input("DIgite una cantidad de pesetas: ")) #3 y #4
#caja negra
ch_pesetas=((chel_aust*956.871)/100) #1
drac_francos=((drac_grie*88.607)/(100*20.110)) #2
pes_dolar=(pesetas/122.499) #3
pes_liras=((pesetas*100)/9.289) #4
#salidas
print(chel_aust, "chelines austríacos equivalen a:",ch_pesetas,"pesetas") #1
print(drac_grie, "dracmas griegos equivalen a:",drac_francos,"francos franceses") #2
print(pesetas, "pesetas equivalen a:",pes_dolar,"dólares") #3
print(pesetas, "pesetas equivalen a:",pes_liras,"liras italianas") #4
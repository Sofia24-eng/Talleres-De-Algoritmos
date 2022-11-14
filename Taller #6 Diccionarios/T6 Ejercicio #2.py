Ejemplo={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lista=[]
for i in Ejemplo:
    if Ejemplo[i] not in lista:
        lista.append(Ejemplo[i])
print(lista)
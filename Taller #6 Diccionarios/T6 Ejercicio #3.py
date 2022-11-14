usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
 }
intento=1
while (intento <=3):
    Usuario=input("Escriba su usuario: ")
    Password=input("Escriba su contraseña: ")
    if Usuario in usuarios and Password == usuarios[Usuario]['password']:
        if(Usuario=="iperurena"):
            nombre=usuarios["iperurena"]['nombre']
            apellido=usuarios["iperurena"]['apellido']
        elif(Usuario=="aolaizola"):
            nombre=usuarios["aolaizola"]['nombre']
            apellido=usuarios["aolaizola"]['apellido']
        elif(Usuario=="fmuguruza"):
            nombre=usuarios["fmuguruza"]['nombre']
            apellido=usuarios["fmuguruza"]['apellido']
        print("Bienvenid@:",nombre,apellido)
        intento=4
    else:
        print("Incorrecto")
        if(intento==3):
            print("Intentos Fallidos")
    intento=intento+1
def mostrar(ingles):
    for español in ingles:
        traductor=0
        print(español,ingles[ingles])
        
traducciones = {
        "ES-EN": { "Perro": "Dog", "Silla": "Chair", "Mesa": "Table"},
        "EN-ES": { "Dog": "Perro", "Chair": "Silla", "Table": "Mesa",}
}


traductor=input("Ingrese una Palabra en Español para Traducirla en Ingles:")
if traductor=="Perro":
    print("Si Existe")
    print("Dog")

if traductor=="Silla":
    print("Si Existe")
    print("Chair")

elif traductor=="Mesa":
    print("Si Existe")
    print("Table")

else:
    print("No Esta Disponible la Traducción.")
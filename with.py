lista = ["platano\n", "apple"]

with open("datos.txt", "w") as fichero:
    fichero.writelines(lista)
fichero = open("datos.txt", "w")
lista = ["Manzana ", "Pera ", "Platano "]

fichero.writelines(lista)
fichero.close()
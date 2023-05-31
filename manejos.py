from io import open

archivo = open("archivo.txt","w")

frase = "this day is the better \n wednsday"

archivo.write(frase)

archivo.close()



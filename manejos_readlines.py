from io import open

reading = open("archivo.txt","r")

line = reading.readlines()

reading.close()

print(line[1])
from io import open

reading = open("archivo.txt","r")


print(reading.read())

reading.seek(0)

print(reading.read())
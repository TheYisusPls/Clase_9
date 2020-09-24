# haste la idea de que aqui hay un archivo de texto que contiene un lorem ipsum porfavor jaja

with open("Archivo.txt", "r") as f:
    lorem_ipsum = f.read()
    texto = lorem_ipsum.split()

palabra = ""

for i in texto:
    if len(i) > len(palabra):
        palabra = i

print("La palabra mas larga es!: {}.".format(palabra))









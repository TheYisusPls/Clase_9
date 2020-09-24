# primero hacer esto:
#   with open("Cree_este_archivo", "x") as f:
#     texto = f.write("Hola, como estas?")

with open("Cree_este_archivo", "r") as f:
    texto = f.read()

print(texto)
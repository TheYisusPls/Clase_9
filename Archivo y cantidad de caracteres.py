# imagina que aqui hay un archivo que se llama "Cree_este_archivo" y que tiene texto en su interior 

with open("Cree_este_archivo", "r") as f:
    texto = f.read()

print(len(texto))
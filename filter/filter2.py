# filtra palabras que comiencen con "p" de una lista 

palabras = ["perro", "gato", "pato", "hamster"]
palabras_con_p = list(filter(lambda x: x.startswith("p"), palabras))

print(f"Palabras: {palabras}")
print(f"Palabras que empiezan con 'p': {palabras_con_p}")
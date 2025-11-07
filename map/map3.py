# longitud de cada palabra en una lista

palabras = ["uno", "dos", "tres"]

longitudes = list(map(lambda p: len(p), palabras))

print(f"Palabras: {palabras}")
print(f"Longitudes: {longitudes}")
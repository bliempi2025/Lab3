# contanena una lista de cadenas en una sola 
from functools import reduce

cadenas = ["Hola", " ", "Mundo", "!"]

concatenado = reduce(lambda x, y: x + y, cadenas)

print(f"Cadenas: {cadenas}")
print(f"Concatenado: {concatenado}")
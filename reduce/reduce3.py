# encuentra el numero mayor en una lista 
from functools import reduce

numeros = [7, 3, 9, 1, 5]

# comparamos los dos numeros y devolvemos el mayor 
mayor = reduce(lambda x, y: x if x > y else y, numeros)

print(f"Numeros: {numeros}")
print(f"El mayor es: {mayor}")
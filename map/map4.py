# cuadrado de cada numero en una lista 

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, numeros)) 

print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")
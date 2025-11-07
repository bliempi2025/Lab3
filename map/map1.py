# multiplica cada numero de una lista por 10

numeros = [1, 2, 3, 4, 5]

multiplicados = list(map(lambda x: x * 10, numeros))

print(f"Lista original: {numeros}")
print(f"Lista multiplicada por 10: {multiplicados}")
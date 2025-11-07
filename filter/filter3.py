# filtra numeros mayores a 50

numeros = [10, 60, 30, 80, 50, 100]

mayores_a_50 = list(filter(lambda x: x > 50, numeros))

print(f"Números: {numeros}")
print(f"Mayores a 50: {mayores_a_50}")
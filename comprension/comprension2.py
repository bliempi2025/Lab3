# cuadrado de todos los numeros pares hasta el 20

cuadrados_pares = [i**2 for i in range(1, 21) if i % 2 == 0]

print("Cuadrados de pares del 1 al 20")
print(cuadrados_pares)
# numeros impares de una lista 

def solo_impares(lista_numeros):

    for num in lista_numeros:
        if num % 2 != 0:
            yield num

# lista de numeros del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista original: {numeros}")
print("Numeros impares de la lista")

for impar in solo_impares(numeros):
    print(impar)
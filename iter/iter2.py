# clase que genera los numeros impares del 1 al 20 


class ImparesUnoAVeinte:
    def __iter__(self):
        for i in range(1, 21):
            if i % 2 != 0:
                yield i


print("Numeros impares del 1 al 20")
generador_impares = ImparesUnoAVeinte()

# iteramos con un for 
for impar in generador_impares:
    print(impar)
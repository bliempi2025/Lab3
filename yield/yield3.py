# clase generadora de cuadrados

class CuadradosGenerador:
    def __init__(self, n):
        # inicia el generador hasta n
        self.n = n

    def __iter__(self):
        
        # metodo que genera los cuadrados de 1 a n
        for i in range(1, self.n + 1):
            yield i ** 2


print("Cuadrados del 1 al 10")
# itera sobre la instancia de la clase generadora
for cuadrado in CuadradosGenerador(10):
    print(cuadrado)
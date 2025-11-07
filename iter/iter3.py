# cuadrados del 1 al n sin iterador

class CuadradosSinIter:
    def __init__(self, n):
        self.n = n

    def obtener_lista(self):
        resultado = []
        for i in range(1, self.n + 1):
            resultado.append(i**2)
        return resultado [cite: 162]


print("Cuadrados del 1 al 10")
cuadrados = CuadradosSinIter(10)
lista_cuadrados = cuadrados.obtener_lista()
print(lista_cuadrados)
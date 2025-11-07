# contador del 10 al 15 usando iter y next

class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        # el propio objeto es el iterador 
        return self [cite: 86]

    def __next__(self):
        if self.actual <= self.fin:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            # lo lanzamos cuando termina
            raise StopIteration


print("Contador 10 a 15 con next")
mi_contador = Contador(10, 15)
mi_iterador = iter(mi_contador) # tenemos el iterador 

try:
    print(next(mi_iterador)) # 10
    print(next(mi_iterador)) # 11
    print(next(mi_iterador)) # 12
    print(next(mi_iterador)) # 13
    print(next(mi_iterador)) # 14
    print(next(mi_iterador)) # 15
    print(next(mi_iterador)) # el stopinteration
except StopIteration:
    print("Contador finalizado.")
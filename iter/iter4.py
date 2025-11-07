# iterador que devuelve cadenas en mayusculas 

class IteradorMayusculas:
    def __init__(self, lista_cadenas):
        self.cadenas = lista_cadenas
        self.indice = 0 # indice incial

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.cadenas):
            # obtenemos la cadena en mayusculas
            valor = self.cadenas[self.indice].upper()
            self.indice += 1
            return valor
        else:
            raise StopIteration


lista = ["hola", "mundo", "python"]
print(f"Lista original: {lista}")
print("Iterador en mayúsculas")
iterador_mayus = IteradorMayusculas(lista)

for mayuscula in iterador_mayus:
    print(mayuscula)
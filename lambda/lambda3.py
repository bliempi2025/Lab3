# devuelve primer elemento de una lista 

primer_elemento = lambda lista: lista[0] if lista else None

print("Lambda: Primer elemento")
print(f"Primer elemento de [10, 20, 30]: {primer_elemento([10, 20, 30])}")
print(f"Primer elemento de ['a', 'b']: {primer_elemento(['a', 'b'])}")
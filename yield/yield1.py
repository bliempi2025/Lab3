# primeros diez numeros pares 

def primeros_diez_pares():

    # funcion que genera los numeros del 0 al 18

    contador = 0
    numero = 0
    while contador < 10:
        yield numero
        numero += 2
        contador += 1

# recorremos el generador y mostramos los numeros 

print("Primeros 10 numeros pares")
for par in primeros_diez_pares():
    print(par)
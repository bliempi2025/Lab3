# fibonacci usando yield

def fibonacci(elementos):
    # funcion que genera la serie de Fibonacci
    a, b = 0, 1
    contador = 0
    while contador < elementos:
        yield a
        a, b = b, a + b
        contador += 1

print("10 primeros elementos de Fibonacci")
for num in fibonacci(10):
    print(num)
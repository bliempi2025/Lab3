# devuelve el mayor de dos numeros

mayor = lambda x, y: x if x > y else y

print("Lambda: Mayor de dos numeros")
print(f"Mayor entre 10 y 5: {mayor(10, 5)}")
print(f"Mayor entre 3 y 8: {mayor(3, 8)}")
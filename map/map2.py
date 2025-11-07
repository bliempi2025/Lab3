# convertidor de celsius a fahrenheit

celsius = [0, 10, 20, 30]  

# formula: (x * 9/5) + 32
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius)) 

print(f"Grados Celsius: {celsius}")
print(f"Grados Fahrenheit: {fahrenheit}")
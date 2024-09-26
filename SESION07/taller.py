"""
Escribir un programa que cree una lista con los números de 1 a 100(ambos incluidos), sustituyendo posteriormente los elementos siguientes:

posiciones múltiplos de 3 por la palabra "fizz"
posiciones múltiplos de 5 por la palabra "buzz"
posiciones múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

# Crear una lista vacía
numeros = []

# Solicitar al usuario que ingrese números entre 1 y 100
print("Ingresa números entre 1 y 100. Escribe 'fin' para terminar.")
while True:
    entrada = input("Número: ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)
        if 1 <= numero <= 100:
            numeros.append(numero)
        else:
            print("Por favor, ingresa un número entre 1 y 100.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

# Mostrar la lista original
print("\nLista original:")
print(numeros)

# Modificar la lista
for i in range(len(numeros)):
    if numeros[i] % 15 == 0:
        numeros[i] = "fizzbuzz"
    elif numeros[i] % 3 == 0:
        numeros[i] = "fizz"
    elif numeros[i] % 5 == 0:
        numeros[i] = "buzz"

# Mostrar la lista modificada
print("\nLista modificada:")
print(numeros)

#Encontrar Números Primos y Descomponer Números en Factores Primos

def es_primo(n):
    """Función para verificar si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(rango):
    """Encuentra todos los números primos en un rango."""
    return [num for num in range(rango[0], rango[1]+1) if es_primo(num)]

def descomponer_en_factores_primos(n):
    """Descompone un número en sus factores primos."""
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores

def clasificar_numeros(lista):
    """Clasifica los números de una lista como primos o no primos."""
    clasificacion = {
        "primos": [num for num in lista if es_primo(num)],
        "no_primos": [num for num in lista if not es_primo(num)]
    }
    return clasificacion

# Lista de números y rango para encontrar primos
numeros = [10, 15, 23, 30, 41, 55]
rango_primos = (10, 50)

# Encontrar primos en un rango
primos_encontrados = encontrar_primos(rango_primos)
print(f"Números primos entre {rango_primos[0]} y {rango_primos[1]}: {primos_encontrados}")

# Descomponer cada número en la lista en factores primos
for num in numeros:
    factores = descomponer_en_factores_primos(num)
    print(f"Factores primos de {num}: {factores}")

# Clasificar los números de la lista como primos o no primos
clasificacion = clasificar_numeros(numeros)
print(f"Números primos en la lista: {clasificacion['primos']}")
print(f"Números no primos en la lista: {clasificacion['no_primos']}")

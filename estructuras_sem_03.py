# -*- coding: utf-8 -*-
"""estructuras_sem_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q7BvGvGQFmd5iBXcpJj1z3XcnWu7oTJ0

##Ejercicio I: Suma de elementos
Dado un arreglo de números enteros, escriban un programa que calcule Ia suma de
todos los elementos del arreglo.
"""

def main():
    arreglo = [1, 2, 3, 4, 5]
    print(f"La suma de los elementos del arreglo {arreglo} es {sum(arreglo)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 2: Encontrar el máximo y mínimo
Desarrollen un programa que encuentre el valor máximo y mínimo en un arreglo de
números enteros .
"""

def maximo_minimo(arreglo):
    max = arreglo[0]
    min = arreglo[0]
    for elemento in arreglo:
        if elemento > max:
            max = elemento
        elif elemento < min:
            min = elemento
    return max, min


def main():
    arreglo = [1, 2, 3, 4, 5]
    print(f"El valor máximo del arreglo {arreglo} es {maximo_minimo(arreglo)[0]} y el valor mínimo es {maximo_minimo(arreglo)[1]}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 3: Contar elementos pares e impares
Programa que cuente Ia cantidad de elementos pares e impares en un arreglo de
números enteros.
"""

def contar_pares_impares(arreglo):
    pares = 0
    impares = 0

    for i in arreglo:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_impares(arreglo)
print(f"Cantidad de elementos pares: {pares}")
print(f"Cantidad de elementos impares: {impares}")

#complejidad de tiempo: O(n)
#complejidad de espacio: O(1)

"""##Ejercicio 4: Búsqueda de un elemento
Desarrollen una función que busque Ia posición de un elemento específico en un
arreglo. Si el elemento no está presente, el programa debe indicar que no se
encontró .
"""

def buscar_elemento(arreglo, elemento):
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            return i
    return None

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 6

posicion = buscar_elemento(arreglo, elemento)

if posicion is not None:
    print(f"Elemento encontrado en la posición: {posicion}")
else:
    print("Elemento no encontrado en el arreglo")

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 5: Ordenar un arreglo
Implementar un algoritmo de ordenamiento, como el método de burbuja o el de
selección, para ordenar un arreglo de números enteros en orden ascendente.
"""

def ordenar_arreglo(arreglo):
    for i in range(len(arreglo)):
        for j in range(len(arreglo) - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

arreglo = [64, 34, 25, 12, 22, 11, 90]

ordenar_arreglo(arreglo)

print("Arreglo ordenado:")
for i in range(len(arreglo)):
    print("%d" % arreglo[i]),

#complejidad de tiempo: O(n^2)
#complejidad de espacio: O(n)

"""##Ejercicio 6: Eliminar duplicados
Escriban un programa que elimine los elementos duplicados de un arreglo y
devuelva un nuevo arreglo sin duplicados.
"""

def eliminar_duplicados(arreglo):
    nuevo_arreglo = []
    for i in arreglo:
        if i not in nuevo_arreglo:
            nuevo_arreglo.append(i)
    return nuevo_arreglo

arreglo = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25]

arreglo_sin_duplicados = eliminar_duplicados(arreglo)

print("Arreglo original:")
for i in range(len(arreglo)):
    print("%d" % arreglo[i]),

print("\nArreglo sin duplicados:")
for i in range(len(arreglo_sin_duplicados)):
    print("%d" % arreglo_sin_duplicados[i]),

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 7: Matriz de multiplicación
Generar una matriz de multiplicación para un número dado. Por ejemplo, si el
número es 5, Ia matriz mostraría la tabla de multiplicar del 1 al 5.
"""

def matriz_multiplicacion(numero):
    matriz = []
    for i in range(1, numero + 1):
        fila = []
        for j in range(1, numero + 1):
            fila.append(i * j)
        matriz.append(fila)
    return matriz

numero = 5
matriz = matriz_multiplicacion(numero)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print("%d" % matriz[i][j]),
    print("\n")

#complejidad de tiempo: O(n^2)
#complejidad de espacio: O(n^2)

"""##Ejercicio 8: Palabras más largas
Desarrollen un programa que encuentre Ia palabra más larga en un arreglo de
palabras .
"""

def palabra_mas_larga(palabras):
    max_length = 0
    max_word = ""
    for palabra in palabras:
        if len(palabra) > max_length:
            max_length = len(palabra)
            max_word = palabra
    return max_word

palabras = ["estructuras", "de", "datos", "y", "algoritmos"]
print("la palabras mas laraga es: ",palabra_mas_larga(palabras))


#complejidad de tiempo: O(n)
#complejidad de espacio: O(1)

"""##Ejercicio 9: Suma de matrices
Escriban un programa que sume dos matrices y devuelva el resultado.
"""

def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener el mismo tamaño")

    filas = len(matriz1)
    columnas = len(matriz1[0])

    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(suma_matrices(matriz1, matriz2))

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 10: Fibonacci con arreglos
Solicita a los estudiantes que generen Ia secuencia de Fibonacci utilizando un
arreglo. EI programa debe imprimir los primeros n números de Ia secuencia de
Fibonacci .
"""

def fibonacci(n):
    if n <= 0:
        raise ValueError("El tamaño de la secuencia debe ser un número positivo")

    secuencia = [0, 1]

    for i in range(2, n):
        secuencia.append(secuencia[i-1] + secuencia[i-2])

    return secuencia


print(fibonacci(10))

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)
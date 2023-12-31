# -*- coding: utf-8 -*-
"""Estructuras_sem_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1705jNmnSVR_PlfJB45_U_LA0msr4APsQ

##Ejercicio I: Factorial Recursivo
Escribe una función recursiva para calcular el factorial de un número entero n.
"""

def factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def main():
    n = int(input("Ingrese un número: "))
    print(f"El factorial de {n} es {factorial(n)}")


if __name__ == "__main__":
    main()
#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 2: Suma de Números Naturales
Escribe una función recursiva para calcular Ia suma de los primeros n números
naturales.
"""

def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def main():
    n = int(input("Ingrese un número: "))
    print(f"La suma de los primeros {n} números naturales es {suma_naturales(n)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 3: Fibonacci Recursivo
Escribe una función recursiva para calcular el n—ésimo número de Ia secuencia
de Fibonacci.
"""

# Función recursiva para calcular el n-ésimo número de la secuencia de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Programa principal
def main():
    n = int(input("Ingrese un número: "))
    print(f"El {n}-ésimo número de Fibonacci es {fibonacci(n)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 4: Potencia Recursiva
Escribe una función recursiva para calcular x elevado a Ia potencia n.
"""

def potencia(x, n):
    return x ** n


def main():
    x = float(input("Ingrese un número: "))
    n = int(input("Ingrese la potencia: "))
    print(f"x elevado a la potencia n es: {potencia(x, n)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(n)
#complejidad de espacio: O(n)

"""##Ejercicio 5: Suma de Dígitos
Escribe una función recursiva que calcule ta suma de los dígitos de un número
entero positivo.
"""

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


def main():
    n = int(input("Ingrese un número entero positivo: "))
    print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(log n)
#complejidad de espacio: O(1)

"""##Ejercicio 6: Conteo de Caracteres
Escribe una función recursiva que cuente ta cantidad de veces que un carácter
específico aparece en una cadena.
"""

def contar_caracteres(cadena, caracter):
    if len(cadena) == 0:
        return 0
    elif cadena[0] == caracter:
        return 1 + contar_caracteres(cadena[1:], caracter)
    else:
        return contar_caracteres(cadena[1:], caracter)


def main():
    cadena = input("Ingrese una cadena: ")
    caracter = input("Ingrese un carácter: ")
    print(f"El caracter {caracter} aparece {contar_caracteres(cadena, caracter)} veces en la cadena {cadena}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(1)
#complejidad de espacio: O(1)

"""##Ejercicio 7: Suma de Elementos en Lista
Escribe una función recursiva para calcular Ia suma de los elementos en una
lista.

"""

def suma_elementos(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_elementos(lista[1:])


def main():
    lista = [1, 2, 3, 4, 5]
    print(f"La suma de los elementos de la lista {lista} es {suma_elementos(lista)}")


if __name__ == "__main__":
    main()

#complejidad de tiempo: O(1)
#complejidad de espacio: O(1)
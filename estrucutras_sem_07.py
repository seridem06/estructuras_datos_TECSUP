# -*- coding: utf-8 -*-
"""estrucutras_sem_07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bh6_FkNNNBpSHw9f-BcNuhnSMV78eQtW

##Ejercicio 1: Impplementacion de una tabla hash basica
implementar una tabla hash simple utilizando un arreglo y una funcion de hash
basica(por ejemplo, modulo). deben agregar operaciones para insertar elementos
(clave-valor), buscar elementos por clave y eliminar elementos.
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return


# Ejemplo de uso
hash_table = HashTable()
hash_table.insert('test1', 'value1')
hash_table.insert('test2', 'value2')
hash_table.insert('test3', 'value3')

print(hash_table.search('test1')) # Devuelve 'value1'
print(hash_table.search('test4')) # Devuelve None

hash_table.delete('test1')
print(hash_table.search('test1')) # Devuelve None

#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 2: Solucion de coilsiones con listas enlazadas
pide a tus estudiantes de modifiquen su implementacion la tabla hash para manejar
colisiones utilizando listas enlazadas en cada buquet. Deben implementar operaciones
para manejar colisones, como agregar elementos en una lista enlazada dentro del bucket y
buscar elementos en la lista enlazada.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            return
        if node.key == key:
            self.table[index] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return


# Ejemplo de uso
hash_table = HashTable()
hash_table.insert('test1', 'value1')
hash_table.insert('test2', 'value2')
hash_table.insert('test3', 'value3')

print(hash_table.search('test1')) # Devuelve 'value1'
print(hash_table.search('test4')) # Devuelve None

hash_table.delete('test1')
print(hash_table.search('test1')) # Devuelve None

#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicion 3: Implementacion de una tabla hash con funcion de hash nmejorada
implementar una funcion de hash corta mas robusta, como el metodo de hash de cadena
de caracteres "djb2", y utilizarla en su implementacion de la tabla hash. Esto
mejorara la distribucion de los elementos en la tabla y reducira las colisiones.

"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        hash_value = 5381
        for char in str(key):
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        if node is None:
            return
        if node.key == key:
            self.table[index] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return

# Ejemplo de uso
hash_table = HashTable()
hash_table.insert('test1', 'value1')
hash_table.insert('test2', 'value2')
hash_table.insert('test3', 'value3')

print(hash_table.search('test1')) # Devuelve 'value1'
print(hash_table.search('test4')) # Devuelve None

hash_table.delete('test1')
print(hash_table.search('test1')) # Devuelve None

"""##Ejercicio 4: Contador de frecuencia de palabras
Desarrollen un programa de tome un texto y cuenta la frecuencia de aparicion
de cada palabra utlizando una tabla hash. Cada palabra sera una clave en la
tabla y el valor asociado sera su frecuencia.

"""

def word_frequency(text):
    words = text.split()
    freq_table = {}

    for word in words:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table


def main():
    text = input("Ingrese el texto: ")
    freq_table = word_frequency(text)

    print("Frecuencia de palabras:")
    for word, freq in freq_table.items():
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 5: eliminacion de duplicados en un arreglo
crear un programa  que tome un arreglo de numeros y elimine los elementos
duplicados utilizando una tabla hash para rastrear los elementos unicos.


"""

def remove_duplicates(nums):
    num_set = {}
    unique_nums = []

    for num in nums:
        if num not in num_set:
            num_set[num] = True
            unique_nums.append(num)

    return unique_nums


def main():
    nums = list(map(int, input("Ingrese los numeros separados por espacios: ").split()))
    unique_nums = remove_duplicates(nums)

    print("Numeros sin duplicados:")
    for num in unique_nums:
        print(num)


if __name__ == "__main__":
    main()


#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 6: implemtacion de un diccionario
implementar un diccionario utlizando una tabla hash. Deben permitir la
insercion, busqueda y eliminacion de definiciones(clave-definicion).


"""

class Dictionary:
    def __init__(self):
        self.size = 0
        self.table = {}

    def insert(self, key, definition):
        if key not in self.table:
            self.table[key] = definition
            self.size += 1

    def search(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return None

    def delete(self, key):
        if key in self.table:
            del self.table[key]
            self.size -= 1

    def print_dictionary(self):
        for key, definition in self.table.items():
            print(f"{key}: {definition}")


def main():
    dictionary = Dictionary()

    while True:
        print("\nMenu de opciones:")
        print("1. Insertar definición")
        print("2. Buscar definición")
        print("3. Eliminar definición")
        print("4. Imprimir diccionario")
        print("5. Salir")

        option = int(input("Ingrese el número de la opción deseada: "))

        if option == 1:
            key = input("Ingrese la clave: ")
            definition = input("Ingrese la definición: ")
            dictionary.insert(key, definition)
        elif option == 2:
            key = input("Ingrese la clave: ")
            result = dictionary.search(key)
            if result:
                print(f"Definición: {result}")
            else:
                print("La clave no se encuentra en el diccionario.")
        elif option == 3:
            key = input("Ingrese la clave: ")
            dictionary.delete(key)
        elif option == 4:
            dictionary.print_dictionary()
        elif option == 5:
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()


#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 7: solucion de coliciones con sondeo lineal
desarrolla un programa que maneje colsiones utiklizando sondeo lineal en cada bucket. cuando ocurre una colision, los elementos se agregan
en la siguiente poscision disponible en la lista enlazada dentro del bucket


"""

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashEntry(key, value)
        else:
            entry = self.table[index]
            while entry.next is not None:
                entry = entry.next
            entry.next = HashEntry(key, value)

    def search(self, key):
        index = self.hash_function(key)
        entry = self.table[index]
        while entry is not None:
            if entry.key == key:
                return entry.value
            entry = entry.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        entry = self.table[index]
        if entry is None:
            return
        if entry.key == key:
            self.table[index] = entry.next
            return
        while entry.next is not None:
            if entry.next.key == key:
                entry.next = entry.next.next
                return
            entry = entry.next

    def print_dictionary(self):
        for i in range(self.size):
            entry = self.table[i]
            while entry is not None:
                print(f"{entry.key}: {entry.value}")
                entry = entry.next


def main():
    hash_table = HashTable(10)

    hash_table.insert("clave1", "definición1")
    hash_table.insert("clave2", "definición2")
    hash_table.insert("clave3", "definición3")
    hash_table.insert("clave4", "definición4")

    hash_table.print_dictionary()

    print("\nBúsqueda:")
    print(f"Definición de clave1: {hash_table.search('clave1')}")
    print(f"Definición de clave2: {hash_table.search('clave2')}")

    print("\nEliminación:")
    hash_table.delete("clave1")
    hash_table.delete("clave2")

    hash_table.print_dictionary()


if __name__ == "__main__":
    main()


#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 8: solucion de coliciones con sondeo cuadratico
desarrolla un programa que maneje colisiones utilizando sondeo cuadratico en
cada bucket. Cuendo ocurre una colision, los elementos se agregan en la
siguiente posicion disponible en la lista enlazada dentro del bucket.

"""

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def quadratic_probe(self, index):
        return (index * index + index) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = self.quadratic_probe(index + 1)
        self.table[index] = HashEntry(key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = self.quadratic_probe(index + 1)
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = self.table[index].next
                return
            index = self.quadratic_probe(index + 1)

    def print_dictionary(self):
        for i in range(self.size):
            entry = self.table[i]
            while entry is not None:
                print(f"{entry.key}: {entry.value}")
                entry = entry.next


def main():
    hash_table = HashTable(10)

    hash_table.insert("clave1", "definición1")
    hash_table.insert("clave2", "definición2")
    hash_table.insert("clave3", "definición3")
    hash_table.insert("clave4", "definición4")

    hash_table.print_dictionary()

    print("\nBúsqueda:")
    print(f"Definición de clave1: {hash_table.search('clave1')}")
    print(f"Definición de clave2: {hash_table.search('clave2')}")

    print("\nEliminación:")
    hash_table.delete("clave1")
    hash_table.delete("clave2")

    hash_table.print_dictionary()


if __name__ == "__main__":
    main()


#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##Ejercicio 9: solcion de colisiones con hashing doble
desarrolla un programa que maneje colisiones utilizando hashing doble en cada
bucket. Cuando ocurre cada colision, los elementos se agregan en la siguiente
posicion disponible en la lista enlazada dentro del bucket. h1 = key % 11 and h2 = 8 -(key % 8)




"""

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function1(self, key):
        return key % 11

    def hash_function2(self, key):
        return 8 - (key % 8)

    def insert(self, key, value):
        index = self.hash_function1(key)
        position = self.hash_function2(key)
        while self.table[index] is not None:
            index = (index + position) % self.size
        self.table[index] = HashEntry(key, value)

    def search(self, key):
        index = self.hash_function1(key)
        position = self.hash_function2(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + position) % self.size
        return None

    def delete(self, key):
        index = self.hash_function1(key)
        position = self.hash_function2(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = self.table[index].next
                return
            index = (index + position) % self.size

    def print_dictionary(self):
        for i in range(self.size):
            entry = self.table[i]
            while entry is not None:
                print(f"{entry.key}: {entry.value}")
                entry = entry.next


def main():
    hash_table = HashTable(11)

    hash_table.insert("clave1", "definición1")
    hash_table.insert("clave2", "definición2")
    hash_table.insert("clave3", "definición3")
    hash_table.insert("clave4", "definición4")

    hash_table.print_dictionary()

    print("\nBúsqueda:")
    print(f"Definición de clave1: {hash_table.search('clave1')}")
    print(f"Definición de clave2: {hash_table.search('clave2')}")

    print("\nEliminación:")
    hash_table.delete("clave1")
    hash_table.delete("clave2")

    hash_table.print_dictionary()


if __name__ == "__main__":
    main()


#COMPLEJIDAD DE TIEMPO: O(1)
#COMPLEJIDAD DE ESPACIO: O(n)
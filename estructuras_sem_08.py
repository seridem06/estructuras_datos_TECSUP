# -*- coding: utf-8 -*-
"""estructuras_sem_08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8riRojRLMF_HJ04tzGw6gb-Y4LzQHT5

##Ejercicio 1: Implementacion de un arbol binario de busqueda
Implementar un arbol binario simple utilizando. Agregar operaciones para
insertar elementos, buscar elementos por clave y eliminar elementos.
Tambien, los tres recorridos mencionados.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif(key > root.val):
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

r = Node(50)
keys = [30, 20, 40, 70, 60, 80]

for key in keys:
    r = insert(r, key)

print("Inorder traversal of the given tree")
inorder(r)

print("\nPreorder traversal of the given tree")
preorder(r)

print("\nPostorder traversal of the given tree")
postorder(r)

print("\nSearching for key 60:")
val = search(r, 60)
if val:
    print("Found:", val.val)
else:
    print("Key not found")

print("\nDeleting key 20")
r = delete(r, 20)
print("Inorder traversal after deletion of key 20:")
inorder(r)


#COMPLEJIDAD DE TIEMPO: O(log n)
#COMPLEJIDAD DE ESPACIO: O(n)

"""##
Ejercicion 2: Hallar la profundidad
tomando el arbol binario con los numeros 15, 10, 20, 5, 12, 18, y 25, calcula la profundidad
de un nodo  dado en el arbol. Por ejemplo, si se te da en el nodo 12. ¿puedes determinar su profundidad?

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def depth(root, key):
    if root is None:
        return 0
    if root.val == key:
        return 1
    left_depth = depth(root.left, key)
    right_depth = depth(root.right, key)
    if left_depth != 0:
        return left_depth + 1
    else:
        return right_depth + 1

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(12)
root.right.left = Node(18)
root.right.right = Node(25)

key = 12
print("The depth of the node {} is {}".format(key, depth(root, key)))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##
Ejercicio 3: Hallar la Altura
usando el mismo arbol binario, solicita a los estudiantes que encuentren la altura del arbol, esdecir la longitud del camino
mas largo desde la raiz.

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(12)
root.right.left = Node(18)
root.right.right = Node(25)

print("The height of the tree is {}".format(height(root)))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 4: Identificar el maximo y el minimo
Observa el siguiente arbol binario: 25,15, 30, 10, 20. Identifica cual es el
valor maximo y cual es el valor minimo en este arbol.


"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def get_max_min(root):
    if root is None:
        return None, None
    max_val = root.val
    min_val = root.val
    if root.left is not None:
        left_max, left_min = get_max_min(root.left)
        max_val = max(max_val, left_max)
        min_val = min(min_val, left_min)
    if root.right is not None:
        right_max, right_min = get_max_min(root.right)
        max_val = max(max_val, right_max)
        min_val = min(min_val, right_min)
    return max_val, min_val

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)

max_val, min_val = get_max_min(root)
print("The maximum value in the tree is {}".format(max_val))
print("The minimum value in the tree is {}".format(min_val))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 5: Numeros de nodos de hoja
Implementa un metodo que cuente cuantos nodos hoja tiene el arbol

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)

num_leaves = count_leaves(root)
print("The number of leaf nodes in the tree is {}".format(num_leaves))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 6: nodos hermanos
implementa un metodo que retorno si dos nodos son hermanos



"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_sibling(root, key1, key2):
    if root is None:
        return False

    left = root.left
    right = root.right

    if left is not None and left.val == key1 and right is not None and right.val == key2:
        return True
    if left is not None and left.val == key2 and right is not None and right.val == key1:
        return True

    return is_sibling(left, key1, key2) or is_sibling(right, key1, key2)

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)

print("Sibling check: ", is_sibling(root, 10, 20))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 7: tamaño del arbol
en el arbol binario con los numeros 15, 10, 20, 5, 12, 18 y 25 determina el tamaño
del arbol, esdecir, cuantos nodos hay en total en el arbol.

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def get_size(root):
    if root is None:
        return 0

    return 1 + get_size(root.left) + get_size(root.right)

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)
root.left.left.left = Node(5)
root.left.left.right = Node(12)
root.left.right.left = Node(18)
root.left.right.right = Node(25)

print("Size of tree: ", get_size(root))

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 8: Obtener ancestros
En el mismo binario, pide a los estudiantes qu ete ayuden a encontrar
los ancestros de un nodo especifico

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def get_ancestors(root, node_val, path=[]):
    if root is None:
        return None

    path.append(root.val)

    if root.val == node_val:
        return path

    left_ancestors = get_ancestors(root.left, node_val, path)
    if left_ancestors is not None:
        return left_ancestors

    right_ancestors = get_ancestors(root.right, node_val, path)
    if right_ancestors is not None:
        return right_ancestors

    path.pop()
    return None

root = Node(25)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(20)
root.left.left.left = Node(5)
root.left.left.right = Node(12)
root.left.right.left = Node(18)
root.left.right.right = Node(25)

node_val = 18
print("Ancestors of node", node_val, ": ", get_ancestors(root, node_val))
#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 9: Verificar si es arbol de busqueda
dado un arbol binario, verifica si cumple con la propiedad de ser un arbol de busqueda.
comprueba si, para cada nodo , todos los valores en su subarbol
izquierdo son menores y todos los valores en su sunarbol derecho son mayores.

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_bst(root, min_value, max_value):
    if root is None:
        return True

    if not min_value <= root.val <= max_value:
        return False

    return is_bst(root.left, min_value, root.val) and is_bst(root.right, root.val, max_value)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.left.right.left = Node(35)
root.right.left = Node(60)
root.right.right = Node(80)

if is_bst(root, float('-inf'), float('inf')):
    print("The tree is a binary search tree.")
else:
    print("The tree is not a binary search tree.")

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)

"""##Ejercicio 10: nodos a K distancia
dado un arbol binario de busqueda y un nodo especifico en el arbol, tu tareas es
implementar una funcion de devuelva todos los nodos que se encuentran a una
distancia k del nodo dado. La distancia se mide por la cantidad de aristas que se
deben recorrer para llegar de un nodo a otro.
"""

from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_k_distant_nodes(root, k):
    if root is None or k < 0:
        return []

    result = []
    queue = deque([(root, 0)])

    while queue:
        node, distance = queue.popleft()

        if distance == k:
            result.append(node.val)
        elif distance < k:
            if node.left:
                queue.append((node.left, distance + 1))
            if node.right:
                queue.append((node.right, distance + 1))

    return result

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.left.right.left = Node(35)
root.right.left = Node(60)
root.right.right = Node(80)

k = 3
print(f"Nodos a una distancia de  {k} del nodo dado: {find_k_distant_nodes(root, k)}")

#COMPLEJIDAD DE TIEMPO: O(n)
#COMPLEJIDAD DE ESPACIO: O(h)
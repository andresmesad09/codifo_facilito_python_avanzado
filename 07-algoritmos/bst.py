class Node:
    def __init__(self, key, value2):
        self.left = None
        self.right = None
        self.value = key
        self.value2 = value2

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value2):
        if self.root is None:
            self.root = Node(key, value2)
        else:
            self._insert(self.root, key, value2)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            # Nodo con solo un hijo o sin hijos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Nodo con dos hijos: obtener el sucesor inorden (el más pequeño en el subárbol derecho)
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, res):
        if node:
            self._inorder_traversal(node.left, res)
            res.append(node.value)
            self._inorder_traversal(node.right, res)
        return res

# Ejemplo de uso
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Recorrido inorden:", bst.inorder_traversal())  # Salida: [20, 30, 40, 50, 60, 70, 80]

print("Buscar 40:", bst.search(40) is not None)  # Salida: True
print("Buscar 90:", bst.search(90) is not None)  # Salida: False

bst.delete(20)
print("Recorrido inorden después de eliminar 20:", bst.inorder_traversal())  # Salida: [30, 40, 50, 60, 70, 80]

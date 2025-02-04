class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка значення в дерево"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)


    def find_min(self):
        """Знаходження найменшого значення в BST"""
        if self.root is None:
            return None  # Дерево порожнє
        current = self.root
        while current.left:  # Найменше значення — найлівіший вузол
            current = current.left
        return current.value


# Приклад використання
tree = BST()
values = [10, 5, 20, 15, 30, 25, 35, 12, 36]
for v in values:
    tree.insert(v)

print("Мінімальне значення в BST:", tree.find_min())

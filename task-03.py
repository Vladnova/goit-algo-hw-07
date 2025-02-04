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

    def sum_tree(self):
        """Знаходження суми всіх значень у дереві"""
        return self._sum_tree(self.root)

    def _sum_tree(self, node):
        if node is None:
            return 0
        return node.value + self._sum_tree(node.left) + self._sum_tree(node.right)


# Приклад використання
tree = BST()
values = [10, 5, 20, 15, 30, 25, 35]
for v in values:
    tree.insert(v)

print("Сума всіх значень у BST:", tree.sum_tree())

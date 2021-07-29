"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BTree:

    def __init__(self, node):
        self.root = node
        self.l_child = None
        self.r_child = None

    def __str__(self):
        return str(self.root)

    def binary_insert(self, data):
        if self.root > data:
            if self.l_child is None:
                self.l_child = BTree(data)
            else:
                self.l_child.binary_insert(data)
        else:
            if self.r_child is None:
                self.r_child = BTree(data)
            else:
                self.r_child.binary_insert(data)

    @staticmethod
    def in_order_print(root):
        if not root:
            return
        BTree.in_order_print(root.l_child)
        print(root.root)
        BTree.in_order_print(root.r_child)

    @staticmethod
    def pre_order_print(root):
        if not root:
            return
        print(root.root)
        BTree.pre_order_print(root.l_child)
        BTree.pre_order_print(root.r_child)


def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.l_child:
                next_level.append(n.l_child)
            if n.r_child:
                next_level.append(n.r_child)
        current_level = next_level


r = BTree(4)
r.binary_insert(7)
r.binary_insert(1)
r.binary_insert(5)
r.binary_insert(4)
r.binary_insert(2)
r.binary_insert(2)
r.binary_insert(3)
r.binary_insert(6)
r.binary_insert(0)

print("in order:")
BTree.in_order_print(r)

print("pre order")
BTree.pre_order_print(r)
print()
traverse(r)

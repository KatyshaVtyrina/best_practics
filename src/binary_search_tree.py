from src.node import Node

class BinarySearchTree:
    """Класс для представления бинарного дерева"""

    def __init__(self) -> None:
        """Дерево инициализируется пустым"""
        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, data: dict) -> None:
        """Добавляет данные в структуру дерева"""
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursive(self.__root, data)

    def _insert_recursive(self, node: Node, data: dict) -> None:
        """Рекурсивно ищем куда добавить словарь с данными"""
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, post_id: int) -> dict | None:
        """Ищем по id пост и возвращаем словарь с его данными"""

class Node:
    """Класс для узла стека"""


    def __init__(self, data, next_node = None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий узел в стеке (по умолчанию None)
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""


    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        node.next_node = self.top
        self.top = node


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        else:
            pop_node = self.top
            self.top = self.top.next_node
            pop_node.next_node = None
            return pop_node.data


    def __str__(self):
        if self.top.next_node != None:
            return f'''Вершина стэка: {self.top.data}
Следующий узел: {self.top.next_node.data}'''
        return f'Вершина стэка: {self.top.data}'

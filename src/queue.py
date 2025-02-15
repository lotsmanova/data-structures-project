class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""


    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None


    def enqueue(self, data: str) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node


    def dequeue(self) -> str:
        """
        Метод для удаления элемента из очереди.
        Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        pop_node = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return pop_node.data


    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return f''
        return f'{self.head.data}\n{self.head.next_node.data}\n' \
               f'{self.tail.data}'

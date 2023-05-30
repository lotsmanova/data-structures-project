class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data: dict) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None


    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет
        узел с этими данными в начало связанного списка
        """
        new_node = Node(data)
        last_node = self.head
        new_node.next_node = last_node
        self.head = new_node


    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет
        узел с этими данными в конец связанного списка
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node != None:
            last_node = last_node.next_node
        last_node.next_node = new_node


    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string


    def to_list(self) -> list:
        """
        Возвращает список с данными
        """
        nodelist = []
        node = self.head
        while node is not None:
            nodelist.append(node.data)
            node = node.next_node
        return nodelist


    def get_data_by_id(self, value: int):
        """
        Возвращает первый найденный в `LinkedList`
        словарь с ключом 'id'
        """
        try:
            node = self.head
            while node is not None:
                if isinstance(node.data, dict):
                    if node.data.get('id') == value:
                        return node.data
                node = node.next_node
            raise TypeError('Данные не являются словарем или в словаре нет id.')
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')

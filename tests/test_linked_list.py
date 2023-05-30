import unittest
from src.linked_list import Node, LinkedList

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})


    def test_insert_beginning(self):
        # TestCase#1 для добавления элемента в начало списка
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(str(self.ll), " {'id': 1} -> {'id': 0} -> {'id': 3} -> None")


    def test_insert_at_end(self):
        # TestCase#2 для добавления элемента в конец списка
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(str(self.ll), " {'id': 0} -> {'id': 3} -> {'id': 2} -> None")


    def test_to_list(self):
        # TestCase#3 для вывода списка данных
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEqual(self.ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])


    def test_get_data_by_id(self):
        # TestCase#4 поиск словаря по ключу 'id'
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(self.ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})


    def test_get_data_by_id_type_error(self):
        # TestCase#5 проверка выброса исключения TypeError
        self.assertRaises(TypeError, self.ll.get_data_by_id(2))


if __name__ == '__main__':
    unittest.main()
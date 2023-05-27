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

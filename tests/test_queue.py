import unittest
from src.queue import Node, Queue

class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        # фикстура
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')


    def test_enqueue(self):
        # TestCase#1 проверка добавления в очередь
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')


    def test_str(self):
        # TestCase#2 проверка строкового представления
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")


    def test_dequeue(self):
        # TestCase#3 проверка удаления из очереди
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
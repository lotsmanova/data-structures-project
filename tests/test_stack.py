import unittest
from src.stack import Node, Stack

class TestClass(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')


    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')


    def test_stack(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')


    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'data2')
        self.assertEqual(self.stack.pop(), 'data1')
        self.assertEqual(self.stack.pop(), None)


    def test_str(self):
        self.assertEqual(str(self.stack), 'Вершина стэка: data2\nСледующий узел: data1')


if __name__ == "__main__":
  unittest.main()
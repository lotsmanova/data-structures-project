import unittest
from src.stack import Node, Stack

class TestClass(unittest.TestCase):
    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')


    def test_stack(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')


if __name__ == "__main__":
  unittest.main()
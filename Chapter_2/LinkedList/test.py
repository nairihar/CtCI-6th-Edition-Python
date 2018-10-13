import unittest

from Node import Node

n_1 = Node(1)

n_2 = n_1.connect(2)

n_3 = n_2.connect(3)


class Test(unittest.TestCase):
    '''Test Cases'''

    def test_node_values(self):
      self.assertEqual(n_1.getValue(), 1)
      self.assertEqual(n_2.getValue(), 2)
      self.assertEqual(n_3.getValue(), 3)

    def test_node_reference_values(self):
      self.assertEqual(n_1.getNext().getValue(), n_2.getValue())
      self.assertEqual(n_2.getPrev().getValue(), n_1.getValue())

      self.assertEqual(n_2.getNext().getValue(), n_3.getValue())
      self.assertEqual(n_3.getPrev().getValue(), n_2.getValue())

if __name__ == "__main__":
    unittest.main()
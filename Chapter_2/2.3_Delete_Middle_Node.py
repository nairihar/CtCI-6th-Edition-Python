# ** implementation of a little different question 

import unittest
from math import floor

from LinkedList.Node import Node

def deleteMiddleNode(node):
  n = node
  count = 1

  while n.getNext() != None:
    count += 1
    n = n.getNext()
  
  n = node

  for i in range(floor(count/2)):
    n = n.getNext()
  
  n.getPrev().setNext(n.getNext())
  n.getNext().setPrev(n.getPrev())

class Test(unittest.TestCase):
    '''Test Cases'''

    def setUp(self):
      self.node = Node(1)
      self.node.connect(2).connect(3).connect(4).connect(5)
      deleteMiddleNode(self.node)

      self.node2 = Node(1)
      self.node2.connect(2).connect(3).connect(4)
      deleteMiddleNode(self.node2)

    def test_node_values_1(self):
      self.assertEqual(self.node.getValue(), 1)
      self.assertEqual(self.node.getNext().getValue(), 2)
      self.assertEqual(self.node.getNext().getNext().getValue(), 4)
      self.assertEqual(self.node.getNext().getNext().getNext().getValue(), 5)
      self.assertEqual(self.node.getNext().getNext().getNext().getNext(), None)

    def test_node_values_2(self):
      self.assertEqual(self.node2.getValue(), 1)
      self.assertEqual(self.node2.getNext().getValue(), 2)
      self.assertEqual(self.node2.getNext().getNext().getValue(), 4)
      self.assertEqual(self.node2.getNext().getNext().getNext(), None)

if __name__ == "__main__":
    unittest.main()

import unittest

from LinkedList.Node import Node

def removeDups(node, d={}):
  if node.getNext() == None:
    return

  d[node.getValue()] = True
  next_node = node.getNext()

  if next_node.getValue() in d:
    node.setNext(next_node.getNext())
    next_node.getNext().setPrev(node)
  
  return removeDups(node.getNext(), d)


class Test(unittest.TestCase):
    '''Test Cases'''

    def setUp(self):
      self.node = Node(1)
      self.node.connect(2).connect(3).connect(2).connect(4)
      removeDups(self.node)

    def test_node_values(self):
      self.assertEqual(self.node.getValue(), 1)
      self.assertEqual(self.node.getNext().getValue(), 2)
      self.assertEqual(self.node.getNext().getNext().getValue(), 3)
      self.assertEqual(self.node.getNext().getNext().getNext().getValue(), 4)
      self.assertEqual(self.node.getNext().getNext().getNext().getNext(), None)

if __name__ == "__main__":
    unittest.main()

# ** implementation of a little different question 

import unittest

from LinkedList.Node import Node

def getKthLastFromLinkedList(n, node, i, arr):
  if i < n:
    i += 1
    next_node = node.getNext()
    return getKthLastFromLinkedList(n, next_node, i, arr)
  
  value = node.getValue()
  arr.append(value)

  next_node = node.getNext()
  if next_node is not None:
    i += 1
    return getKthLastFromLinkedList(n, next_node, i, arr)
  else:
    return arr

def returnKthToLast(n, node):
  return getKthLastFromLinkedList(n, node, 1, [])

class Test(unittest.TestCase):
    '''Test Cases'''

    def setUp(self):
      self.node = Node(1)
      self.node.connect(2).connect(3).connect(2).connect(4)

    def test_node_values(self):
      self.assertEqual(returnKthToLast(2, self.node), [2,3,2,4])
     
if __name__ == "__main__":
    unittest.main()

import unittest

from LinkedList.Node import Node

def getReverseNumberFromLinkedList(node):
  num = 0
  multiply = 1

  while node is not None:
    v = node.getValue()

    num += v * multiply

    multiply *= 10
    node = node.getNext()

  return num

def getReverseLinkedListFromNumber(num):
  root_node = Node(None)
  node = root_node
  n = 0
  divide = 10

  while True:
    single_num = (num%divide) - n
    n += single_num

    if single_num == 0:
      break
    else:
      single_pure_num = single_num // (divide//10)
      if node.getValue() is None:
        node.setValue(single_pure_num)
      else:
        node.connect(single_pure_num)
        node = node.getNext()
    
    divide *= 10

  return root_node

def sumLists(node1, node2):
  number_1 = getReverseNumberFromLinkedList(node1)
  number_2 = getReverseNumberFromLinkedList(node2)

  sum = number_1 + number_2

  sum_node = getReverseLinkedListFromNumber(sum)

  return sum_node

class Test(unittest.TestCase):
  '''Test Cases'''

  def setUp(self):
    self.node1 = Node(7)
    self.node1.connect(1).connect(6)

    self.node2 = Node(5)
    self.node2.connect(9).connect(2)
  
  def testGetNumberFromList(self):
    self.assertEqual(getReverseNumberFromLinkedList(self.node1), 617)
    self.assertEqual(getReverseNumberFromLinkedList(self.node2), 295)

  def testGetListFromNumber(self):
    node = getReverseLinkedListFromNumber(123)
    self.assertEqual(node.getPrev(), None)
    self.assertEqual(node.getValue(), 3)
    self.assertEqual(node.getNext().getValue(), 2)
    self.assertEqual(node.getNext().getNext().getValue(), 1)
    self.assertEqual(node.getNext().getNext().getNext(), None)

  def testSumLists(self):
    sum_node = sumLists(self.node1, self.node2)
    self.assertEqual(sum_node.getPrev(), None)
    self.assertEqual(sum_node.getValue(), 2)
    self.assertEqual(sum_node.getNext().getValue(), 1)
    self.assertEqual(sum_node.getNext().getNext().getValue(), 9)
    self.assertEqual(sum_node.getNext().getNext().getNext(), None)

if __name__ == "__main__":
    unittest.main()

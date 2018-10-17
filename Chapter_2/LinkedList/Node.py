class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  
  def connect(self, value):
    new_node = Node(value)
    new_node.setPrev(self)

    self.setNext(new_node)
    
    return new_node

  def getValue(self):
    return self.value
  
  def setValue(self, value):
    self.value = value

  def getNext(self):
    return self.next

  def setNext(self, next_node):
    self.next = next_node

  def getPrev(self):
    return self.prev
  
  def setPrev(self, prev_node):
    self.prev = prev_node

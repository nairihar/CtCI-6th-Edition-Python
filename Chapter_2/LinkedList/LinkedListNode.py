class LinkedListNode:
  def __init__(self, value, nextNode=None):
    self.value = value
    self.next = nextNode
  
  def __str__(self):
    return str(self.value)

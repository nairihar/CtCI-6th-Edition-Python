from LinkedListNode import LinkedListNode

class LinkedList:
  def __init__(self, values):
    self.head = None
    self.tail = None

    if values:
      self.add_multiple(values)
  
  def __iter__(self):
    current = self.head
    while current:
      yield current
      current = current.next
  
  def __str__(self):
    current = self.head
    values = [str(x) for x in self]

    return '-->'.join(values)
  
  def __len__(self):
    count = 0
    node = self.head
    while node:
      count += 1
      node = node.next
    
    return count

  def add(self, value):
    if self.head is None:
      self.tail = self.head = LinkedListNode(value)
    else:
      self.tail.next = LinkedListNode(value)
      self.tail = self.tail.next
    
    return self.tail
  
  def add_to_beginning(self, value):
    if self.head is None:
      self.tail = self.head = LinkedListNode(value)
    else:
      self.head = LinkedListNode(value, self.head)
    
    return self.head

  def add_multiple(self, values):
    for value in values:
      self.add(value)


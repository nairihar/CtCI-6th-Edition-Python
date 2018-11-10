class Stack:
  def __init__(self, max_size=9999999):
    self.max_size = max_size
    self.stack = []
  
  def push(self, value):
    if self.size() == self.max_size:
      raise Exception('Max Stack size limit reached!')
    self.stack.insert(len(self.stack), value)
    return value
  
  def pop(self):
    if self.isEmpty():
      raise Exception('Size is empty!')
    return self.stack.pop()
  
  def peek(self):
    if self.isEmpty():
      raise Exception('Size is empty!')
    return self.stack[-1]
  
  def isEmpty(self):
    return len(self.stack) == 0
  
  def size(self):
    return len(self.stack)
  
  def getFullArray(self):
    return self.stack

